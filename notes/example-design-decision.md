---
created: 2026-04-24
decision-type: Color System
impact: high
tags: [design, decision, architecture]
---

# Design Decision: Brutalist Color Palette

## 🎯 Context
Needed to establish a cohesive color system that reflects the teenage.engineering aesthetic while maintaining accessibility and brand identity for tropical architecture focus.

## 🔍 Options Considered

### Option A: Full Color Spectrum
- **Pros:** More visual variety, vibrant feel
- **Cons:** Loses brutalist minimalism, harder to maintain consistency

### Option B: Monochrome Only
- **Pros:** Very brutalist, clean, easy to maintain
- **Cons:** Too sterile, doesn't convey tropical warmth

### Option C: Limited Palette (CHOSEN) ✅
- **Pros:** Best of both worlds - brutalist base with strategic accent
- **Cons:** Requires discipline to not add more colors

## ✅ Decision Made
**Three-color system:**
- `--dark-blue: #2b3290` - Primary (professional, trust)
- `--white: #ffffff` - Background (clean, minimal)
- `--yellow: #ffba33` - Accent (energy, tropical sun, call-to-action)

## 📐 Implementation Details
- **Files affected:** `styles.css`
- **CSS variables:** Defined in `:root`
- **Usage rules:**
  - Yellow ONLY for: primary buttons, tags, highlights
  - Dark blue for: borders, text, backgrounds
  - White for: main backgrounds, button hover states

## 🔗 Related To
- [[project-memory]] - Design Philosophy section
- [[design-solutions.html]]
- [[styles.css]]
- [[templates/design-decisions-template]]

## 📊 Impact Assessment
- [x] Performance - No impact, CSS variables are efficient
- [x] Accessibility - Contrast ratios checked (AA compliant)
- [x] Mobile responsiveness - Colors work across devices
- [x] Browser compatibility - Full support

---

**Status:** #approved
**Review Date:** 2026-05-24
