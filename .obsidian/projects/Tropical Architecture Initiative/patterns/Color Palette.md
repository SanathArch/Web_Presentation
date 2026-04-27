---
tags: [patterns, project/tropical-initiative]
type: pattern
project: "[[projects/Tropical Architecture Initiative/Tropical Architecture Initiative]]"
created: 2026-04-25
---

# Color Palette

## Brand Colors

| Name | Hex | Usage |
|------|-----|-------|
| Dark Blue | `#2b3290` | Primary brand, nav, headings |
| Yellow | `#ffba33` | Accent, highlights, CTAs |
| White | `#ffffff` | Background, cards |
| Border | `1.5px solid var(--dark-blue)` | Structural lines |

## CSS Variables
```css
:root {
  --dark-blue: #2b3290;
  --white: #ffffff;
  --yellow: #ffba33;
  --border: 1.5px solid var(--dark-blue);
}
```

## Usage Patterns
- **Dark Blue**: Nav brand, section backgrounds, primary text
- **Yellow**: CTAs, tags, accent highlights, active states
- **White**: Main background, card backgrounds
- **Border**: 1.5px dark blue borders separate all grid items

## Related
- [[Design System]] — Parent component
- [[Typography System]] — Font pairing