---
name: Elite Enterprise Narrative
colors:
  surface: '#f7f9ff'
  surface-dim: '#cfdbea'
  surface-bright: '#f7f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#ecf4ff'
  surface-container: '#e3effe'
  surface-container-high: '#dde9f8'
  surface-container-highest: '#d8e4f2'
  on-surface: '#111d27'
  on-surface-variant: '#43474d'
  inverse-surface: '#26323c'
  inverse-on-surface: '#e7f2ff'
  outline: '#73777d'
  outline-variant: '#c3c7cd'
  surface-tint: '#4a6079'
  primary: '#193147'
  on-primary: '#ffffff'
  primary-container: '#30475e'
  on-primary-container: '#9db5d0'
  inverse-primary: '#b1c9e5'
  secondary: '#715b39'
  on-secondary: '#ffffff'
  secondary-container: '#fddeb3'
  on-secondary-container: '#77613f'
  tertiary: '#332f20'
  on-tertiary: '#ffffff'
  tertiary-container: '#4a4535'
  on-tertiary-container: '#bab29e'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#cfe5ff'
  primary-fixed-dim: '#b1c9e5'
  on-primary-fixed: '#021d32'
  on-primary-fixed-variant: '#324960'
  secondary-fixed: '#fddeb3'
  secondary-fixed-dim: '#dfc299'
  on-secondary-fixed: '#281901'
  on-secondary-fixed-variant: '#574324'
  tertiary-fixed: '#ebe2cc'
  tertiary-fixed-dim: '#cec6b1'
  on-tertiary-fixed: '#1f1b0e'
  on-tertiary-fixed-variant: '#4c4636'
  background: '#f7f9ff'
  on-background: '#111d27'
  surface-variant: '#d8e4f2'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 64px
    fontWeight: '700'
    lineHeight: 72px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.01em
  headline-xl:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '600'
    lineHeight: 44px
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
  section-gap: 120px
---

## Brand & Style

The design system is engineered for a top-tier global enterprise presence, balancing corporate authority with a high-end, luxury aesthetic. It draws inspiration from modern "premium-dark" and "refined-light" software giants like Stripe and Linear, but adapts the philosophy for a sophisticated Persian-English bilingual context.

The visual style is **Corporate Modernism**. It prioritizes precision, clarity, and trust through:
- **Generous Whitespace:** Promoting a sense of calm and high-value focus.
- **Micro-interactions:** Using subtle, purposeful transitions rather than flashy animations.
- **Material Integrity:** Surfaces feel intentional, utilizing slight translucency and refined depth to guide the user's eye.
- **Bilingual Harmony:** A strict adherence to baseline alignment and optical balancing between RTL (Persian) and LTR (English) scripts.

## Colors

The palette is rooted in a "New Heritage" aesthetic—combining a deep, trustworthy Navy with a prestigious, muted Gold.

- **Primary (Navy):** Used for core branding, primary buttons, and heavy headings to establish authority.
- **Accent (Gold):** Reserved for high-value highlights, active states, and premium calls to action. It should be used sparingly to maintain its "luxury" impact.
- **Background (Cream/Paper):** Instead of a pure digital white, the system uses a warm, off-white (#E7DEC8 tints) to evoke a physical, high-quality stationery feel.
- **Text (Steel Gray):** Used for body copy and secondary information to reduce visual strain and maintain a modern, softened contrast compared to pure black.

## Typography

The system utilizes a dual-font strategy. **Inter** handles all English and numerical data for a systematic, tech-forward look. For Persian text, **Vazirmatn** (or similar premium sans-serif Persian faces) must be used, ensuring that line heights are increased by 20% compared to English equivalents to accommodate the taller ascenders and descenders of the script.

- **Headlines:** Use tight letter-spacing and heavy weights (600-700) to create a "wall of authority."
- **Body:** Prioritize legibility with a relaxed line height (1.5x - 1.6x) and the Steel Gray color.
- **Numerical Data:** Always use Inter (or a tabular font) to ensure financial and statistical data aligns perfectly in dashboards.

## Layout & Spacing

This design system is built on a **refined 8-point grid**. All margins, paddings, and heights must be multiples of 8 (or 4 for micro-adjustments).

- **Grid Model:** 12-column fluid grid for desktop with 24px gutters.
- **Sectioning:** Large vertical gaps (120px+) between major landing page sections to reinforce the premium, "un-crowded" brand feel.
- **RTL Support:** The layout mirrors perfectly for Persian. Ensure that icons with directionality (arrows, progress bars) are flipped, while "universal" icons (search, settings) remain static.
- **Safe Zones:** Use a fixed max-width container (1280px) for content on large displays to prevent line lengths from becoming unreadable.

## Elevation & Depth

To maintain a "Stripe-like" clean aesthetic, elevation is achieved through **Tonal Layers** and **Ambient Shadows** rather than heavy borders.

- **Surface Levels:** 
  - Level 0: Background (#F9F7F2)
  - Level 1: Surface Cards (#FFFFFF) with 1px border (#E7DEC8)
  - Level 2: Floating elements (Modals, Nav) with Backdrop Blur.
- **Shadows:** Use extremely diffused shadows with a Navy tint. Example: `0px 10px 30px rgba(48, 71, 94, 0.05)`. Avoid pure black shadows.
- **Glassmorphism:** The Navbar uses a 20px background blur (System-ultra-thin) with a 60% opacity white fill to allow the content to scroll elegantly beneath it.

## Shapes

The shape language is **Soft Modernist**. 

- **Corners:** Use a consistent `0.25rem` (4px) for small components like inputs and small buttons, and `0.5rem` (8px) for cards. This slight rounding feels more professional and precise than "bubbly" pill shapes.
- **Containers:** Large service cards and hero sections should stick to `12px` or `16px` max to maintain a structured, architectural feel.

## Components

### Buttons
- **Primary:** Navy background, white text, 8px padding-x, 16px padding-y. Subtle hover state: 5% lighten.
- **Secondary:** Transparent with a 1px Navy or Gold border.
- **Tertiary:** Text-only with a 2px bottom border on hover (Gold).

### Navigation
- **The Global Nav:** High-z-index, backdrop-blur, 72px height. Links use `label-md` typography. Include a language switcher (EN/FA) with a subtle icon.

### Service Cards
- White surface, subtle 1px Cream border. On hover: Translate -4px Y-axis and deepen the ambient shadow. The icon within the card should use the Gold accent.

### Statistics Displays
- Large Display-size numbers in Navy. Below the number, a Gold horizontal divider (24px wide, 2px thick), followed by a Steel Gray label.

### Form Inputs
- 1px Steel Gray border (20% opacity). On focus, the border transitions to Gold with a 2px outer glow. Labels are always `label-md` and positioned above the field for RTL/LTR consistency.