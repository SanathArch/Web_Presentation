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
});
