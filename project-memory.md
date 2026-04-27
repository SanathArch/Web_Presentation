# Tropical Architecture Initiative - Project Memory

**Created:** 2026-04-24
**Project Type:** Static Website - Brutalist Design
**Design Style:** Teenage Engineering-inspired brutalist architecture

---

## 🎯 Project Overview

A global ecosystem website dedicated to researching, designing, and delivering sustainable architectural solutions for tropical climates. The platform focuses on heat, humidity, and tropical climate challenges in architecture.

### Core Mission
> "We empower communities in tropical regions with climate-adapted architecture. Our platform shares research, design guidelines, and innovative products to combat heat, humidity and tropical climate challenges."

---

## 🏗️ Project Structure

```
Website/
├── index.html              # Home/Mission page
├── about.html              # About/Vision page
├── product-solutions.html  # Product Solutions (commerce)
├── design-solutions.html   # Design Solutions (guidelines)
├── research.html           # Research & Publications
├── network.html            # Global Network page
├── contact.html            # Contact form page
├── styles.css              # Main stylesheet (brutalist grid system)
└── script.js               # Mobile menu toggle functionality
```

---

## ✅ Completed Work

### Pages Built
1. **Home (index.html)**
   - Hero section with mission statement
   - Department section explaining tropical climate challenges
   - **NEW: Intelligence Feed section (3-priority news collage)**
   - Full navigation and footer

2. **About/Vision (about.html)****
   - Vision statement: "Ecosystem of Solutions"
   - Background on tropical climate challenges
   - Team section: Universities, NGOs, Green Networks

3. **Product Solutions (product-solutions.html)**
   - Commerce section for physical products
   - Featured: Modular Stilt Foundation Kit ($4,500) - COMPLETED
   - Featured: Bamboo Porosity Facade - IN DEVELOPMENT

4. **Design Solutions (design-solutions.html)**
   - Practical guidelines page
   - Download section for "Design Cheatcodes" PDF
   - Case study previews (Reunion Island, Sabena Towers)

5. **Research (research.html)**
   - Academic & technical backbone section
   - Resources sidebar (Publications, Case Studies, Data Tools, Blog)
   - Featured papers: PAPER_001 (Indochina Buildings), PAPER_002 (Facade Porosity)
   - Data Tools and News/Blog sections

6. **Network (network.html)**
   - Global network visualization
   - Pilot site profile: Jakarta, IDN
   - Call to action for proposing new sites
   - Firms & Contacts directory
   - Academic MOUs (NUS, JCU)

7. **Contact (contact.html)**
   - Contact form with fields (Name, Email, Message)
   - Newsletter signup
   - Social media links (LinkedIn, Twitter/X, Instagram)

### Design System (styles.css)
- **Color Palette:**
  - `--dark-blue: #2b3290` (Primary)
  - `--white: #ffffff` (Background)
  - `--yellow: #ffba33` (Accent - Vivid Orange)

- **Typography:**
  - Primary: Inter (sans-serif)
  - Mono: Space Mono (monospace)

- **Grid System:** 12-column brutalist grid
  - Responsive breakpoints: 1024px, 768px
  - Grid classes: col-span-3, col-span-4, col-span-6, col-span-8, col-span-12

- **Components:**
  - Navigation (sticky, with mobile toggle)
  - Buttons (default, primary)
  - Forms (input fields, textarea)
  - Footer (3-column grid)
  - Tags, section labels, content blocks

### JavaScript
- **script.js**: Mobile menu toggle functionality
- **news-display.js**: Dynamic news collage rendering
- **news-scraper.js**: Node.js content generation script

---

## 🚧 Upcoming Work / TODO

### High Priority
1. **Form Functionality**
   - Contact form needs backend integration
   - Newsletter subscription needs API connection

2. **Product Pages**
   - Create individual product detail pages
   - Add e-commerce functionality (cart, checkout)
   - Build "View Dev Logs" page for Bamboo Porosity Facade

3. **Download System**
   - Create actual PDF downloads for "Design Cheatcodes"
   - Set up research paper PDF downloads

4. **Content Expansion**
   - Write full case studies (Reunion Island Housing, Sabena Towers)
   - Develop Data Tools (thermal comfort calculators, climate charts)
   - Populate News/Blog section

### Medium Priority
5. **Interactive Features**
   - Add image galleries for pilot sites
   - Create interactive map for global network visualization
   - Build portfolio/project showcase pages

6. **SEO & Performance**
   - Add meta descriptions to all pages
   - Implement Open Graph tags
   - Optimize images (currently none embedded)
   - Add sitemap.xml and robots.txt

7. **Accessibility**
   - Add ARIA labels
   - Ensure keyboard navigation
   - Test with screen readers
   - Add skip-to-content links

### Low Priority
8. **Analytics & Tracking**
   - Add Google Analytics or similar
   - Set up conversion tracking for products

9. **Social Integration**
   - Add social sharing buttons
   - Embed social media feeds

10. **Multi-language Support**
    - Consider i18n for tropical regions (Indonesian, French, Spanish, Portuguese)

---

## 🎨 Design Philosophy

**Brutalist Architecture Approach:**
- Sharp, immediate interactions (no soft fade-ups)
- Visible grid system with bold borders
- High contrast color scheme
- Monospace fonts for technical feel
- Functional, raw aesthetic inspired by teenage.engineering

---

## 📋 Technical Notes

- **No framework:** Pure HTML/CSS/JavaScript
- **Responsive:** Mobile-first approach with media queries
- **Fonts:** Google Fonts (Inter + Space Mono)
- **No images currently embedded:** Placeholder structure ready
- **Forms:** Currently non-functional (need backend)

---

## 🔗 Navigation Structure

```
Home → About/Vision → Product Solutions → Design Solutions → Research → Network → Contact
```

All pages have consistent:
- Sticky navigation with active state
- Footer with 3 sections (Brand, Index, Newsletter)
- Mobile menu toggle

---

## 📍 Next Steps Recommendation

1. Set up form backend (Formspree, Netlify Forms, or custom)
2. Create product detail page template
3. Add actual images for visual impact
4. Implement download functionality for resources
5. Build out blog/news section with CMS integration

---

**Tags:** #website #tropical-architecture #brutalist-design #static-site #sustainability
