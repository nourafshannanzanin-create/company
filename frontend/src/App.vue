<script setup>
import { nextTick, onBeforeUnmount, onMounted, ref } from "vue";

const isNavOpen = ref(false);
const navToggle = ref(null);
const siteNav = ref(null);
const currentYear = new Date().getFullYear();

const navLinks = [
  { href: "#services", label: "خدمات" },
  { href: "#customers", label: "مشتریان" },
  { href: "#about", label: "درباره ما" },
  { href: "#contact", label: "تماس" },
];

const logoItems = ["شرکتی", "تولیدی", "خدماتی", "فروش", "آموزشی"];

const valueCards = [
  {
    title: "روش کار",
    text: "پروژه با گفت‌وگوی دقیق شروع می‌شود، نه با حدس. نیاز شما شفاف می‌شود و بعد وارد طراحی و توسعه می‌شویم.",
  },
  {
    title: "نگاه ما",
    text: "هر کسب‌وکار مسیر خودش را دارد؛ برای همین راه‌حل‌ها آماده و کپی نیستند و بر اساس شرایط واقعی شما تنظیم می‌شوند.",
  },
  {
    title: "تعهد ما",
    text: "تحویل تمیز، ارتباط منظم، مستندسازی روشن و پشتیبانی بعد از اجرا بخشی از کار است، نه یک مورد جانبی.",
  },
];

const serviceCards = [
  {
    number: "01",
    title: "طراحی سایت و اپلیکیشن",
    text: "برای معرفی حرفه‌ای خدمات، ایجاد اعتماد، دریافت درخواست و ساخت یک حضور آنلاین منظم و دقیق در وب و موبایل.",
  },
  {
    number: "02",
    title: "توسعه نرم‌افزار اختصاصی",
    text: "برای زمانی که ابزار آماده جواب‌گو نیست و مجموعه شما به راهکاری متناسب با فرایند واقعی خود نیاز دارد.",
  },
  {
    number: "03",
    title: "سامانه‌های داخلی و پنل مدیریت",
    text: "طراحی پنل‌ها و ابزارهایی که پیگیری، ثبت اطلاعات و هماهنگی داخلی را برای تیم شما ساده‌تر می‌کنند.",
  },
  {
    number: "04",
    title: "طراحی تجربه کاربری",
    text: "چیدمان، مسیر حرکت کاربر و ساختار محتوا طوری تنظیم می‌شود که استفاده از محصول برای مخاطب راحت و روشن باشد.",
  },
  {
    number: "05",
    title: "بهبود و بازطراحی محصولات فعلی",
    text: "اگر وب‌سایت یا نرم‌افزار فعلی شما ظاهر قدیمی، ساختار ضعیف یا تجربه استفاده آشفته دارد، بازطراحی اصولی انجام می‌دهیم.",
  },
  {
    number: "06",
    title: "پشتیبانی و توسعه بعد از اجرا",
    text: "پس از تحویل هم کنار پروژه می‌مانیم؛ سه ماه پشتیبانی رایگان برای اصلاحات اولیه، هماهنگی‌های مهم و تثبیت خروجی در شروع مسیر همکاری در نظر گرفته می‌شود.",
    accent: true,
  },
];

const processSteps = [
  {
    number: "01",
    title: "بررسی نیاز",
    text: "نیاز، هدف، مخاطب و محدودیت‌های پروژه بررسی می‌شود تا شروع کار بر پایه فهم درست باشد.",
  },
  {
    number: "02",
    title: "طراحی مسیر اجرا",
    text: "ساختار صفحات، بخش‌های اصلی، روند کاربر و محدوده توسعه مشخص می‌شود تا پروژه مبهم پیش نرود.",
  },
  {
    number: "03",
    title: "توسعه و پیاده‌سازی",
    text: "طراحی و کدنویسی بر اساس همان نقشه جلو می‌رود و خروجی مرحله‌به‌مرحله قابل بررسی است.",
  },
  {
    number: "04",
    title: "تحویل و پشتیبانی",
    text: "بعد از استقرار، اصلاحات نهایی، آموزش لازم و سه ماه پشتیبانی رایگان در کنار مسیر پشتیبانی بعدی، شفاف و قابل اتکا تعریف می‌شود.",
  },
];

const stats = [
  { title: "تحلیل", text: "شروع هر پروژه با شناخت دقیق نیاز" },
  { title: "طراحی", text: "رابط و ساختار متناسب با هویت برند" },
  { title: "توسعه", text: "پیاده‌سازی تمیز و قابل گسترش" },
  { title: "پشتیبانی", text: "همراهی بعد از تحویل و استقرار" },
];

const testimonialCards = [
  {
    text: "قبل از شروع اجرا، نیاز پروژه به زبان روشن جمع‌بندی می‌شود تا چیزی مبهم یا دوپهلو باقی نماند.",
    title: "مرحله تحلیل",
    caption: "شروع شفاف",
  },
  {
    text: "در طول توسعه، تصمیم‌ها بر اساس منطق پروژه گرفته می‌شوند؛ نه بر اساس شتاب یا ظاهر مقطعی.",
    title: "مرحله اجرا",
    caption: "تصمیم‌گیری دقیق",
  },
  {
    text: "خروجی نهایی باید از نظر ظاهری منظم، از نظر فنی پایدار و از نظر استفاده برای مخاطب قابل فهم باشد.",
    title: "مرحله تحویل",
    caption: "کیفیت قابل اتکا",
  },
  {
    text: "بعد از تحویل هم مسیر همکاری قطع نمی‌شود و در سه ماه ابتدایی، پشتیبانی رایگان برای ریزه‌کاری‌ها، هماهنگی‌ها و اطمینان از شروع قدرتمند پروژه همراه شماست.",
    title: "مرحله پشتیبانی",
    caption: "همراهی واقعی",
  },
];

const customerCards = [
  {
    label: "جای نمونه مشتری",
    title: "پروژه برند اول شما",
    text: "این فضا برای قراردادن لوگو، تصویر، توضیح کوتاه و نتیجه همکاری با یکی از مشتریان شما آماده شده است.",
  },
  {
    label: "قابل شخصی سازی",
    title: "داستان موفقیت یک همکاری",
    text: "می توانید در این کارت نوع خدمت، حوزه فعالیت مشتری و خلاصه ای از دستاورد پروژه را قرار دهید تا اعتبار برند بهتر دیده شود.",
  },
  {
    label: "ویترین نمونه ها",
    title: "نمایش حرفه ای نمونه کارها",
    text: "این بخش طوری طراحی شده که بعدا نمونه های واقعی، لوگوها یا تصاویر قبل و بعد را خیلی راحت جایگزین کنید.",
  },
];

const faqs = [
  {
    question: "چه نوع پروژه‌هایی را انجام می‌دهید؟",
    answer:
      "طراحی سایت و اپلیکیشن، توسعه نرم‌افزار اختصاصی، پنل‌های مدیریتی، سامانه‌های داخلی و بازطراحی محصولات دیجیتال از خدمات اصلی ما هستند.",
  },
  {
    question: "پروژه از کجا شروع می‌شود؟",
    answer:
      "ابتدا نیاز شما بررسی می‌شود، بعد محدوده کار، مسیر اجرا و مدل همکاری مشخص می‌گردد تا پروژه از همان ابتدا شفاف پیش برود.",
  },
  {
    question: "آیا کارها کاملاً سفارشی اجرا می‌شوند؟",
    answer:
      "بله. خروجی بر اساس نیاز، نوع خدمات، مخاطب و ساختار کاری مجموعه شما طراحی و توسعه داده می‌شود، نه از روی قالب آماده و تکراری.",
  },
  {
    question: "پشتیبانی سه ماهه رایگان شامل چه چیزهایی است؟",
    answer:
      "بعد از تحویل، تا سه ماه برای اصلاحات اولیه، رفع ایرادهای احتمالی، هماهنگی‌های اجرایی و پاسخ‌گویی سریع کنار شما هستیم تا پروژه با خیال راحت وارد فاز استفاده واقعی شود.",
  },
];

const footerQuickLinks = [
  { href: "#services", label: "خدمات" },
  { href: "#customers", label: "مشتریان" },
  { href: "#about", label: "درباره ما" },
];

const footerMainLinks = [
  { href: "#consultation", label: "درخواست مشاوره" },
  { href: "#contact", label: "اطلاعات تماس" },
  { href: "#top", label: "بازگشت به بالا" },
];

const contactChannels = [
  { href: "https://wa.me/989000000000", label: "واتساپ" },
  { href: "https://t.me/your_username", label: "تلگرام" },
  { href: "https://ble.ir/your_channel", label: "بله" },
];

const contactLicenseImage = "/contact-license.jpg";
const contactLicenseImageSecondary = "/photo_2026-07-01_15-22-38.jpg";
const heroShowreelVideo = "/web-design.mp4";
const heroTextImage = "/one_step_online_success_correct_TA_transparent.png";

const API_BASE = (import.meta.env.VITE_API_BASE || "http://127.0.0.1:8000").replace(/\/$/, "");

const consultationForm = ref({
  fullName: "",
  phone: "",
  email: "",
  service: "",
  projectDetails: "",
});

const consultationState = ref({
  loading: false,
  type: "",
  message: "",
});

const resetConsultationForm = () => {
  consultationForm.value = {
    fullName: "",
    phone: "",
    email: "",
    service: "",
    projectDetails: "",
  };
};

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

const submitConsultation = async () => {
  if (consultationState.value.loading) {
    return;
  }

  consultationState.value = {
    loading: true,
    type: "",
    message: "",
  };

  try {
    const response = await requestJson("/api/consultations", {
      method: "POST",
      body: JSON.stringify({
        full_name: consultationForm.value.fullName,
        phone: consultationForm.value.phone,
        email: consultationForm.value.email,
        service: consultationForm.value.service,
        project_details: consultationForm.value.projectDetails,
      }),
    });

    consultationState.value = {
      loading: false,
      type: "success",
      message: response.message || "درخواست شما با موفقیت ثبت شد.",
    };
    resetConsultationForm();
  } catch (error) {
    consultationState.value = {
      loading: false,
      type: "error",
      message: error.message,
    };
  }
};
const toggleNav = () => {
  isNavOpen.value = !isNavOpen.value;
};

const closeNav = () => {
  isNavOpen.value = false;
};

const handleDocumentClick = (event) => {
  const navElement = siteNav.value;
  const toggleElement = navToggle.value;
  const target = event.target;

  if (!isNavOpen.value || !navElement || !toggleElement || !(target instanceof Node)) {
    return;
  }

  if (!navElement.contains(target) && !toggleElement.contains(target)) {
    closeNav();
  }
};

const handleDocumentKeydown = (event) => {
  if (event.key === "Escape") {
    closeNav();
  }
};

let revealObserver;
let scrollMotionObserver;
let motionMediaQuery;
let scrollMotionFrame = 0;
let scrollMotionCards = [];
let visibleScrollMotionCards = new Set();
let isScrollMotionEnabled = false;

const resetScrollMotionCard = (card) => {
  card.style.setProperty("--scroll-translate-y", "0px");
  card.style.setProperty("--scroll-rotate", "0deg");
  card.style.setProperty("--scroll-scale", "1");
  card.style.setProperty("--scroll-glow", "1");
};

const shouldEnableScrollMotion = () =>
  !window.matchMedia("(prefers-reduced-motion: reduce), (max-width: 1100px), (pointer: coarse)").matches;

const updateScrollMotionCards = () => {
  if (!isScrollMotionEnabled || visibleScrollMotionCards.size === 0) {
    return;
  }

  visibleScrollMotionCards.forEach((card) => {
    const rect = card.getBoundingClientRect();
    const viewportHeight = window.innerHeight || 1;
    const center = rect.top + rect.height / 2;
    const normalized = (center - viewportHeight / 2) / viewportHeight;
    const depth = Number(card.getAttribute("data-depth") || 1);
    const clamped = Math.max(-1, Math.min(1, normalized));
    const translateY = clamped * 16 * Math.min(depth, 1.2);
    const rotate = clamped * 1.2 * Math.min(depth, 1.1);
    const scale = 1 - Math.abs(clamped) * 0.012 * Math.min(depth, 1.2);
    const glow = 1.02 - Math.min(Math.abs(clamped), 1) * 0.08;

    card.style.setProperty("--scroll-translate-y", `${translateY.toFixed(2)}px`);
    card.style.setProperty("--scroll-rotate", `${rotate.toFixed(2)}deg`);
    card.style.setProperty("--scroll-scale", `${scale.toFixed(3)}`);
    card.style.setProperty("--scroll-glow", `${glow.toFixed(3)}`);
  });
};

const teardownScrollMotion = () => {
  window.removeEventListener("scroll", queueScrollMotionUpdate);
  window.removeEventListener("resize", queueScrollMotionUpdate);

  if (scrollMotionObserver) {
    scrollMotionObserver.disconnect();
    scrollMotionObserver = undefined;
  }

  if (scrollMotionFrame) {
    window.cancelAnimationFrame(scrollMotionFrame);
    scrollMotionFrame = 0;
  }

  visibleScrollMotionCards.forEach((card) => resetScrollMotionCard(card));
  visibleScrollMotionCards.clear();
};

const queueScrollMotionUpdate = () => {
  if (!isScrollMotionEnabled) {
    return;
  }

  if (scrollMotionFrame) {
    return;
  }

  scrollMotionFrame = window.requestAnimationFrame(() => {
    updateScrollMotionCards();
    scrollMotionFrame = 0;
  });
};

const setupScrollMotion = () => {
  teardownScrollMotion();
  isScrollMotionEnabled = shouldEnableScrollMotion();
  document.documentElement.classList.toggle("motion-lite", !isScrollMotionEnabled);

  if (!isScrollMotionEnabled || scrollMotionCards.length === 0) {
    scrollMotionCards.forEach((card) => resetScrollMotionCard(card));
    return;
  }

  scrollMotionObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          visibleScrollMotionCards.add(entry.target);
        } else {
          visibleScrollMotionCards.delete(entry.target);
          resetScrollMotionCard(entry.target);
        }
      });

      queueScrollMotionUpdate();
    },
    {
      rootMargin: "220px 0px",
      threshold: 0,
    }
  );

  scrollMotionCards.forEach((card) => scrollMotionObserver.observe(card));
  window.addEventListener("scroll", queueScrollMotionUpdate, { passive: true });
  window.addEventListener("resize", queueScrollMotionUpdate);
  queueScrollMotionUpdate();
};

onMounted(async () => {
  document.addEventListener("click", handleDocumentClick);
  document.addEventListener("keydown", handleDocumentKeydown);

  await nextTick();

  const revealItems = document.querySelectorAll(".reveal");
  scrollMotionCards = Array.from(document.querySelectorAll(".scroll-motion-card"));

  if ("IntersectionObserver" in window && revealItems.length > 0) {
    revealObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            revealObserver.unobserve(entry.target);
          }
        });
      },
      {
        threshold: 0.12,
        rootMargin: "0px 0px -40px 0px",
      }
    );

    revealItems.forEach((item) => revealObserver.observe(item));
  } else {
    revealItems.forEach((item) => item.classList.add("visible"));
  }

  motionMediaQuery = window.matchMedia("(prefers-reduced-motion: reduce), (max-width: 1100px), (pointer: coarse)");
  if (typeof motionMediaQuery.addEventListener === "function") {
    motionMediaQuery.addEventListener("change", setupScrollMotion);
  } else if (typeof motionMediaQuery.addListener === "function") {
    motionMediaQuery.addListener(setupScrollMotion);
  }

  setupScrollMotion();
});

onBeforeUnmount(() => {
  document.removeEventListener("click", handleDocumentClick);
  document.removeEventListener("keydown", handleDocumentKeydown);

  if (revealObserver) {
    revealObserver.disconnect();
  }

  if (motionMediaQuery) {
    if (typeof motionMediaQuery.removeEventListener === "function") {
      motionMediaQuery.removeEventListener("change", setupScrollMotion);
    } else if (typeof motionMediaQuery.removeListener === "function") {
      motionMediaQuery.removeListener(setupScrollMotion);
    }
  }

  teardownScrollMotion();
  scrollMotionCards = [];
  motionMediaQuery = undefined;
});
</script>

<template>
  <div class="page-shell">
    <header class="site-header" id="top">
      <div class="container nav-shell">
        <a class="brand" href="#top">
          <span class="brand-mark">ک</span>
          <span>
            <strong>شرکت توسعه نرم‌افزار کریمی</strong>
            <small>طراحی سایت و اپلیکیشن و سامانه‌های اختصاصی</small>
          </span>
        </a>

        <button
          ref="navToggle"
          class="nav-toggle"
          aria-label="باز کردن منو"
          :aria-expanded="String(isNavOpen)"
          @click="toggleNav"
        >
          <span></span>
          <span></span>
          <span></span>
        </button>

        <nav ref="siteNav" :class="['site-nav', { 'is-open': isNavOpen }]">
          <a v-for="link in navLinks" :key="link.href" :href="link.href" @click="closeNav">{{ link.label }}</a>
        </nav>

        <a class="button button-primary nav-cta" href="#consultation">درخواست مشاوره</a>
      </div>
    </header>

    <main>
      <section class="hero-section">
        <div class="hero-glow hero-glow-a"></div>
        <div class="hero-glow hero-glow-b"></div>
        <div class="container hero-grid">
          <div class="hero-copy reveal">
            <img :src="heroTextImage" alt="متن اصلی هیروسکشن" class="hero-title-image" loading="eager" decoding="async" />
            <p class="hero-text">
              در شرکت توسعه نرم‌افزار کریمی، پروژه فقط به ظاهر خوب ختم نمی‌شود. ما وب‌سایت و نرم‌افزار را طوری طراحی و اجرا می‌کنیم که با روند واقعی کار شما هماهنگ باشد، کار را ساده‌تر کند و تصویر حرفه‌ای‌تری از برندتان بسازد.
            </p>
            <p class="hero-text">
              از تحلیل نیاز تا طراحی رابط، توسعه، استقرار و پشتیبانی، مسیر همکاری روشن است. اگر دنبال خروجی تمیز، اجرای منظم و همراهی واقعی هستید، اینجا دقیقاً برای همین کار ساخته شده است.
            </p>

            <div class="hero-actions">
              <a class="button button-gold" href="#consultation">شروع گفت‌وگو برای پروژه</a>
              <a class="button button-secondary" href="#services">مشاهده خدمات</a>
            </div>
          </div>

          <div class="hero-visual reveal">
            <div class="visual-card visual-main">
              <video autoplay muted loop playsinline preload="metadata">
                <source :src="heroShowreelVideo" type="video/mp4" />
              </video>
            </div>
          </div>
        </div>
      </section>

      <section class="logo-strip reveal">
        <div class="container logo-strip-inner">
          <span class="signature-slogan">
            <span class="signature-slogan-text">همراه کسب‌وکارهایی که اجرا برایشان مهم‌تر از شعار است</span>
          </span>
          <div class="logo-list">
            <span v-for="item in logoItems" :key="item">{{ item }}</span>
          </div>
        </div>
      </section>

      <section class="section about-section" id="about">
        <div class="container">
          <div class="section-copy reveal">
            <div class="section-tag">درباره ما</div>
            <h2 class="about-title-compact">یک تیم فنی در یزد برای ساخت خروجی‌هایی که فقط زیبا نباشند، بلکه واقعاً به کار بیایند</h2>
            <p>
              شرکت توسعه نرم‌افزار کریمی با تمرکز بر طراحی سایت و اپلیکیشن، توسعه نرم‌افزار اختصاصی و بهبود فرایندهای دیجیتال شکل گرفته است. نگاه ما این است که هر پروژه باید هم از نظر ظاهری حرفه‌ای باشد و هم در عمل برای مجموعه شما مفید، قابل توسعه و قابل اتکا بماند.
            </p>
            <div class="value-grid">
              <article
                v-for="(card, index) in valueCards"
                :key="card.title"
                class="value-card reveal throw-card scroll-motion-card"
                :style="{ '--card-delay': `${index * 120}ms` }"
                :data-depth="1 + index * 0.08"
              >
                <strong>{{ card.title }}</strong>
                <p>{{ card.text }}</p>
              </article>
            </div>
          </div>

        </div>
      </section>

      <section class="section services-section" id="services">
        <div class="container">
          <div class="section-heading reveal">
            <div class="section-tag">خدمات تخصصی</div>
            <h2 class="services-title-compact">خدماتی که برای معرفی، مدیریت و توسعه حرفه‌ای کسب‌وکار شما طراحی شده‌اند</h2>
            <p>
              اگر به یک وب‌سایت شرکتی خوش‌ساخت، نرم‌افزار اختصاصی، سامانه داخلی یا بهینه‌سازی مسیرهای کاری نیاز دارید، خدمات ما طوری چیده شده‌اند که از مرحله تحلیل تا اجرا و پشتیبانی، پروژه شما یک مسیر روشن و قابل مدیریت داشته باشد.
            </p>
          </div>

          <div class="services-grid">
            <article
              v-for="service in serviceCards"
              :key="service.number"
              :class="['service-card', 'reveal', 'scroll-motion-card', { 'service-card-accent': service.accent }]"
              :data-depth="service.accent ? 1.25 : 1.05"
            >
              <span class="service-icon">{{ service.number }}</span>
              <span v-if="service.accent" class="service-chip">پشتیبانی VIP</span>
              <h3>{{ service.title }}</h3>
              <p>{{ service.text }}</p>
            </article>
          </div>
        </div>
      </section>

      <section class="section process-section">
        <div class="container">
          <div class="section-heading reveal">
            <div class="section-tag">فرایند همکاری</div>
            <h2>مسیر اجرای پروژه روشن، حرفه‌ای و قابل پیگیری است</h2>
            <p>
              هر مرحله طوری طراحی می‌شود که هم خروجی زیبا باشد، هم بعد از تحویل با سه ماه پشتیبانی رایگان، شروع استفاده برای تیم شما نرم و مطمئن پیش برود.
            </p>
          </div>
          <div class="timeline">
            <article
              v-for="(step, index) in processSteps"
              :key="step.number"
              class="timeline-item reveal scroll-motion-card"
              :data-depth="1 + index * 0.06"
            >
              <strong>{{ step.number }}</strong>
              <h3>{{ step.title }}</h3>
              <p>{{ step.text }}</p>
            </article>
          </div>
        </div>
      </section>

      <section class="section customers-section" id="customers">
        <div class="container">
          <div class="section-heading reveal">
            <div class="section-tag">مشتریان</div>
            <h2>جایی برای نمایش نمونه همکاری ها و برندهایی که به شما اعتماد کرده اند</h2>
            <p>
              این بخش آماده شده تا بعدا بتوانید نمونه های واقعی، لوگوی مشتریان، تصویر پروژه و خلاصه دستاورد هر همکاری را داخل آن قرار دهید و یک ویترین حرفه ای بسازید.
            </p>
          </div>
          <div class="customer-grid">
            <article
              v-for="(customer, index) in customerCards"
              :key="customer.title"
              class="customer-card reveal throw-card scroll-motion-card"
              :style="{ '--card-delay': `${index * 130}ms` }"
              :data-depth="1.08 + index * 0.08"
            >
              <span>{{ customer.label }}</span>
              <h3>{{ customer.title }}</h3>
              <p>{{ customer.text }}</p>
            </article>
          </div>
        </div>
      </section>

      <section class="stats-band reveal">
        <div class="container stats-grid">
          <div v-for="item in stats" :key="item.title">
            <strong>{{ item.title }}</strong>
            <span>{{ item.text }}</span>
          </div>
        </div>
      </section>

      <section class="section testimonial-section">
        <div class="container testimonial-shell">
          <div class="testimonial-grid">
            <article
              v-for="(item, index) in testimonialCards"
              :key="item.title"
              class="testimonial-card reveal slide-card scroll-motion-card"
              :style="{ '--card-delay': `${index * 100}ms` }"
              :data-slide-index="index"
              :data-depth="1.05 + index * 0.05"
            >
              <span class="testimonial-card-caption">{{ item.caption }}</span>
              <strong>{{ item.title }}</strong>
              <p>{{ item.text }}</p>
            </article>
          </div>
        </div>
      </section>

      <section class="section faq-section">
        <div class="container">
          <div class="section-heading reveal">
            <div class="section-tag">سوالات متداول</div>
            <h2>پاسخ‌های روشن برای شروع یک همکاری حرفه‌ای</h2>
          </div>
          <div class="faq-list">
            <details
              v-for="(item, index) in faqs"
              :key="item.question"
              class="faq-item reveal scroll-motion-card"
              :data-depth="1 + index * 0.04"
            >
              <summary>{{ item.question }}</summary>
              <p>{{ item.answer }}</p>
            </details>
          </div>
        </div>
      </section>

      <section class="section consultation-section" id="consultation">
        <div class="container consultation-shell">
          <form class="consultation-form reveal scroll-motion-card" data-depth="1.06" id="consultationForm" @submit.prevent="submitConsultation">
            <div class="section-tag">درخواست مشاوره</div>
            <h2>برای شروع همکاری، اطلاعات اولیه را ثبت کنید</h2>
            <p class="consultation-intro">
              فرم را تکمیل کنید تا برای هماهنگی، بررسی پروژه و ارائه مسیر همکاری با شما تماس بگیریم.
            </p>
            <div class="form-grid">
              <label>
                <span>نام و نام خانوادگی</span>
                <input
                  v-model="consultationForm.fullName"
                  type="text"
                  name="fullName"
                  placeholder="نام شما"
                  autocomplete="name"
                />
              </label>
              <label>
                <span>شماره تماس</span>
                <input
                  v-model="consultationForm.phone"
                  type="tel"
                  name="phone"
                  placeholder="09xxxxxxxxx"
                  autocomplete="tel"
                />
              </label>
              <label>
                <span>ایمیل</span>
                <input
                  v-model="consultationForm.email"
                  type="email"
                  name="email"
                  placeholder="ایمیل سازمانی شما"
                  autocomplete="email"
                />
              </label>
              <label>
                <span>نوع خدمت</span>
                <select v-model="consultationForm.service" name="service">
                  <option value="" disabled>انتخاب کنید</option>
                  <option>طراحی سایت و اپلیکیشن</option>
                  <option>توسعه نرم افزار اختصاصی</option>
                  <option>سامانه داخلی و پنل مدیریت</option>
                  <option>بازطراحی و بهبود محصول فعلی</option>
                </select>
              </label>
              <label class="field-wide">
                <span>توضیحات پروژه</span>
                <textarea
                  v-model="consultationForm.projectDetails"
                  rows="5"
                  name="projectDetails"
                  placeholder="در مورد نیاز، هدف، وضعیت فعلی و مقیاس پروژه بنویسید"
                ></textarea>
              </label>
            </div>
            <button class="button button-primary" type="submit" :disabled="consultationState.loading">
              {{ consultationState.loading ? "در حال ثبت درخواست..." : "ثبت درخواست" }}
            </button>
            <p
              v-if="consultationState.message"
              :class="[
                'site-form-note',
                consultationState.type === 'success' ? 'site-form-note-success' : 'site-form-note-error',
              ]"
            >
              {{ consultationState.message }}
            </p>
          </form>
        </div>
      </section>
    </main>

    <footer class="site-footer" id="contact">
      <div class="container footer-grid">
        <div>
          <h3>لینک‌های سریع</h3>
          <a v-for="link in footerQuickLinks" :key="link.href" :href="link.href">{{ link.label }}</a>
        </div>
        <div>
          <h3>بخش‌های مهم</h3>
          <a v-for="link in footerMainLinks" :key="link.href" :href="link.href">{{ link.label }}</a>
        </div>
        <div>
          <h3>اطلاعات تماس</h3>
          <p>آدرس: یزد، بخش مرکزی، شهر یزد، ملا فرج الله، کوچه ۵، کوچه ۶، پلاک ۱۲۶۴، مجتمع لاله، طبقه همکف</p>
          <p>ساعت کاری: شنبه تا پنج‌شنبه، از ساعت ۹:۰۰ صبح تا ۲۱:۰۰ شب</p>
          <div class="contact-channels">
            <span>پیام‌رسان‌ها</span>
            <a
              v-for="channel in contactChannels"
              :key="channel.label"
              :href="channel.href"
              target="_blank"
              rel="noopener noreferrer"
            >
              {{ channel.label }}
            </a>
          </div>
          <div class="footer-license-group">
            <a :href="contactLicenseImage" class="footer-license-link" target="_blank" rel="noopener noreferrer">
              <img :src="contactLicenseImage" alt="مجوز فعالیت شرکت" class="footer-license" loading="lazy" decoding="async" />
            </a>
            <a :href="contactLicenseImageSecondary" class="footer-license-link" target="_blank" rel="noopener noreferrer">
              <img :src="contactLicenseImageSecondary" alt="مجوز دوم فعالیت شرکت" class="footer-license" loading="lazy" decoding="async" />
            </a>
          </div>
        </div>
      </div>
      <div class="container footer-bottom">
        <span>© {{ currentYear }} شرکت توسعه نرم‌افزار کریمی. تمامی حقوق محفوظ است.</span>
      </div>
    </footer>
  </div>
</template>






