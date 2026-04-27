---
tags: [components, project/tropical-initiative]
type: component
layer: frontend/rendering
project: "[[projects/Tropical Architecture Initiative/Tropical Architecture Initiative]]"
created: 2026-04-25
status: active
depends-on: [[News Scraper]]
depended-on-by: []
key-files: [news-display.js, index.html]
---

# News Display System

## Purpose
Client-side JavaScript that renders the dynamic news collage on the homepage by loading `news-data.json`.

## Components

### Card Types
1. **Material Cards** — Display sustainable materials with yellow tags
2. **Research Cards** — Show climate/field studies with dark blue tags
3. **AI Cards** — Present AI tools with gradient backgrounds
4. **Quote Cards** — Featured architect quotes (large, strip, small variants)

### Layout Structure
The collage is a 12-column CSS Grid with mixed spans:
- Row 1: Quote (6) + Material (3) + AI (3)
- Row 2-3: Priority headers as visual blocks
- Row 4: AI (3) + AI (3) + Research (3) + Research (3)
- Row 5: Material (4) + Quote small (4) + Quote dark (4)

### Key Functions

| Function | Purpose |
|----------|---------|
| `formatDate()` | Relative time display |
| `createCard()` | Material/research/AI card generation |
| `createQuoteCard()` | Quote card variants |
| `renderCollage()` | Main layout rendering |
| `loadAndDisplayNews()` | JSON fetch + error handling |

## Data Flow
```
news-data.json → loadAndDisplayNews() → renderCollage() → DOM
```

## Dependencies
- [[news-scraper.js]] (generates news-data.json)
- [[styles.css]] (grid and card styles)

## Gotchas
- Auto-rotates quotes in the strip section (5-second interval)
- Graceful fallback when JSON unavailable
- Uses `fetch()` API (no external dependencies)