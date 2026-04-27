---
tags: [patterns, project/tropical-initiative]
type: pattern
project: "[[projects/Tropical Architecture Initiative/Tropical Architecture Initiative]]"
created: 2026-04-25
---

# Typography System

## Font Stack

| Font | Type | Usage |
|------|------|-------|
| Inter | Sans-serif | Primary body text, headings |
| Space Mono | Monospace | Labels, tags, buttons, accents |

## Import
```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap');
```

## Scale

| Element | Size | Weight |
|---------|------|--------|
| Hero Title | `clamp(3rem, 6vw, 6rem)` | 700 |
| H1-H2 | `2.5-5rem` | 700 |
| H3 | `1.5rem` | 700 |
| Body | `1rem` | 400 |
| Mono (labels) | `0.85rem` | 400 |

## Text Styles

### Uppercase Headings
```css
h1, h2, h3, h4, h5, h6 {
  font-weight: 700;
  line-height: 1.1;
  text-transform: uppercase;
  letter-spacing: -0.02em;
}
```

### Mono Class
```css
.mono {
  font-family: var(--font-mono);
  font-size: 0.85rem;
  text-transform: uppercase;
}
```

## Related
- [[Design System]] — Parent component
- [[Color Palette]] — Brand colors