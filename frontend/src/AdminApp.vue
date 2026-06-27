<script setup>
import { computed, onMounted, ref } from "vue";
import featureStrategyImage from "./assets/photos/feature-team.jpg";
import heroCollaborationImage from "./assets/photos/hero-team.jpg";

const API_BASE = (import.meta.env.VITE_API_BASE || "http://127.0.0.1:8000").replace(/\/$/, "");
const ADMIN_TOKEN_KEY = "karimi_admin_token";

const adminPassword = ref("");
const adminToken = ref(localStorage.getItem(ADMIN_TOKEN_KEY) || "");
const loginState = ref({ loading: false, type: "", message: "" });
const entriesState = ref({ loading: false, type: "", message: "" });
const entries = ref([]);

const formatter = new Intl.DateTimeFormat("fa-IR", {
  dateStyle: "medium",
  timeStyle: "short",
});

const requestJson = async (path, options = {}) => {
  const response = await fetch(`${API_BASE}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...(options.headers || {}),
    },
  });

  const contentType = response.headers.get("content-type") || "";
  const data = contentType.includes("application/json") ? await response.json() : null;

  if (!response.ok) {
    throw new Error(data?.error || "ارتباط با سرور انجام نشد.");
  }

  return data;
};

const formatDate = (value) => {
  if (!value) {
    return "-";
  }

  const date = new Date(value);
  if (Number.isNaN(date.getTime())) {
    return value;
  }

  return formatter.format(date);
};

const serviceLabel = (value) => value || "ثبت نشده";

const todayKey = new Date().toLocaleDateString("en-CA", { timeZone: "Asia/Tehran" });

const stats = computed(() => {
  const total = entries.value.length;
  const today = entries.value.filter((entry) => {
    const date = new Date(entry.submitted_at);
    if (Number.isNaN(date.getTime())) {
      return false;
    }
    return date.toLocaleDateString("en-CA", { timeZone: "Asia/Tehran" }) === todayKey;
  }).length;
  const services = new Set(entries.value.map((entry) => serviceLabel(entry.service))).size;

  return [
    { label: "کل درخواست ها", value: total },
    { label: "ثبت های امروز", value: today },
    { label: "نوع خدمت فعال", value: services },
  ];
});

const isAuthenticated = computed(() => adminToken.value.length > 0);

const persistToken = (token) => {
  adminToken.value = token;
  if (token) {
    localStorage.setItem(ADMIN_TOKEN_KEY, token);
  } else {
    localStorage.removeItem(ADMIN_TOKEN_KEY);
  }
};

const loadEntries = async () => {
  if (!adminToken.value) {
    return;
  }

  entriesState.value = { loading: true, type: "", message: "" };

  try {
    const data = await requestJson("/api/admin/submissions", {
      method: "GET",
      headers: {
        Authorization: `Bearer ${adminToken.value}`,
      },
    });

    entries.value = Array.isArray(data.entries) ? data.entries : [];
    entriesState.value = { loading: false, type: "success", message: "اطلاعات مشاوره ها بارگذاری شد." };
  } catch (error) {
    persistToken("");
    entries.value = [];
    entriesState.value = { loading: false, type: "error", message: error.message };
  }
};

const login = async () => {
  if (!adminPassword.value || loginState.value.loading) {
    return;
  }

  loginState.value = { loading: true, type: "", message: "" };

  try {
    const data = await requestJson("/api/admin/login", {
      method: "POST",
      body: JSON.stringify({ password: adminPassword.value }),
    });

    persistToken(data.token || "");
    adminPassword.value = "";
    loginState.value = { loading: false, type: "success", message: "ورود با موفقیت انجام شد." };
    await loadEntries();
  } catch (error) {
    loginState.value = { loading: false, type: "error", message: error.message };
  }
};

const logout = async () => {
  const token = adminToken.value;
  persistToken("");
  entries.value = [];
  entriesState.value = { loading: false, type: "", message: "" };

  if (!token) {
    return;
  }

  try {
    await requestJson("/api/admin/logout", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ ok: true }),
    });
  } catch {
    return;
  }
};

onMounted(() => {
  if (adminToken.value) {
    loadEntries();
  }
});
</script>

<template>
  <div class="admin-page">
    <header class="site-header admin-header-bar">
      <div class="container nav-shell admin-nav-shell">
        <a class="brand" href="/">
          <span class="brand-mark">ک</span>
          <span>
            <strong>شرکت توسعه نرم افزار کریمی</strong>
            <small>پنل مدیریت درخواست های مشاوره</small>
          </span>
        </a>

        <div class="admin-header-actions">
          <a class="button button-secondary admin-back-link" href="/">بازگشت به سایت</a>
          <button v-if="isAuthenticated" class="button button-primary" type="button" @click="logout">
            خروج از پنل
          </button>
        </div>
      </div>
    </header>

    <main class="admin-main-shell">

      <section v-if="isAuthenticated" class="section admin-list-section">
        <div class="container">
          <div class="section-heading reveal visible admin-list-heading">
            <div class="section-tag">درخواست های ثبت شده</div>
            <h2>فهرست کامل متقاضیان مشاوره</h2>
            <p>
              همه اطلاعات فرم از جمله نام، شماره تماس، ایمیل، نوع خدمت و توضیحات پروژه در اینجا نمایش داده می شود.
            </p>
          </div>

          <p
            v-if="entriesState.message"
            :class="[
              'site-form-note',
              entriesState.type === 'success' ? 'site-form-note-success' : 'site-form-note-error',
            ]"
          >
            {{ entriesState.message }}
          </p>

          <div v-if="entriesState.loading" class="admin-empty-state">
            <strong>در حال دریافت اطلاعات...</strong>
            <p>چند لحظه صبر کنید تا ثبت های مشاوره بارگذاری شوند.</p>
          </div>

          <div v-else-if="entries.length" class="admin-entry-grid">
            <article v-for="entry in entries" :key="entry.id" class="admin-entry-card reveal visible">
              <div class="admin-entry-header">
                <div>
                  <h3>{{ entry.full_name }}</h3>
                  <span>{{ formatDate(entry.submitted_at) }}</span>
                </div>
                <strong class="admin-entry-badge">{{ serviceLabel(entry.service) }}</strong>
              </div>

              <div class="admin-entry-meta">
                <div>
                  <span>شماره تماس</span>
                  <strong>{{ entry.phone }}</strong>
                </div>
                <div>
                  <span>ایمیل</span>
                  <strong>{{ entry.email }}</strong>
                </div>
              </div>

              <div class="admin-entry-details">
                <span>توضیحات پروژه</span>
                <p>{{ entry.project_details }}</p>
              </div>
            </article>
          </div>

          <div v-else class="admin-empty-state">
            <img :src="featureStrategyImage" alt="هنوز ثبت مشاوره ای وجود ندارد" />
            <strong>هنوز هیچ درخواست مشاوره ای ثبت نشده است</strong>
            <p>به محض ثبت فرم از سمت سایت، اطلاعات اینجا نمایش داده می شود.</p>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>
