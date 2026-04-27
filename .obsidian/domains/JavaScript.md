---
tags: [domains]
type: domain
projects: 
  - "[[projects/Tropical Architecture Initiative/Tropical Architecture Initiative]]"
created: 2026-04-25
---

# JavaScript

## Overview
Primary language used in the Tropical Architecture Initiative project.

## Usage in Project

### Backend (Node.js)
- `news-scraper.js` — RSS scraping and data generation
- Uses: `https`, `http`, `fs`, `path` modules

### Frontend (Browser)
- `script.js` — DOM manipulation (mobile menu)
- `news-display.js` — Fetch API, dynamic rendering

## Key Patterns Used

### Async/Await
```javascript
async function fetchUrl(url) {
  return new Promise((resolve, reject) => {
    // ...
  });
}
```

### Promise-based HTTP
```javascript
const response = await fetch('news-data.json');
const data = await response.json();
```

### Module Pattern
```javascript
const MODULE = {
  function1: () => {},
  function2: () => {}
};
```

## Related
- [[domains/web-development|Web Development]] (frontend context)
- [[domains/nodejs|Node.js]] (backend context)