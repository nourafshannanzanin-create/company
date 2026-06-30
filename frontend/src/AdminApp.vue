<script setup>
import { computed, onMounted, ref } from "vue";
import featureStrategyImage from "./assets/photos/team-profile.png";
import heroCollaborationImage from "./assets/photos/team-profile.png";

const API_BASE = (import.meta.env.VITE_API_BASE || "http://127.0.0.1:8000").replace(/\/$/, "");
const ADMIN_TOKEN_KEY = "karimi_admin_token";

const TEXT = {
  connectionError: "\u0627\u0631\u062a\u0628\u0627\u0637 \u0628\u0627 \u0633\u0631\u0648\u0631 \u0627\u0646\u062c\u0627\u0645 \u0646\u0634\u062f.",
  notProvided: "\u062b\u0628\u062a \u0646\u0634\u062f\u0647",
  statsTotal: "\u06a9\u0644 \u062f\u0631\u062e\u0648\u0627\u0633\u062a \u0647\u0627",
  statsToday: "\u062b\u0628\u062a \u0647\u0627\u06cc \u0627\u0645\u0631\u0648\u0632",
  statsServices: "\u0646\u0648\u0639 \u062e\u062f\u0645\u062a \u0641\u0639\u0627\u0644",
  entriesLoaded: "\u0627\u0637\u0644\u0627\u0639\u0627\u062a \u0645\u0634\u0627\u0648\u0631\u0647 \u0647\u0627 \u0628\u0627\u0631\u06af\u0630\u0627\u0631\u06cc \u0634\u062f.",
  loginSuccess: "\u0648\u0631\u0648\u062f \u0628\u0627 \u0645\u0648\u0641\u0642\u06cc\u062a \u0627\u0646\u062c\u0627\u0645 \u0634\u062f.",
  brandTitle: "\u0634\u0631\u06a9\u062a \u062a\u0648\u0633\u0639\u0647 \u0646\u0631\u0645 \u0627\u0641\u0632\u0627\u0631 \u06a9\u0631\u06cc\u0645\u06cc",
  brandSubtitle: "\u067e\u0646\u0644 \u0645\u062f\u06cc\u0631\u06cc\u062a \u062f\u0631\u062e\u0648\u0627\u0633\u062a \u0647\u0627\u06cc \u0645\u0634\u0627\u0648\u0631\u0647",
  backToSite: "\u0628\u0627\u0632\u06af\u0634\u062a \u0628\u0647 \u0633\u0627\u06cc\u062a",
  logout: "\u062e\u0631\u0648\u062c \u0627\u0632 \u067e\u0646\u0644",
  loginEyebrow: "\u0648\u0631\u0648\u062f \u0645\u062f\u06cc\u0631 \u0633\u06cc\u0633\u062a\u0645",
  loginTitle: "\u0648\u0631\u0648\u062f \u0627\u0645\u0646 \u0628\u0647 \u067e\u0646\u0644 \u0645\u062f\u06cc\u0631\u06cc\u062a \u062f\u0631\u062e\u0648\u0627\u0633\u062a \u0647\u0627\u06cc \u0645\u0634\u0627\u0648\u0631\u0647",
  loginDescription: "\u0627\u0632 \u0627\u06cc\u0646 \u0628\u062e\u0634 \u0645\u06cc \u062a\u0648\u0627\u0646\u06cc\u062f \u0647\u0645\u0647 \u0641\u0631\u0645 \u0647\u0627\u06cc \u062b\u0628\u062a \u0634\u062f\u0647 \u0631\u0627 \u0628\u0628\u06cc\u0646\u06cc\u062f\u060c \u0648\u0636\u0639\u06cc\u062a \u0648\u0631\u0648\u062f\u06cc \u0647\u0627\u06cc \u062c\u062f\u06cc\u062f \u0631\u0627 \u0628\u0631\u0631\u0633\u06cc \u06a9\u0646\u06cc\u062f \u0648 \u067e\u06cc\u06af\u06cc\u0631\u06cc \u062a\u06cc\u0645 \u0641\u0631\u0648\u0634 \u0631\u0627 \u0633\u0631\u06cc\u0639 \u062a\u0631 \u0627\u0646\u062c\u0627\u0645 \u062f\u0647\u06cc\u062f.",
  secureAccess: "\u0627\u0645\u0646",
  accessStatus: "\u0648\u0636\u0639\u06cc\u062a \u062f\u0633\u062a\u0631\u0633\u06cc",
  apiConnection: "\u0627\u062a\u0635\u0627\u0644 API",
  panelType: "\u0646\u0648\u0639 \u067e\u0646\u0644",
  management: "\u0645\u062f\u06cc\u0631\u06cc\u062a",
  adminHeroAlt: "\u0646\u0645\u0627\u06cc \u067e\u0646\u0644 \u0645\u062f\u06cc\u0631\u06cc\u062a \u0634\u0631\u06a9\u062a \u0646\u0631\u0645 \u0627\u0641\u0632\u0627\u0631\u06cc",
  internalPanel: "\u067e\u0646\u0644 \u062f\u0627\u062e\u0644\u06cc",
  requestsAccess: "\u062f\u0633\u062a\u0631\u0633\u06cc \u0628\u0647 \u062f\u0631\u062e\u0648\u0627\u0633\u062a \u0647\u0627",
  layeredAccess: "\u062f\u0633\u062a\u0631\u0633\u06cc \u0645\u0631\u062d\u0644\u0647 \u0627\u06cc",
  managerPasswordLogin: "\u0648\u0631\u0648\u062f \u0628\u0627 \u0631\u0645\u0632 \u0645\u062f\u06cc\u0631",
  quickFollowup: "\u067e\u06cc\u06af\u06cc\u0631\u06cc \u0633\u0631\u06cc\u0639",
  liveEntries: "\u0646\u0645\u0627\u06cc\u0634 \u0644\u062d\u0638\u0647 \u0627\u06cc \u062b\u0628\u062a \u0647\u0627",
  authTitle: "\u0627\u062d\u0631\u0627\u0632 \u0647\u0648\u06cc\u062a",
  loginCardTitle: "\u0628\u0631\u0627\u06cc \u0645\u0634\u0627\u0647\u062f\u0647 \u062f\u0631\u062e\u0648\u0627\u0633\u062a \u0647\u0627 \u0648\u0627\u0631\u062f \u0634\u0648\u06cc\u062f",
  loginCardDescription: "\u0631\u0645\u0632 \u0639\u0628\u0648\u0631 \u0645\u062f\u06cc\u0631 \u0631\u0627 \u0648\u0627\u0631\u062f \u06a9\u0646\u06cc\u062f \u062a\u0627 \u0641\u0647\u0631\u0633\u062a \u06a9\u0627\u0645\u0644 \u0641\u0631\u0645 \u0647\u0627\u06cc \u062b\u0628\u062a \u0634\u062f\u0647 \u062f\u0631 \u0627\u062e\u062a\u06cc\u0627\u0631 \u0634\u0645\u0627 \u0642\u0631\u0627\u0631 \u0628\u06af\u06cc\u0631\u062f.",
  adminPassword: "\u0631\u0645\u0632 \u0639\u0628\u0648\u0631 \u0645\u062f\u06cc\u0631\u06cc\u062a",
  adminPasswordPlaceholder: "\u0631\u0645\u0632 \u0639\u0628\u0648\u0631 \u0631\u0627 \u0648\u0627\u0631\u062f \u06a9\u0646\u06cc\u062f",
  loggingIn: "\u062f\u0631 \u062d\u0627\u0644 \u0648\u0631\u0648\u062f...",
  loginButton: "\u0648\u0631\u0648\u062f \u0628\u0647 \u067e\u0646\u0644",
  dashboardEyebrow: "\u062f\u0627\u0634\u0628\u0648\u0631\u062f \u0645\u062f\u06cc\u0631\u06cc\u062a",
  dashboardTitle: "\u0641\u0647\u0631\u0633\u062a \u062f\u0631\u062e\u0648\u0627\u0633\u062a \u0647\u0627\u06cc \u0645\u0634\u0627\u0648\u0631\u0647 \u0647\u0645\u06cc\u0634\u0647 \u062f\u0631 \u062f\u0633\u062a\u0631\u0633 \u0634\u0645\u0627\u0633\u062a",
  dashboardDescription: "\u0627\u06cc\u0646 \u0646\u0645\u0627\u06cc \u0645\u062f\u06cc\u0631\u06cc\u062a\u06cc\u060c \u062b\u0628\u062a \u0647\u0627\u06cc \u062c\u062f\u06cc\u062f \u0631\u0627 \u0628\u0647 \u0634\u06a9\u0644 \u0645\u062a\u0645\u0631\u06a9\u0632 \u0646\u0634\u0627\u0646 \u0645\u06cc \u062f\u0647\u062f \u062a\u0627 \u062a\u06cc\u0645 \u0634\u0645\u0627 \u0633\u0631\u06cc\u0639 \u062a\u0631 \u067e\u0627\u0633\u062e \u062f\u0647\u062f \u0648 \u0647\u06cc\u0686 \u0633\u0631\u0646\u062e\u06cc \u0627\u0632 \u062f\u0633\u062a \u0646\u0631\u0648\u062f.",
  dashboardHeroAlt: "\u0646\u0645\u0627\u06cc \u062f\u0627\u062f\u0647 \u0647\u0627\u06cc \u062b\u0628\u062a \u0634\u062f\u0647 \u0645\u0634\u062a\u0631\u06cc\u0627\u0646",
  updated: "\u0628\u0647 \u0631\u0648\u0632\u0631\u0633\u0627\u0646\u06cc",
  requestsRegisteredSuffix: "\u062f\u0631\u062e\u0648\u0627\u0633\u062a \u062b\u0628\u062a \u0634\u062f\u0647",
  latestStatus: "\u0622\u062e\u0631\u06cc\u0646 \u0648\u0636\u0639\u06cc\u062a",
  loading: "\u062f\u0631 \u062d\u0627\u0644 \u0628\u0627\u0631\u06af\u06cc\u0631\u06cc",
  synced: "\u0647\u0645\u06af\u0627\u0645 \u0628\u0627 \u067e\u0627\u06cc\u06af\u0627\u0647 \u062f\u0627\u062f\u0647",
  today: "\u0627\u0645\u0631\u0648\u0632",
  newEntriesSuffix: "\u062b\u0628\u062a \u062c\u062f\u06cc\u062f",
  savedRequests: "\u062f\u0631\u062e\u0648\u0627\u0633\u062a \u0647\u0627\u06cc \u062b\u0628\u062a \u0634\u062f\u0647",
  savedRequestsTitle: "\u0641\u0647\u0631\u0633\u062a \u06a9\u0627\u0645\u0644 \u0645\u062a\u0642\u0627\u0636\u06cc\u0627\u0646 \u0645\u0634\u0627\u0648\u0631\u0647",
  savedRequestsDescription: "\u0647\u0645\u0647 \u0627\u0637\u0644\u0627\u0639\u0627\u062a \u0641\u0631\u0645 \u0627\u0632 \u062c\u0645\u0644\u0647 \u0646\u0627\u0645\u060c \u0634\u0645\u0627\u0631\u0647 \u062a\u0645\u0627\u0633\u060c \u0627\u06cc\u0645\u06cc\u0644\u060c \u0646\u0648\u0639 \u062e\u062f\u0645\u062a \u0648 \u062a\u0648\u0636\u06cc\u062d\u0627\u062a \u067e\u0631\u0648\u0698\u0647 \u062f\u0631 \u0627\u06cc\u0646\u062c\u0627 \u0646\u0645\u0627\u06cc\u0634 \u062f\u0627\u062f\u0647 \u0645\u06cc \u0634\u0648\u062f.",
  loadingEntriesTitle: "\u062f\u0631 \u062d\u0627\u0644 \u062f\u0631\u06cc\u0627\u0641\u062a \u0627\u0637\u0644\u0627\u0639\u0627\u062a...",
  loadingEntriesDescription: "\u0686\u0646\u062f \u0644\u062d\u0638\u0647 \u0635\u0628\u0631 \u06a9\u0646\u06cc\u062f \u062a\u0627 \u062b\u0628\u062a \u0647\u0627\u06cc \u0645\u0634\u0627\u0648\u0631\u0647 \u0628\u0627\u0631\u06af\u0630\u0627\u0631\u06cc \u0634\u0648\u0646\u062f.",
  phone: "\u0634\u0645\u0627\u0631\u0647 \u062a\u0645\u0627\u0633",
  email: "\u0627\u06cc\u0645\u06cc\u0644",
  projectDetails: "\u062a\u0648\u0636\u06cc\u062d\u0627\u062a \u067e\u0631\u0648\u0698\u0647",
  emptyAlt: "\u0647\u0646\u0648\u0632 \u062b\u0628\u062a \u0645\u0634\u0627\u0648\u0631\u0647 \u0627\u06cc \u0648\u062c\u0648\u062f \u0646\u062f\u0627\u0631\u062f",
  emptyTitle: "\u0647\u0646\u0648\u0632 \u0647\u06cc\u0686 \u062f\u0631\u062e\u0648\u0627\u0633\u062a \u0645\u0634\u0627\u0648\u0631\u0647 \u0627\u06cc \u062b\u0628\u062a \u0646\u0634\u062f\u0647 \u0627\u0633\u062a",
  emptyDescription: "\u0628\u0647 \u0645\u062d\u0636 \u062b\u0628\u062a \u0641\u0631\u0645 \u0627\u0632 \u0633\u0645\u062a \u0633\u0627\u06cc\u062a\u060c \u0627\u0637\u0644\u0627\u0639\u0627\u062a \u0627\u06cc\u0646\u062c\u0627 \u0646\u0645\u0627\u06cc\u0634 \u062f\u0627\u062f\u0647 \u0645\u06cc \u0634\u0648\u062f.",
};


const normalizeAdminPassword = (value) => {
  const compact = String(value || "")
    .trim()
    .replace(/[\u200c\u200e\u200f\ufeff\s]+/g, "");

  return compact.replace(/[\u06f0-\u06f9\u0660-\u0669]/g, (char) => {
    const code = char.charCodeAt(0);
    if (code >= 0x06f0 && code <= 0x06f9) {
      return String(code - 0x06f0);
    }
    return String(code - 0x0660);
  });
};

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
    throw new Error(data?.error || TEXT.connectionError);
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

const serviceLabel = (value) => value || TEXT.notProvided;

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
    { label: TEXT.statsTotal, value: total },
    { label: TEXT.statsToday, value: today },
    { label: TEXT.statsServices, value: services },
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
    entriesState.value = { loading: false, type: "success", message: TEXT.entriesLoaded };
  } catch (error) {
    persistToken("");
    entries.value = [];
    entriesState.value = { loading: false, type: "error", message: error.message };
  }
};

const login = async () => {
  const normalizedPassword = normalizeAdminPassword(adminPassword.value);

  if (!normalizedPassword || loginState.value.loading) {
    return;
  }

  loginState.value = { loading: true, type: "", message: "" };

  try {
    const data = await requestJson("/api/admin/login", {
      method: "POST",
      body: JSON.stringify({ password: normalizedPassword }),
    });

    persistToken(data.token || "");
    adminPassword.value = "";
    loginState.value = { loading: false, type: "success", message: TEXT.loginSuccess };
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

const submitLogin = async () => {
  await login();
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
          <span class="brand-mark">K</span>
          <span>
            <strong>{{ TEXT.brandTitle }}</strong>
            <small>{{ TEXT.brandSubtitle }}</small>
          </span>
        </a>

        <div class="admin-header-actions">
          <a class="button button-secondary admin-back-link" href="/">{{ TEXT.backToSite }}</a>
          <button v-if="isAuthenticated" class="button button-primary" type="button" @click="logout">
            {{ TEXT.logout }}
          </button>
        </div>
      </div>
    </header>

    <main class="admin-main-shell">
      <section v-if="!isAuthenticated" class="admin-hero-section">
        <div class="hero-glow hero-glow-a"></div>
        <div class="hero-glow hero-glow-b"></div>

        <div class="container admin-grid admin-grid-compact">
          <div class="admin-hero-copy reveal visible">
            <div class="eyebrow">{{ TEXT.loginEyebrow }}</div>
            <h1>{{ TEXT.loginTitle }}</h1>
            <p class="hero-text admin-hero-text">
              {{ TEXT.loginDescription }}
            </p>

            <div class="admin-stats-grid">
              <article class="admin-stat-card">
                <span>{{ TEXT.accessStatus }}</span>
                <strong>{{ TEXT.secureAccess }}</strong>
              </article>
              <article class="admin-stat-card">
                <span>{{ TEXT.apiConnection }}</span>
                <strong>{{ API_BASE.replace(/^https?:\/\//, "") }}</strong>
              </article>
              <article class="admin-stat-card">
                <span>{{ TEXT.panelType }}</span>
                <strong>{{ TEXT.management }}</strong>
              </article>
            </div>
          </div>

<form class="admin-login-card reveal visible" @submit.prevent="submitLogin">
            <div class="section-tag">{{ TEXT.authTitle }}</div>
            <h2>{{ TEXT.loginCardTitle }}</h2>
            <p>{{ TEXT.loginCardDescription }}</p>

            <label class="admin-field" for="admin-password">
              <span>{{ TEXT.adminPassword }}</span>
              <input
                id="admin-password"
                v-model="adminPassword"
                type="password"
                name="password"
                autocomplete="current-password"
                :placeholder="TEXT.adminPasswordPlaceholder"
              />
            </label>

            <button class="button button-primary admin-login-button" type="submit" :disabled="loginState.loading">
              {{ loginState.loading ? TEXT.loggingIn : TEXT.loginButton }}
            </button>

            <p
              v-if="loginState.message"
              :class="[
                'site-form-note',
                loginState.type === 'success' ? 'site-form-note-success' : 'site-form-note-error',
              ]"
            >
              {{ loginState.message }}
            </p>

            <p
              v-if="entriesState.type === 'error' && entriesState.message"
              class="site-form-note site-form-note-error"
            >
              {{ entriesState.message }}
            </p>
          </form>
        </div>
      </section>

      <template v-else>
        <section class="admin-hero-section">
          <div class="hero-glow hero-glow-a"></div>
          <div class="hero-glow hero-glow-b"></div>

          <div class="container admin-grid admin-grid-compact">
            <div class="admin-hero-copy reveal visible">
              <div class="eyebrow">{{ TEXT.dashboardEyebrow }}</div>
              <h1>{{ TEXT.dashboardTitle }}</h1>
              <p class="hero-text admin-hero-text">
                {{ TEXT.dashboardDescription }}
              </p>

              <div class="admin-stats-grid">
                <article v-for="item in stats" :key="item.label" class="admin-stat-card">
                  <span>{{ item.label }}</span>
                  <strong>{{ item.value }}</strong>
                </article>
              </div>
            </div>

</div>
        </section>

        <section class="section admin-list-section">
          <div class="container">
            <div class="section-heading reveal visible admin-list-heading">
              <div class="section-tag">{{ TEXT.savedRequests }}</div>
              <h2>{{ TEXT.savedRequestsTitle }}</h2>
              <p>{{ TEXT.savedRequestsDescription }}</p>
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
              <strong>{{ TEXT.loadingEntriesTitle }}</strong>
              <p>{{ TEXT.loadingEntriesDescription }}</p>
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
                    <span>{{ TEXT.phone }}</span>
                    <strong>{{ entry.phone }}</strong>
                  </div>
                  <div>
                    <span>{{ TEXT.email }}</span>
                    <strong>{{ entry.email }}</strong>
                  </div>
                </div>

                <div class="admin-entry-details">
                  <span>{{ TEXT.projectDetails }}</span>
                  <p>{{ entry.project_details }}</p>
                </div>
              </article>
            </div>

            <div v-else class="admin-empty-state">
              <img :src="featureStrategyImage" :alt="TEXT.emptyAlt" />
              <strong>{{ TEXT.emptyTitle }}</strong>
              <p>{{ TEXT.emptyDescription }}</p>
            </div>
          </div>
        </section>
      </template>
    </main>
  </div>
</template>




