---
tags: [components, project/tropical-initiative]
type: component
layer: frontend/pages
project: "[[projects/Tropical Architecture Initiative/Tropical Architecture Initiative]]"
created: 2026-04-25
status: active
depends-on: [[Design System]]
depended-on-by: []
key-files: [index.html, news-display.js]
---

# Homepage

## Purpose
Main landing page featuring the Tropical Architecture Initiative hero and dynamic news collage.

## Structure

### Sections
1. **Navigation** — Sticky nav with 7 links
2. **Hero** — Mission statement with CTAs
3. **Department** — Climate challenges overview (3 blocks)
4. **News Collage** — Dynamic intelligence feed (main feature)
5. **Footer** — 3-column with newsletter

## Key Features

### Intelligence Feed
Loads `news-data.json` and renders in collage layout:
- Material cards (sustainable materials)
- Quote cards (architect quotes)
- Research cards (climate solutions)
- AI cards (technology)

### Dynamic Updates
- Quotes auto-rotate every 5 seconds
- Cards populated via [[News Display]] component
- Graceful fallback when data unavailable

## Content Sources
- RSS feeds via [[News Scraper]]
- Hardcoded architect quotes (12 quotes)
- Fallback content for when scraping fails

## Files
- `index.html` — Structure
- `news-display.js` — Collage rendering
- `styles.css` — Design system

## Related Pages
- [[About Page]]
- [[Product Solutions]]
- [[Design Solutions]]
- [[Research Page]]