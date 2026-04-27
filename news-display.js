/**
 * Tropical Architecture Initiative - News Display Script (Collage Version)
 * 
 * Displays scraped news content in a random collage layout
 * Loads from news-data.json and renders cards dynamically
 */

// News data will be loaded here
let newsData = null;

/**
 * Format date for display
 */
function formatDate(dateString) {
    const date = new Date(dateString);
    const now = new Date();
    const diffTime = Math.abs(now - date);
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    
    if (diffDays === 0) return 'TODAY';
    if (diffDays === 1) return 'YESTERDAY';
    if (diffDays < 7) return `${diffDays} DAYS AGO`;
    if (diffDays < 30) return `${Math.floor(diffDays / 7)} WEEKS AGO`;
    return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
}

/**
 * Generate a dynamic image prompt based on the news item
 */
function getInferencePrompt(item) {
    const typeStr = item.type ? item.type.replace('-', ' ') : 'architecture';
    return `tropical architecture ${typeStr}, ${item.title}, high quality architectural photography`;
}

/**
 * Create a material/news card HTML element
 */
function createCard(item, cardType) {
    let content = '';
    
    // Generate image URL based on inference of the news item
    const prompt = getInferencePrompt(item);
    const seed = Math.floor(Math.random() * 10000); // Prevent caching
    const imgUrl = `https://image.pollinations.ai/prompt/${encodeURIComponent(prompt)}?width=600&height=800&nologo=true&seed=${seed}`;
    
    const bgImageStyle = `position: absolute; top: 0; left: 0; right: 0; bottom: 0; background-image: url('${imgUrl}'); background-size: cover; background-position: center; opacity: 0.6; z-index: 0; transition: transform 0.5s ease;`;
    
    if (cardType === 'material' || item.type === 'material') {
        content = `
            <div style="position: relative; overflow: hidden; height: 100%; background: var(--white); color: var(--dark-blue);">
                <div class="card-bg" style="${bgImageStyle}"></div>
                <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(to bottom, rgba(255,255,255,0.6), rgba(255,255,255,0.95)); z-index: 1;"></div>
                <div style="position: relative; z-index: 2; padding: 2rem; height: 100%; display: flex; flex-direction: column; justify-content: center;">
                    <span class="tag" style="align-self: flex-start; margin-bottom: 1rem; background: var(--yellow); color: var(--dark-blue);">NEW MATERIAL</span>
                    <h3 style="font-size: 1.1rem; margin-bottom: 0.8rem; line-height: 1.3;">${item.title}</h3>
                    <p style="flex: 1; font-size: 0.9rem; line-height: 1.5; margin-bottom: 1rem;">${item.description}</p>
                    <div style="margin-top: auto;">
                        <p class="mono" style="font-size: 0.7rem; color: #444;">${item.source}</p>
                        <p class="mono" style="font-size: 0.65rem; color: #666; margin-top: 0.3rem;">${formatDate(item.date)}</p>
                    </div>
                </div>
            </div>
        `;
    } else if (cardType === 'research' || item.type === 'research' || item.type === 'project' || item.type === 'standards') {
        content = `
            <div style="position: relative; overflow: hidden; height: 100%; background: var(--white); color: var(--dark-blue);">
                <div class="card-bg" style="${bgImageStyle}"></div>
                <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(to bottom, rgba(255,255,255,0.6), rgba(255,255,255,0.95)); z-index: 1;"></div>
                <div style="position: relative; z-index: 2; padding: 2rem; height: 100%; display: flex; flex-direction: column; justify-content: center;">
                    <span class="tag" style="align-self: flex-start; margin-bottom: 1rem; background: var(--dark-blue); color: var(--white);">${(item.type || 'research').toUpperCase()}</span>
                    <h3 style="font-size: 1.1rem; margin-bottom: 0.8rem; line-height: 1.3;">${item.title}</h3>
                    <p style="flex: 1; font-size: 0.9rem; line-height: 1.5; margin-bottom: 1rem;">${item.description}</p>
                    <div style="margin-top: auto;">
                        <a href="${item.url || '#'}" class="mono" style="font-size: 0.75rem; text-decoration: underline; color: var(--dark-blue);">READ MORE →</a>
                        <p class="mono" style="font-size: 0.7rem; color: #444; margin-top: 0.5rem;">${item.source} • ${formatDate(item.date)}</p>
                    </div>
                </div>
            </div>
        `;
    } else if (cardType === 'ai' || item.type === 'ai-tool' || item.type === 'ai-research') {
        content = `
            <div style="position: relative; overflow: hidden; height: 100%; background: var(--dark-blue); color: var(--white);">
                <div class="card-bg" style="${bgImageStyle}"></div>
                <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(to bottom, rgba(26,31,92,0.5), rgba(26,31,92,0.95)); z-index: 1;"></div>
                <div style="position: relative; z-index: 2; padding: 2rem; height: 100%; display: flex; flex-direction: column; justify-content: center;">
                    <span class="tag" style="align-self: flex-start; margin-bottom: 1rem; background: linear-gradient(135deg, var(--dark-blue), var(--yellow)); color: var(--white);">AI + ARCH</span>
                    <h3 style="font-size: 1.1rem; margin-bottom: 0.8rem; line-height: 1.3; color: var(--white);">${item.title}</h3>
                    <p style="flex: 1; font-size: 0.9rem; line-height: 1.5; margin-bottom: 1rem; color: #eee;">${item.description}</p>
                    <div style="margin-top: auto;">
                        <a href="${item.url || '#'}" class="mono" style="font-size: 0.75rem; text-decoration: underline; color: var(--yellow);">LEARN MORE →</a>
                        <p class="mono" style="font-size: 0.7rem; color: #ccc; margin-top: 0.5rem;">${item.source} • ${formatDate(item.date)}</p>
                    </div>
                </div>
            </div>
        `;
    }
    
    return content;
}

/**
 * Generate a dynamic image prompt based on a quote
 */
function getQuoteInferencePrompt(quote) {
    return `tropical architecture concept, ${quote.author}, moody atmospheric architectural lighting`;
}

/**
 * Create quote card HTML
 */
function createQuoteCard(quote, variant = 'default') {
    const prompt = getQuoteInferencePrompt(quote);
    const seed = Math.floor(Math.random() * 10000);
    const imgUrl = `https://image.pollinations.ai/prompt/${encodeURIComponent(prompt)}?width=800&height=600&nologo=true&seed=${seed}`;
    const bgImageStyle = `position: absolute; top: 0; left: 0; right: 0; bottom: 0; background-image: url('${imgUrl}'); background-size: cover; background-position: center; opacity: 0.6; z-index: 0; transition: transform 0.5s ease;`;

    if (variant === 'large') {
        return `
            <div style="position: relative; overflow: hidden; padding: 3rem; height: 100%; display: flex; flex-direction: column; justify-content: center; background: var(--dark-blue); color: var(--white);">
                <div class="card-bg" style="${bgImageStyle}"></div>
                <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(to bottom, rgba(26,31,92,0.4), rgba(26,31,92,0.9)); z-index: 1;"></div>
                <div style="position: relative; z-index: 2; height: 100%; display: flex; flex-direction: column;">
                    <span class="tag" style="align-self: flex-start; margin-bottom: 2rem; background: var(--yellow); color: var(--dark-blue);">FEATURED QUOTE</span>
                    <blockquote style="font-size: 1.6rem; line-height: 1.3; font-style: italic; margin-bottom: 2rem; color: var(--white);">"${quote.quote}"</blockquote>
                    <div style="margin-top: auto;">
                        <strong style="font-family: var(--font-mono); font-size: 1.1rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--white);">— ${quote.author}</strong>
                        ${quote.context ? `<p class="mono" style="margin-top: 0.5rem; font-size: 0.8rem; color: #ccc;">${quote.context}</p>` : ''}
                    </div>
                </div>
            </div>
        `;
    } else if (variant === 'strip') {
        return `
            <div style="position: relative; overflow: hidden; padding: 2rem; height: 100%; display: flex; flex-direction: column; justify-content: center; background: var(--white); border-left: 4px solid var(--yellow); color: var(--dark-blue);">
                <div class="card-bg" style="${bgImageStyle}"></div>
                <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(to right, rgba(255,255,255,0.9), rgba(255,255,255,0.7)); z-index: 1;"></div>
                <div style="position: relative; z-index: 2; height: 100%; display: flex; flex-direction: column;">
                    <blockquote style="font-size: 1.2rem; line-height: 1.4; font-style: italic; margin-bottom: 1rem;">"${quote.quote}"</blockquote>
                    <div style="margin-top: auto;">
                        <strong style="font-family: var(--font-mono); font-size: 0.9rem; text-transform: uppercase;">— ${quote.author}</strong>
                    </div>
                </div>
            </div>
        `;
    } else if (variant === 'small-dark') {
        return `
            <div style="position: relative; overflow: hidden; padding: 1.5rem; height: 100%; display: flex; flex-direction: column; justify-content: center; background: var(--dark-blue); color: var(--white);">
                <div class="card-bg" style="${bgImageStyle}"></div>
                <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: rgba(26,31,92,0.8); z-index: 1;"></div>
                <div style="position: relative; z-index: 2; height: 100%; display: flex; flex-direction: column;">
                    <blockquote style="font-size: 1rem; line-height: 1.4; font-style: italic; margin-bottom: 0.8rem; color: var(--white);">"${quote.quote}"</blockquote>
                    <strong style="font-family: var(--font-mono); font-size: 0.75rem; text-transform: uppercase; color: var(--yellow);">— ${quote.author}</strong>
                </div>
            </div>
        `;
    } else {
        // Default small
        return `
            <div style="position: relative; overflow: hidden; padding: 1.5rem; height: 100%; display: flex; flex-direction: column; justify-content: center; background: var(--white); color: var(--dark-blue);">
                <div class="card-bg" style="${bgImageStyle}"></div>
                <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: rgba(255,255,255,0.85); z-index: 1;"></div>
                <div style="position: relative; z-index: 2; height: 100%; display: flex; flex-direction: column;">
                    <blockquote style="font-size: 0.95rem; line-height: 1.4; font-style: italic; margin-bottom: 0.8rem;">"${quote.quote}"</blockquote>
                    <strong style="font-family: var(--font-mono); font-size: 0.7rem; text-transform: uppercase;">— ${quote.author}</strong>
                    ${quote.context ? `<p class="mono" style="margin-top: 0.3rem; font-size: 0.65rem; color: #555;">${quote.context}</p>` : ''}
                </div>
            </div>
        `;
    }
}

/**
 * Render the entire collage layout
 */
function renderCollage() {
    if (!newsData) return;
    
    const materials = newsData.priority1.filter(item => item.type === 'material');
    const quotes = newsData.priority1.filter(item => item.type === 'quote');
    const research = newsData.priority2;
    const ai = newsData.priority3;
    
    // Row 1: Large Quote (col-span-6) + Material (col-span-3) + AI (col-span-3)
    const quoteLargeEl = document.getElementById('collage-quote-large');
    if (quoteLargeEl && quotes.length > 0) {
        quoteLargeEl.innerHTML = createQuoteCard(quotes[0], 'large');
    }
    
    const material1El = document.getElementById('collage-material-1');
    if (material1El && materials.length > 0) {
        material1El.innerHTML = createCard(materials[0], 'material');
    }
    
    const ai1El = document.getElementById('collage-ai-1');
    if (ai1El && ai.length > 0) {
        ai1El.innerHTML = createCard(ai[0], 'ai');
    }
    
    // Row 3: Research (col-span-4) + Material (col-span-3) + Quote Strip (col-span-5)
    const research1El = document.getElementById('collage-research-1');
    if (research1El && research.length > 0) {
        research1El.innerHTML = createCard(research[0], 'research');
    }
    
    const material2El = document.getElementById('collage-material-2');
    if (material2El && materials.length > 1) {
        material2El.innerHTML = createCard(materials[1], 'material');
    }
    
    const quoteStripEl = document.getElementById('collage-quote-strip');
    if (quoteStripEl && quotes.length > 1) {
        // Auto-rotate quotes in strip
        let currentQuote = 1;
        const renderQuote = () => {
            const quote = quotes[currentQuote % quotes.length];
            quoteStripEl.innerHTML = createQuoteCard(quote, 'strip');
            currentQuote++;
        };
        renderQuote();
        setInterval(renderQuote, 5000);
    }
    
    // Row 4: AI (col-span-3) + AI (col-span-3) + Research (col-span-3) + Research (col-span-3)
    const ai2El = document.getElementById('collage-ai-2');
    if (ai2El && ai.length > 1) {
        ai2El.innerHTML = createCard(ai[1], 'ai');
    }
    
    const ai3El = document.getElementById('collage-ai-3');
    if (ai3El && ai.length > 2) {
        ai3El.innerHTML = createCard(ai[2], 'ai');
    }
    
    const research2El = document.getElementById('collage-research-2');
    if (research2El && research.length > 1) {
        research2El.innerHTML = createCard(research[1], 'research');
    }
    
    const research3El = document.getElementById('collage-research-3');
    if (research3El && research.length > 2) {
        research3El.innerHTML = createCard(research[2], 'research');
    }
    
    // Row 5: Material (col-span-4) + Small Quote (col-span-4) + Small Quote Dark (col-span-4)
    const material3El = document.getElementById('collage-material-3');
    if (material3El && materials.length > 2) {
        material3El.innerHTML = createCard(materials[2], 'material');
    }
    
    const quoteSmall1El = document.getElementById('collage-quote-small-1');
    if (quoteSmall1El && quotes.length > 2) {
        quoteSmall1El.innerHTML = createQuoteCard(quotes[2], 'small');
    }
    
    const quoteSmall2El = document.getElementById('collage-quote-small-2');
    if (quoteSmall2El && quotes.length > 3) {
        quoteSmall2El.innerHTML = createQuoteCard(quotes[3], 'small-dark');
    }
}

/**
 * Load news data and render collage
 */
async function loadAndDisplayNews() {
    const loadingEl = document.getElementById('news-loading');
    
    try {
        const response = await fetch('news-data.json');
        if (!response.ok) {
            throw new Error('News data not found');
        }
        newsData = await response.json();
        
        // Hide loading message
        if (loadingEl) loadingEl.style.display = 'none';
        
        // Render collage
        renderCollage();
        
        console.log('✅ News collage loaded successfully');
        
    } catch (error) {
        console.warn('⚠️ Could not load news data.');
        
        if (loadingEl) loadingEl.style.display = 'none';
        
        // Show fallback message
        const fallbackMsg = document.createElement('div');
        fallbackMsg.className = 'grid-item col-span-12 content-block';
        fallbackMsg.style.cssText = 'text-align: center; padding: 3rem;';
        fallbackMsg.innerHTML = `
            <span class="tag" style="margin-bottom: 1rem;">NEWS FEED</span>
            <h3 style="margin-bottom: 1rem;">INTELLIGENCE FEED UNAVAILABLE</h3>
            <p class="mono" style="max-width: 600px; margin: 0 auto;">
                Run <code style="background: #f0f0f0; padding: 0.2rem 0.5rem;">node news-scraper.js</code> to generate news-data.json
            </p>
        `;
        
        document.getElementById('news-collage').parentNode.insertBefore(fallbackMsg, document.getElementById('news-collage').nextSibling);
    }
}

/**
 * Initialize when DOM is ready
 */
document.addEventListener('DOMContentLoaded', () => {
    const collageEl = document.getElementById('news-collage');
    if (collageEl) {
        loadAndDisplayNews();
    }
});
