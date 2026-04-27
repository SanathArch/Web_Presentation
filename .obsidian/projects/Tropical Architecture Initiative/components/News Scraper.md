---
tags: [components, project/tropical-initiative]
type: component
layer: backend/data
project: "[[projects/Tropical Architecture Initiative/Tropical Architecture Initiative]]"
created: 2026-04-25
status: active
depends-on: []
depended-on-by: [[news-display.js]]
key-files: [news-scraper.js, news-data.json]
---

# News Scraper

## Purpose
Node.js script that scrapes RSS feeds from architecture websites and generates `news-data.json` for the frontend.

## Functionality

### RSS Feed Sources
Organized into 3 priority categories:

**Priority 01: Materials & Vernacular Wisdom**
- ArchDaily materials feeds
- Dezeen sustainable materials
- Vernacular architecture sources

**Priority 02: Climate Solutions & Research**
- Sustainability research
- Field studies and case studies
- Green certification (LEED, Passive House, Net Zero)

**Priority 03: AI + Architecture**
- Generative design
- Machine learning
- Parametric modeling

### Key Functions

| Function | Purpose |
|----------|---------|
| `fetchUrl()` | HTTP GET with timeout/retry |
| `parseRSS()` | XML parsing for item extraction |
| `fetchCategoryFeeds()` | Batch fetch multiple feeds |
| `filterByKeywords()` | Category-specific filtering |
| `generateNewsData()` | Main orchestration |

### Data Structure
```javascript
{
  priority1: [],  // Materials & quotes
  priority2: [],  // Research & projects
  priority3: [],  // AI tools
  categories: { /* detailed breakdown */ },
  allQuotes: [],  // Full quote database
  allMaterials: [], // Fallback materials
  lastUpdated: ISO_DATE
}
```

## Usage
```bash
node news-scraper.js
```

## Gotchas
- Falls back to curated content if RSS scraping fails
- Quotes are hardcoded in the file (12 architect quotes)
- Rate limiting handled with retries (2 attempts per URL)