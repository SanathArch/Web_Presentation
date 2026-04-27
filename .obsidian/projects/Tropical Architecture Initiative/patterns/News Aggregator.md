---
tags: [patterns, project/tropical-initiative]
type: pattern
project: "[[projects/Tropical Architecture Initiative/Tropical Architecture Initiative]]"
created: 2026-04-25
---

# News Aggregator Pattern

## Pattern
Server-side scraper generates static JSON that the frontend fetches and renders dynamically. The scraper can run on a schedule, and the frontend handles all rendering without server-side templating.

## Architecture

```
RSS Feeds → news-scraper.js → news-data.json → fetch() → news-display.js → DOM
```

## When to Use
- Content from external sources needs to be displayed
- Updates can be batched (not real-time)
- Client-side rendering is acceptable
- No backend API needed

## Implementation

### Scraper Side
```javascript
async function generateNewsData() {
  // Fetch multiple RSS feeds
  // Parse and filter content
  // Save to JSON file
}
```

### Frontend Side
```javascript
async function loadAndDisplayNews() {
  const data = await fetch('news-data.json');
  renderCollage(data);
}
```

## Advantages
- Simple architecture (no backend)
- Cached data survives server restarts
- Easy to debug (JSON is human-readable)
- CDN-cacheable static file

## Gotchas
- Data freshness depends on scraper frequency
- Large JSON = slower initial load
- Error handling needed for missing data

## Alternatives
- Server-side rendering (EJS, Handlebars)
- API backend (Express + database)
- CMS integration