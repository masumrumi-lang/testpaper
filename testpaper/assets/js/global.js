/**
 * Global JavaScript for Etestpaper Responsive Design
 */

document.addEventListener('DOMContentLoaded', function() {
    initMobileMenu();
    wrapTables();
    optimizeButtons();
    
    // Watch for dynamic content changes (for MCQ/CQ pages)
    const observer = new MutationObserver((mutations) => {
        let needsWrap = false;
        mutations.forEach((mutation) => {
            if (mutation.addedNodes.length) {
                needsWrap = true;
            }
        });
        if (needsWrap) {
            wrapTables();
            optimizeButtons();
        }
    });
    
    const container = document.getElementById('mcqListContainer') || document.getElementById('cqListContainer') || document.body;
    observer.observe(container, { childList: true, subtree: true });
});

/**
 * Mobile Menu Logic
 */
function initMobileMenu() {
    const menuBtn = document.getElementById('mobileMenuBtn');
    const closeBtn = document.getElementById('closeMobileMenuBtn');
    const sidebar = document.getElementById('mobileSidebar');
    const overlay = document.getElementById('mobileOverlay');

    if (!menuBtn || !sidebar) return;

    function toggleMenu() {
        sidebar.classList.toggle('active');
        overlay.classList.toggle('active');
        document.body.classList.toggle('overflow-hidden');
    }

    menuBtn.addEventListener('click', toggleMenu);
    if (closeBtn) closeBtn.addEventListener('click', toggleMenu);
    if (overlay) overlay.addEventListener('click', toggleMenu);
}

/**
 * Universal Table Wrapping
 * Finds all tables and wraps them in a scrollable div if not already wrapped.
 */
function wrapTables() {
    const tables = document.querySelectorAll('table');
    tables.forEach(table => {
        if (!table.parentElement.classList.contains('table-responsive')) {
            const wrapper = document.createElement('div');
            wrapper.className = 'table-responsive shadow-sm border border-gray-100 dark:border-gray-800';
            table.parentNode.insertBefore(wrapper, table);
            wrapper.appendChild(table);
        }
    });
}

/**
 * Button Optimization
 * Adds mobile-full class to buttons that should stretch on small screens.
 */
function optimizeButtons() {
    // Find common buttons like Submit, Search, Filter
    const selectors = [
        '#filterBtnGroup button',
        '.modal button',
        '#globalShowAnsToggle',
        'button[type="submit"]',
        'input[type="submit"]'
    ];
    
    if (window.innerWidth < 768) {
        selectors.forEach(selector => {
            document.querySelectorAll(selector).forEach(btn => {
                btn.classList.add('btn-mobile-full');
            });
        });
    }
}

/**
 * Theme Sync (Global helper)
 */
function toggleDarkMode() {
    document.documentElement.classList.toggle('dark');
    const isDark = document.documentElement.classList.contains('dark');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
}
