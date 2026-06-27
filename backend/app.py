import json
import os
import secrets
import sqlite3
import threading
from datetime import datetime, timedelta, timezone
from hmac import compare_digest
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "consultations.db"
HOST = os.environ.get("HOST", "127.0.0.1")
PORT = int(os.environ.get("PORT", "8000"))
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "K11223344!")
TOKEN_TTL = timedelta(hours=12)


db_lock = threading.Lock()
session_lock = threading.Lock()
sessions = {}


def utc_now():
    return datetime.now(timezone.utc)


def init_db():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS consultations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT NOT NULL,
                service TEXT NOT NULL,
                project_details TEXT NOT NULL,
                submitted_at TEXT NOT NULL
            )
            """
        )
        connection.commit()


def create_session():
    token = secrets.token_urlsafe(32)
    expires_at = utc_now() + TOKEN_TTL
    with session_lock:
        sessions[token] = expires_at
    return token


def is_session_valid(token):
    with session_lock:
        expires_at = sessions.get(token)
        if not expires_at:
            return False
        if expires_at <= utc_now():
            sessions.pop(token, None)
            return False
        return True


def revoke_session(token):
    if not token:
        return
    with session_lock:
        sessions.pop(token, None)


def cleanup_sessions():
    now = utc_now()
    with session_lock:
        expired_tokens = [token for token, expires_at in sessions.items() if expires_at <= now]
        for token in expired_tokens:
            sessions.pop(token, None)


def insert_consultation(payload):
    submitted_at = utc_now().isoformat()
    with db_lock, sqlite3.connect(DB_PATH) as connection:
        cursor = connection.execute(
            """
            INSERT INTO consultations (
                full_name,
                phone,
                email,
                service,
                project_details,
                submitted_at
            ) VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                payload["full_name"],
                payload["phone"],
                payload["email"],
                payload["service"],
                payload["project_details"],
                submitted_at,
            ),
        )
        connection.commit()
        return {
            "id": cursor.lastrowid,
            "submitted_at": submitted_at,
        }


def fetch_consultations():
    with db_lock, sqlite3.connect(DB_PATH) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            """
            SELECT id, full_name, phone, email, service, project_details, submitted_at
            FROM consultations
            ORDER BY datetime(submitted_at) DESC, id DESC
            """
        ).fetchall()
    return [dict(row) for row in rows]


class ApiHandler(BaseHTTPRequestHandler):
    server_version = "KarimiAdminServer/1.0"

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(HTTPStatus.NO_CONTENT)
        self.end_headers()

    def do_GET(self):
        cleanup_sessions()
        path = urlparse(self.path).path

        if path == "/api/health":
            self.respond_json(HTTPStatus.OK, {"ok": True})
            return

        if path == "/api/admin/submissions":
            token = self.extract_bearer_token()
            if not is_session_valid(token):
                self.respond_json(HTTPStatus.UNAUTHORIZED, {"error": "احراز هویت نامعتبر است."})
                return

            self.respond_json(HTTPStatus.OK, {"entries": fetch_consultations()})
            return

        self.respond_json(HTTPStatus.NOT_FOUND, {"error": "مسیر موردنظر پیدا نشد."})

    def do_POST(self):
        cleanup_sessions()
        path = urlparse(self.path).path
        payload = self.read_json_body()
        if payload is None:
            return

        if path == "/api/consultations":
            normalized = self.validate_consultation_payload(payload)
            if normalized is None:
                return

            saved = insert_consultation(normalized)
            self.respond_json(
                HTTPStatus.CREATED,
                {
                    "message": "درخواست مشاوره با موفقیت ثبت شد.",
                    "submission": saved,
                },
            )
            return

        if path == "/api/admin/login":
            password = str(payload.get("password", ""))
            if not compare_digest(password, ADMIN_PASSWORD):
                self.respond_json(HTTPStatus.UNAUTHORIZED, {"error": "رمز عبور نادرست است."})
                return

            token = create_session()
            self.respond_json(
                HTTPStatus.OK,
                {
                    "token": token,
                    "expires_in_seconds": int(TOKEN_TTL.total_seconds()),
                },
            )
            return

        if path == "/api/admin/logout":
            revoke_session(self.extract_bearer_token())
            self.respond_json(HTTPStatus.OK, {"ok": True})
            return

        self.respond_json(HTTPStatus.NOT_FOUND, {"error": "مسیر موردنظر پیدا نشد."})

    def read_json_body(self):
        content_length = int(self.headers.get("Content-Length", "0"))
        raw_body = self.rfile.read(content_length) if content_length > 0 else b"{}"

        try:
            return json.loads(raw_body.decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            self.respond_json(HTTPStatus.BAD_REQUEST, {"error": "بدنه درخواست معتبر نیست."})
            return None

    def validate_consultation_payload(self, payload):
        fields = {
            "full_name": str(payload.get("full_name", "")).strip(),
            "phone": str(payload.get("phone", "")).strip(),
            "email": str(payload.get("email", "")).strip(),
            "service": str(payload.get("service", "")).strip(),
            "project_details": str(payload.get("project_details", "")).strip(),
        }

        if any(not value for value in fields.values()):
            self.respond_json(HTTPStatus.BAD_REQUEST, {"error": "تمام فیلدهای فرم باید تکمیل شوند."})
            return None

        if len(fields["project_details"]) < 10:
            self.respond_json(HTTPStatus.BAD_REQUEST, {"error": "توضیحات پروژه باید دقیق‌تر ثبت شود."})
            return None

        return fields

    def extract_bearer_token(self):
        authorization = self.headers.get("Authorization", "")
        if not authorization.startswith("Bearer "):
            return ""
        return authorization[7:].strip()

    def respond_json(self, status, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        return


def run():
    init_db()
    server = ThreadingHTTPServer((HOST, PORT), ApiHandler)
    print(f"API server running on http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    run()
