---
tags: [project/tropical-initiative]
type: project
created: 2026-04-25
status: active
language: [JavaScript, HTML, CSS]
framework: []
---

# Tropical Architecture Initiative

## Overview
A web platform for tropical climate-adapted architecture featuring:
- News scraper that aggregates RSS feeds from architecture sources
- Dynamic collage-style news display
- Product and design solutions showcase

## Architecture

### Pages (Entry Points)
| Page | Component | Purpose |
|------|-----------|---------|
| `index.html` | [[Homepage]] | Main landing with news collage |
| `about.html` | [[About Page]] | Vision and team |
| `product-solutions.html` | [[Product Solutions]] | Physical products |
| `design-solutions.html` | [[Design Solutions]] | Design guidelines |
| `research.html` | [[Research Page]] | Academic resources |
| `network.html` | [[Network Page]] | Global network |
| `contact.html` | [[Contact Page]] | Communication hub |

### Core Components

| Component | Files | Purpose |
|-----------|-------|---------|
| [[News Scraper]] | news-scraper.js | RSS feed aggregation |
| [[News Display]] | news-display.js | Dynamic collage rendering |
| [[Design System]] | styles.css | Brutalist design system |

### Utilities
- `script.js` — Mobile menu toggle
- `news-data.json` — Cached scraped content

### Patterns
| Pattern | Description |
|---------|-------------|
| [[Brutalist Grid System]] | 12-column CSS Grid with visible borders |
| [[News Aggregator]] | Server-side scraper → JSON → client render |
| [[Color Palette]] | Brand colors (Dark Blue, Yellow, White) |
| [[Typography System]] | Inter + Space Mono font pairing |

### Architecture Decisions
- Static JSON approach for news (no backend API)
- CSS Grid for responsive brutalist aesthetic
- RSS scraping for external content aggregation

## Tech Stack

### Dependencies
- `axios` (^1.6.0) — HTTP requests
- `cheerio` (^1.0.0-rc.12) — HTML parsing

### External Resources
- Google Fonts: Inter, Space Mono

## Key Content

### Products
- **Modular Stilt Foundation Kit** ($4,500) — Completed
- **Bamboo Porosity Facade** — In development

### Research Publications
- PAPER_001: Adaptive Design for Indochina-style Buildings
- PAPER_002: Thermal Comfort via Facade Porosity

### Pilot Sites
- Jakarta, Indonesia — Urban heat mitigation study

## Related Notes
- [[domains/javascript|JavaScript]] — Development language
- [[domains/web-development|Web Development]] — Frontend context
- [[domains/architecture|Architecture]] — Domain focus