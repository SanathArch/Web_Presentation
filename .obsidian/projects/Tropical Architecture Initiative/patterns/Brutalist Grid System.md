---
tags: [patterns, project/tropical-initiative]
type: pattern
project: "[[projects/Tropical Architecture Initiative/Tropical Architecture Initiative]]"
created: 2026-04-25
---

# Brutalist Grid System

## Pattern
Using a rigid 12-column CSS Grid with visible borders to create a brutalist, architectural aesthetic.

## Implementation

```css
.grid-container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
}

.grid-item {
  border-right: 1.5px solid var(--dark-blue);
}
```

## When to Use
- When you want strong structural visual language
- For content-heavy pages needing clear hierarchy
- When grid alignment matters more than whitespace

## Examples in Project
- Homepage: 12-column news collage
- About: 2x4 content blocks
- Footer: 3-column layout

## Column Spans
| Class | Columns | Use Case |
|-------|---------|----------|
| `.col-span-12` | 12 | Full width sections |
| `.col-span-6` | 6 | Two-column layouts |
| `.col-span-4` | 4 | Three-column layouts |
| `.col-span-3` | 3 | Four-column grids |

## Alternatives
- Flexbox for single-row layouts
- CSS Subgrid for nested alignment