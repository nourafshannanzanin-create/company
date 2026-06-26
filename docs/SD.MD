# Enterprise Design System

## Corporate Static Website Design System

### Version 1.0

---

# 1. Design Philosophy

## Brand Positioning

این طراحی برای یک شرکت حرفه‌ای، معتبر و سازمانی طراحی شده است.

هدف:

* ایجاد اعتماد
* نمایش اعتبار
* افزایش نرخ تبدیل
* ایجاد حس Premium
* نمایش قدرت برند

---

## Brand Attributes

| Attribute    | Value |
| ------------ | ----- |
| Professional | 10/10 |
| Corporate    | 10/10 |
| Luxury       | 8/10  |
| Modern       | 9/10  |
| Trustworthy  | 10/10 |
| Elegant      | 9/10  |

---

# 2. Color System

## Primary Palette

```css
:root {

--primary-900:#30475E;
--primary-800:#3F5B74;
--primary-700:#4F6A82;

--secondary-500:#7E8A97;
--secondary-400:#99A4AF;
--secondary-300:#B6BEC6;

--accent-500:#CBAF87;
--accent-400:#D8C2A1;
--accent-300:#E4D4BB;

--neutral-100:#FFFFFF;
--neutral-200:#F8F5EF;
--neutral-300:#E7DEC8;

}
```

---

## Color Usage

### Primary Navy

```css
#30475E
```

استفاده در:

* Navbar
* Footer
* Primary Buttons
* Headings
* Statistics Section

---

### Accent Gold

```css
#CBAF87
```

استفاده در:

* CTA
* Hover
* Links
* Highlights
* Icons

---

### Cream

```css
#E7DEC8
```

استفاده در:

* Background
* Cards
* Soft Sections

---

### Steel Gray

```css
#7E8A97
```

استفاده در:

* Body Text
* Borders
* Secondary Elements

---

# 3. Typography System

## Font Family

### Persian

```css
font-family:
"Vazirmatn",
sans-serif;
```

### English

```css
font-family:
"Inter",
sans-serif;
```

---

# Type Scale

## Display Large

```css
font-size:80px;
font-weight:800;
line-height:1.05;
```

Hero Titles

---

## Display Medium

```css
font-size:64px;
font-weight:800;
```

Landing Sections

---

## Heading 1

```css
font-size:48px;
font-weight:700;
```

---

## Heading 2

```css
font-size:36px;
font-weight:700;
```

---

## Heading 3

```css
font-size:28px;
font-weight:600;
```

---

## Body Large

```css
font-size:20px;
line-height:1.9;
```

---

## Body Normal

```css
font-size:18px;
line-height:1.8;
```

---

## Small Text

```css
font-size:14px;
```

---

# 4. Spacing System

## 8 Point Grid

```css
4px
8px
16px
24px
32px
48px
64px
96px
128px
```

---

# 5. Layout System

## Container

```css
max-width:1440px;
margin:auto;
padding-inline:32px;
```

---

## Grid

Desktop

```css
12 Columns
```

Tablet

```css
8 Columns
```

Mobile

```css
4 Columns
```

---

# 6. Border Radius System

```css
--radius-xs:8px;
--radius-sm:12px;
--radius-md:16px;
--radius-lg:24px;
--radius-xl:32px;
```

---

# 7. Shadow System

## Small

```css
0 4px 12px rgba(0,0,0,.06)
```

## Medium

```css
0 10px 30px rgba(0,0,0,.08)
```

## Large

```css
0 20px 60px rgba(0,0,0,.12)
```

## Floating

```css
0 30px 100px rgba(0,0,0,.16)
```

---

# 8. Button System

## Primary Button

```html
<button class="btn-primary">
مشاوره رایگان
</button>
```

```css
background:#30475E;
color:white;
height:56px;
padding:0 32px;
border-radius:16px;
font-weight:600;
```

Hover:

```css
transform:translateY(-3px);
```

---

## Secondary Button

```css
background:#CBAF87;
color:#30475E;
```

---

## Ghost Button

```css
background:transparent;
border:1px solid #30475E;
color:#30475E;
```

---

# 9. Navbar Design

Height

```css
90px
```

Features

* Sticky
* Blur Background
* Transparent Hero State
* Animated Scroll State

Structure

```html
Logo

Menu

CTA Button
```

---

# 10. Hero Section

Height

```css
100vh
```

Background

```css
linear-gradient(
135deg,
#30475E,
#4F6A82
)
```

Layout

```html
Left:
Text
CTA

Right:
Image / Video
```

Content

* Headline
* Description
* CTA
* Trust Indicators

---

# 11. Service Cards

Structure

```html
Icon
Title
Description
CTA
```

Card Style

```css
background:white;
padding:40px;
border-radius:24px;
```

Hover

```css
translateY(-10px);
```

---

# 12. Statistics Section

Background

```css
#30475E
```

Numbers

```css
72px
800 weight
#CBAF87
```

Labels

```css
18px
white
```

---

# 13. About Section

Components

* Company Story
* Mission
* Vision
* Values

Layout

```html
Image
Text
```

50 / 50 Split

---

# 14. Portfolio Section

Grid

```css
3 Columns
```

Card

```html
Image
Category
Title
Description
```

Hover

```css
scale(1.03)
```

---

# 15. Testimonial System

Card

```css
background:white;
padding:40px;
border-radius:24px;
```

Components

```html
Avatar
Name
Company
Review
```

---

# 16. FAQ System

Accordion

State

```css
Closed
Open
Hover
```

Animation

```css
300ms ease
```

---

# 17. Contact Section

Components

* Form
* Map
* Contact Info

Fields

```html
Name

Phone

Email

Subject

Message
```

---

# 18. Footer

Background

```css
#30475E
```

Layout

4 Columns

```html
Logo

Quick Links

Services

Contact
```

---

# 19. Motion Design System

## Duration

```css
100ms
200ms
300ms
500ms
```

---

## Easing

```css
ease-in-out
```

---

## Hover

```css
scale(1.03)
```

---

## Cards

```css
translateY(-8px)
```

---

## Buttons

```css
translateY(-3px)
```

---

## Scroll Reveal

```css
opacity:0;
transform:translateY(40px);
```

Visible

```css
opacity:1;
transform:none;
```

---

# 20. Forms

Input

```css
height:56px;
padding:16px;
border-radius:16px;
border:1px solid #DADADA;
```

Focus

```css
border-color:#30475E;
```

---

# 21. Responsive System

## Desktop

```css
1440px+
```

---

## Laptop

```css
1024px
```

---

## Tablet

```css
768px
```

---

## Mobile

```css
480px
```

---

# 22. SEO Structure

Pages

```text
/
about
/services
/projects
/blog
/careers
/contact
```

---

# 23. Accessibility

Minimum Contrast

```css
AA Standard
```

Keyboard Navigation

```css
Required
```

Focus States

```css
Required
```

---

# 24. HTML Folder Structure

```text
project/

index.html

about.html

services.html

projects.html

blog.html

contact.html

assets/

css/
style.css

js/
main.js

images/

fonts/
```

---

# 25. Final Design Direction

Reference Style:

* Stripe
* Linear
* Notion
* Webflow Enterprise
* HubSpot Corporate

Visual Feeling:

* Premium
* Corporate
* Elegant
* Trustworthy
* Modern
* High-End

هدف نهایی این سیستم دیزاین، ساخت یک وب‌سایت شرکتی در سطح برندهای بزرگ است که در نگاه اول حس اعتبار، ثبات مالی، حرفه‌ای بودن و اعتماد را به مخاطب منتقل کند.
