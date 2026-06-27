<script setup>
import { nextTick, onBeforeUnmount, onMounted, ref } from "vue";
import featureStrategyImage from "./assets/photos/feature-team.jpg";
import heroCollaborationImage from "./assets/photos/hero-team.jpg";
import projectCorporateImage from "./assets/photos/project-corporate.jpg";
import projectDashboardImage from "./assets/photos/project-dashboard.jpg";
import projectPortalImage from "./assets/photos/project-portal.jpg";

const isNavOpen = ref(false);
const navToggle = ref(null);
const siteNav = ref(null);
const currentYear = new Date().getFullYear();

const navLinks = [
  { href: "#services", label: "خدمات" },
  { href: "#projects", label: "پروژه‌ها" },
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
    title: "طراحی سایت شرکتی",
    text: "برای معرفی حرفه‌ای خدمات، ایجاد اعتماد، دریافت درخواست و ساخت یک حضور آنلاین منظم و دقیق.",
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
    text: "پس از تحویل هم کنار پروژه می‌مانیم تا اصلاحات، توسعه مرحله بعد و پایداری فنی با نظم ادامه پیدا کند.",
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
    text: "بعد از استقرار، اصلاحات نهایی، آموزش لازم و مسیر پشتیبانی پروژه مشخص و قابل اتکا می‌ماند.",
  },
];

const stats = [
  { title: "تحلیل", text: "شروع هر پروژه با شناخت دقیق نیاز" },
  { title: "طراحی", text: "رابط و ساختار متناسب با هویت برند" },
  { title: "توسعه", text: "پیاده‌سازی تمیز و قابل گسترش" },
  { title: "پشتیبانی", text: "همراهی بعد از تحویل و استقرار" },
];

const projects = [
  {
    image: projectCorporateImage,
    alt: "نمونه وب‌سایت شرکتی",
    category: "وب‌سایت شرکتی",
    title: "معرفی خدمات و دریافت درخواست",
    text: "مناسب برای شرکت‌هایی که می‌خواهند خدمات، نمونه‌کارها و مسیر تماس را با ساختاری حرفه‌ای و قابل اعتماد ارائه کنند.",
  },
  {
    image: projectDashboardImage,
    alt: "نمونه سامانه داخلی مدیریت",
    category: "سامانه داخلی",
    title: "مدیریت درخواست‌ها و گردش کار",
    text: "برای مجموعه‌هایی که ثبت اطلاعات، پیگیری وظایف یا هماهنگی بین واحدها را می‌خواهند از حالت دستی خارج کنند.",
  },
  {
    image: projectPortalImage,
    alt: "نمونه پنل مشتری و پیگیری",
    category: "پنل مشتری",
    title: "ثبت، پیگیری و ارتباط منظم",
    text: "مناسب برای کسب‌وکارهایی که می‌خواهند ارتباط با مشتری، دریافت درخواست و پاسخ‌گویی را ساختارمندتر کنند.",
  },
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
    text: "بعد از تحویل هم مسیر همکاری قطع نمی‌شود و برای اصلاح، توسعه بعدی و پشتیبانی، نقطه تماس روشن دارید.",
    title: "مرحله پشتیبانی",
    caption: "همراهی واقعی",
  },
];

const faqs = [
  {
    question: "چه نوع پروژه‌هایی را انجام می‌دهید؟",
    answer:
      "طراحی سایت شرکتی، توسعه نرم‌افزار اختصاصی، پنل‌های مدیریتی، سامانه‌های داخلی و بازطراحی محصولات دیجیتال از خدمات اصلی ما هستند.",
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
];

const footerQuickLinks = [
  { href: "#services", label: "خدمات" },
  { href: "#projects", label: "پروژه ها" },
  { href: "#about", label: "درباره ما" },
];

const footerMainLinks = [
  { href: "#consultation", label: "درخواست مشاوره" },
  { href: "#contact", label: "اطلاعات تماس" },
  { href: "#top", label: "بازگشت به بالا" },
];

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

onMounted(async () => {
  document.addEventListener("click", handleDocumentClick);
  document.addEventListener("keydown", handleDocumentKeydown);

  await nextTick();

  const revealItems = document.querySelectorAll(".reveal");

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
});

onBeforeUnmount(() => {
  document.removeEventListener("click", handleDocumentClick);
  document.removeEventListener("keydown", handleDocumentKeydown);

  if (revealObserver) {
    revealObserver.disconnect();
  }
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
            <small>طراحی سایت و سامانه‌های اختصاصی</small>
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
            <div class="eyebrow">طراحی سایت و توسعه نرم‌افزار برای کسب‌وکارهای جدی</div>
            <h1>راهکار دیجیتال را<br />بر اساس کار واقعی شرکت شما می‌سازیم</h1>
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
              <img
                :src="heroCollaborationImage"
                alt="جلسه کاری تیم توسعه نرم‌افزار"
              />
              <div class="visual-badge">
                <span>اجرای حرفه‌ای</span>
                <strong>تحلیل، توسعه و تحویل دقیق</strong>
              </div>
            </div>
            <div class="visual-mini visual-mini-top">
              <span>رویکرد</span>
              <strong>شفاف، مرحله‌به‌مرحله و قابل پیگیری</strong>
            </div>
          </div>
        </div>
      </section>

      <section class="logo-strip reveal">
        <div class="container logo-strip-inner">
          <span>همراه کسب‌وکارهایی که اجرا برایشان مهم‌تر از شعار است</span>
          <div class="logo-list">
            <span v-for="item in logoItems" :key="item">{{ item }}</span>
          </div>
        </div>
      </section>

      <section class="section about-section" id="about">
        <div class="container split-layout">
          <div class="section-copy reveal">
            <div class="section-tag">درباره ما</div>
            <h2 class="about-title-compact">یک تیم فنی در یزد برای ساخت خروجی‌هایی که فقط زیبا نباشند، بلکه واقعاً به کار بیایند</h2>
            <p>
              شرکت توسعه نرم‌افزار کریمی با تمرکز بر طراحی سایت، توسعه نرم‌افزار اختصاصی و بهبود فرایندهای دیجیتال شکل گرفته است. نگاه ما این است که هر پروژه باید هم از نظر ظاهری حرفه‌ای باشد و هم در عمل برای مجموعه شما مفید، قابل توسعه و قابل اتکا بماند.
            </p>
            <div class="value-grid">
              <article v-for="card in valueCards" :key="card.title" class="value-card">
                <strong>{{ card.title }}</strong>
                <p>{{ card.text }}</p>
              </article>
            </div>
          </div>

          <div class="feature-panel reveal">
            <div class="feature-image">
              <img
                :src="featureStrategyImage"
                alt="تیم نرم‌افزاری در حال بررسی پروژه"
                loading="lazy"
                decoding="async"
              />
            </div>
            <div class="feature-quote">
              <span>نگاه مدیریتی</span>
              <p>
                وقتی قرار است یک برند حرفه‌ای‌تر دیده شود، فقط ظاهر مهم نیست. ساختار محتوا، تجربه کاربر، نظم توسعه و پایداری خروجی هم باید در همان سطح جدی گرفته شوند.
              </p>
              <strong>تیم شرکت توسعه نرم‌افزار کریمی</strong>
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
              :class="['service-card', 'reveal', { 'service-card-accent': service.accent }]"
            >
              <span class="service-icon">{{ service.number }}</span>
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
          </div>
          <div class="timeline">
            <article v-for="step in processSteps" :key="step.number" class="timeline-item reveal">
              <strong>{{ step.number }}</strong>
              <h3>{{ step.title }}</h3>
              <p>{{ step.text }}</p>
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

      <section class="section projects-section" id="projects">
        <div class="container">
          <div class="section-heading reveal">
            <div class="section-tag">نمونه مسیرهای اجرا</div>
            <h2>نمونه خروجی‌هایی که برای کسب‌وکارهای مختلف قابل اجرا هستند</h2>
            <p>
              به‌جای ادعاهای کلی، ما روی خروجی‌هایی تمرکز می‌کنیم که مسئله مشخصی را حل کنند؛ چه معرفی حرفه‌ای خدمات باشد، چه مدیریت داخلی یا ساده‌تر کردن ارتباط با مشتری.
            </p>
          </div>
          <div class="project-grid">
            <article v-for="project in projects" :key="project.title" class="project-card reveal">
              <img :src="project.image" :alt="project.alt" loading="lazy" decoding="async" />
              <div class="project-copy">
                <span>{{ project.category }}</span>
                <h3>{{ project.title }}</h3>
                <p>{{ project.text }}</p>
              </div>
            </article>
          </div>
        </div>
      </section>

      <section class="section testimonial-section">
        <div class="container testimonial-shell">
          <div class="testimonial-copy reveal">
            <div class="section-tag">تجربه همکاری</div>
            <h2>در همکاری با ما، خروجی فقط یک فایل تحویلی نیست؛ یک مسیر روشن و حرفه‌ای است</h2>
            <p class="section-copy">
              خیلی از دغدغه‌ها قبل از شروع توسعه شکل می‌گیرند: ابهام در نیاز، بی‌نظمی در اجرا و نداشتن پشتیبانی بعد از تحویل. ما این بخش‌ها را از ابتدا جدی می‌گیریم.
            </p>
          </div>
          <div class="testimonial-grid">
            <article v-for="item in testimonialCards" :key="item.title" class="testimonial-card reveal">
              <p>{{ item.text }}</p>
              <strong>{{ item.title }}</strong>
              <span>{{ item.caption }}</span>
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
            <details v-for="item in faqs" :key="item.question" class="faq-item reveal">
              <summary>{{ item.question }}</summary>
              <p>{{ item.answer }}</p>
            </details>
          </div>
        </div>
      </section>

      <section class="section consultation-section" id="consultation">
        <div class="container consultation-shell">
          <div class="consultation-copy reveal">
            <div class="section-tag">درخواست مشاوره</div>
            <h2>اگر آماده‌اید حرفه‌ای‌تر دیده شوید، از همین‌جا شروع کنیم</h2>
            <p>
              این فرم برای شروع یک گفت‌وگوی دقیق و کاربردی طراحی شده است. اطلاعات اولیه پروژه را ثبت کنید تا تیم ما بر اساس نیاز واقعی شما، برای هماهنگی و بررسی ادامه مسیر تماس بگیرد.
            </p>
          </div>

          <form class="consultation-form reveal" id="consultationForm" @submit.prevent="submitConsultation">
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
                  <option>طراحی سایت شرکتی</option>
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
          <a class="brand footer-brand" href="#top">
            <span class="brand-mark">ک</span>
            <span>
              <strong>شرکت توسعه نرم‌افزار کریمی</strong>
              <small>طراحی سایت و نرم‌افزار در یزد</small>
            </span>
          </a>
          <p class="footer-text">
            ما برای کسب‌وکارهایی کار می‌کنیم که می‌خواهند خروجی دیجیتال‌شان فقط شیک نباشد، بلکه دقیق، کاربردی و قابل اتکا هم باشد. تمرکز ما روی طراحی تمیز، اجرای منظم و همراهی واقعی بعد از تحویل است.
          </p>
        </div>
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
          <p>یزد، کوچه حنا، ساختمان لاله، طبقه اول</p>
          <p>جلسات با هماهنگی قبلی انجام می‌شود</p>
          <p>شنبه تا پنج‌شنبه | 9 تا 18</p>
          <p>شروع ارتباط از طریق فرم درخواست مشاوره</p>
        </div>
      </div>
      <div class="container footer-bottom">
        <span>© {{ currentYear }} شرکت توسعه نرم‌افزار کریمی. تمامی حقوق محفوظ است.</span>
      </div>
    </footer>
  </div>
</template>


