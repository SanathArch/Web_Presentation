document.addEventListener('DOMContentLoaded', () => {
    // Mobile menu toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');

    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('show');
            const isExpanded = navLinks.classList.contains('show');
            mobileMenuBtn.textContent = isExpanded ? 'CLOSE' : 'MENU';
        });
    }

    // In a brutalist design, we avoid soft fade-ups. 
    // Interactions should be immediate and sharp.
    // So we've removed the scroll observers for a starker feel.

    // Newsletter Integration
    const newsletterEmail = document.getElementById('newsletter-email');
    const newsletterJoin = document.getElementById('newsletter-join');
    const newsletterStatus = document.getElementById('newsletter-status');

    if (newsletterJoin && newsletterEmail && newsletterStatus) {
        newsletterJoin.addEventListener('click', async () => {
            const email = newsletterEmail.value.trim();
            newsletterStatus.style.display = 'block';
            
            // Basic validation
            if (!email || !email.includes('@') || !email.includes('.')) {
                newsletterStatus.style.color = 'red';
                newsletterStatus.textContent = 'ERROR: INVALID EMAIL FORMAT';
                return;
            }

            newsletterStatus.style.color = 'var(--dark-blue)';
            newsletterStatus.textContent = 'SUBSCRIBING...';

            try {
                const response = await fetch('http://localhost:5000/api/subscribe', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email })
                });
                
                const data = await response.json();
                
                if (data.success) {
                    newsletterStatus.style.color = 'green';
                    newsletterStatus.textContent = 'SUCCESS: ' + data.message.toUpperCase();
                    newsletterEmail.value = '';
                } else {
                    newsletterStatus.style.color = 'red';
                    newsletterStatus.textContent = 'ERROR: ' + data.message.toUpperCase();
                }
            } catch (err) {
                console.error(err);
                newsletterStatus.style.color = 'red';
                newsletterStatus.textContent = 'ERROR: BACKEND UNREACHABLE. PLEASE ENSURE IT IS RUNNING.';
            }
        });
    }
});
