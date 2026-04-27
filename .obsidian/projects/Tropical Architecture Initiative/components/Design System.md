---
tags: [components, project/tropical-initiative]
type: component
layer: frontend/styles
project: "[[projects/Tropical Architecture Initiative/Tropical Architecture Initiative]]"
created: 2026-04-25
status: active
depends-on: []
depended-on-by: [[News Display]]
key-files: [styles.css]
---

# Design System

## Purpose
Brutalist design system using CSS custom properties for consistent styling across all pages.

## CSS Variables

| Variable | Value | Usage |
|----------|-------|-------|
| `--dark-blue` | `#2b3290` | Primary brand color |
| `--white` | `#ffffff` | Background |
| `--yellow` | `#ffba33` | Accent/highlights |
| `--border` | `1.5px solid var(--dark-blue)` | Structural borders |

## Typography

### Font Stack
- **Primary**: Inter (sans-serif)
- **Monospace**: Space Mono

### Scale
- Hero: `clamp(3rem, 6vw, 6rem)`
- H1-H2: `2.5-5rem`
- H3: `1.5rem`
- Body: `1rem`
- Mono: `0.85rem`

## Grid System
12-column brutalist grid with:
- Equal column widths
- 1.5px solid borders
- No gutters (clean separation)

### Column Spans
- `.col-span-12` — Full width
- `.col-span-6` — Half
- `.col-span-4` — Third
- `.col-span-3` — Quarter

## Key Components

### Navigation
- Sticky top nav
- Brand (dark blue) | Links | Mobile toggle
- Active state: dark blue background

### Cards
- Padding: 2rem
- Full-height flex display
- Border: 1.5px dark blue

### Buttons
- Font: Space Mono uppercase
- Padding: 1rem 2rem
- Primary: Yellow bg, white text
- Secondary: White bg, blue text

### Footer
- 3-column grid
- Newsletter input with attached button

## Responsive Breakpoints
- **1024px**: Stack all columns
- **768px**: Hamburger menu, reduced padding

## Related
- [[News Display]] — Uses this design system