import glob

html_files = glob.glob('*.html')
target = '''            <div>
                <h3 class="footer-title">NEWSLETTER</h3>
                <div class="newsletter-input">
                    <input type="email" placeholder="ENTER EMAIL">
                    <button class="btn btn-primary" style="padding: 1rem;">JOIN</button>
                </div>
                <p class="mono" style="margin-top: 1rem; color: #666; font-size: 0.7rem;">&copy; 2026. ALL RIGHTS
                    RESERVED.</p>'''
                    
replacement = '''            <div>
                <h3 class="footer-title">NEWSLETTER</h3>
                <div class="newsletter-input">
                    <input type="email" id="newsletter-email" placeholder="ENTER EMAIL">
                    <button id="newsletter-join" class="btn btn-primary" style="padding: 1rem;">JOIN</button>
                </div>
                <p id="newsletter-status" class="mono" style="margin-top: 0.5rem; font-size: 0.8rem; display: none;"></p>
                <p class="mono" style="margin-top: 1rem; color: #666; font-size: 0.7rem;">&copy; 2026. ALL RIGHTS
                    RESERVED.</p>'''

for f in html_files:
    if f == 'index.html': continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if target in content:
        content = content.replace(target, replacement)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Updated {f}')
    else:
        print(f'Target not found in {f}, skipping or trying alternative formatting.')
