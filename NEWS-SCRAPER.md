# 📰 News Scraper System

## Overview

Automated news aggregation system that curates content for the Tropical Architecture Initiative homepage. Content is organized into three priority levels and displayed in a brutalist collage layout.

---

## 🗂️ File Structure

```
Website/
├── news-scraper.js       # Node.js script to scrape/generate news
├── news-display.js       # Frontend script to display news
├── news-data.json        # Generated news data (auto-created)
└── NEWS-SCRAPER.md       # This documentation
```

---

## 📋 Priority Levels

### Priority 01: Materials & Vernacular Wisdom
- **New Materials**: Innovative sustainable building materials
- **Architect Quotes**: Wisdom from tropical/vernacular architecture pioneers
- **Focus**: Hassan Fathy, Geoffrey Bawa, Vo Trong Nghia, etc.

### Priority 02: Climate Solutions & Research
- **Research Papers**: Academic studies on tropical architecture
- **Field Studies**: Real-world project case studies
- **Green Certification**: Standards and guidelines updates

### Priority 03: AI + Architecture
- **Generative Design**: AI-powered design tools
- **Machine Learning**: Climate prediction, optimization
- **Parametric Modeling**: Computational design advances

---

## 🚀 Usage

### Step 1: Generate/Update News Data

Run the scraper to generate fresh content:

```bash
node news-scraper.js
```

This creates/updates `news-data.json` with:
- 6 Priority 1 items (materials + quotes)
- 3 Priority 2 items (research/projects)
- 3 Priority 3 items (AI tools/research)
- 8 architect quotes for carousel

### Step 2: Automatic Display

The homepage (`index.html`) automatically loads and displays news via `news-display.js`. No manual intervention needed.

### Step 3: Schedule Updates (Optional)

Set up a cron job to update news weekly:

```bash
# Edit crontab
crontab -e

# Add weekly update (every Monday at 9 AM)
0 9 * * 1 cd /path/to/Website && node news-scraper.js
```

---

## 🔧 Customization

### Add Custom Sources

Edit `news-scraper.js` to add RSS feeds:

```javascript
const RSS_FEEDS = {
    priority1: [
        'https://www.archdaily.com/tag/materials/feed',
        'YOUR_CUSTOM_FEED_URL'
    ],
    // ...
};
```

### Add Architect Quotes

Add to the `ARCHITECT_QUOTES` array in `news-scraper.js`:

```javascript
{
    quote: "Your quote here",
    author: "Architect Name",
    context: "Brief description/context"
}
```

### Adjust Update Frequency

Quote carousel auto-rotates every 5 seconds. Change in `news-display.js`:

```javascript
setInterval(() => {
    // ... rotation logic
}, 5000); // Change this value (milliseconds)
```

---

## 📊 Data Structure

### news-data.json Format

```json
{
  "priority1": [
    {
      "title": "Material/News Title",
      "description": "Brief description...",
      "source": "Source publication",
      "date": "2026-04-24T10:00:00.000Z",
      "url": "https://...",
      "type": "material|quote|research|project|ai-tool"
    }
  ],
  "priority2": [...],
  "priority3": [...],
  "quotes": [...],
  "materials": [...],
  "lastUpdated": "2026-04-24T10:00:00.000Z"
}
```

---

## 🎨 Display Features

### Collage Layout
- **Priority 1**: 2-column (materials left, quote carousel right)
- **Priority 2**: 3-column grid
- **Priority 3**: 3-column grid with gradient header

### Interactive Elements
- Auto-rotating quotes (5-second intervals)
- Hover effects on cards
- Responsive design for mobile

### Visual Hierarchy
- Color-coded tags by priority
- Consistent brutalist styling
- Date formatting (TODAY, YESTERDAY, etc.)

---

## 🐛 Troubleshooting

### News Feed Not Loading

1. **Check if news-data.json exists**
   ```bash
   ls news-data.json
   ```

2. **Run the scraper**
   ```bash
   node news-scraper.js
   ```

3. **Check browser console for errors**
   - Open DevTools → Console
   - Look for fetch errors

### Quotes Not Rotating

- Check browser console for JavaScript errors
- Verify at least 2 quotes exist in `news-data.json`

### Styling Issues

- Ensure `styles.css` is loaded after any custom CSS
- Check that CSS variables are defined in `:root`

---

## 📝 Future Enhancements

### Planned Features
- [ ] Real RSS feed parsing (currently uses mock data)
- [ ] Admin panel for manual content curation
- [ ] Content filtering by tags/categories
- [ ] Social media sharing integration
- [ ] Email newsletter generation from news
- [ ] Search functionality
- [ ] Archive of past news items

### API Integration Ideas
- ArchDaily API
- Dezeen RSS
- Google News API (filtered queries)
- Research paper APIs (CrossRef, arXiv)

---

## 📞 Support

For issues or questions:
1. Check browser console for errors
2. Verify `news-data.json` is valid JSON
3. Ensure Node.js is installed for scraper
4. Review this documentation

---

**Last Updated:** 2026-04-24
**Version:** 1.0.0
