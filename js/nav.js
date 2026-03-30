// T&Q Lab Guide — Navigation & Language Switcher

document.addEventListener('DOMContentLoaded', function () {

  // Mark active nav link based on current page filename
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-link').forEach(link => {
    const href = link.getAttribute('href').split('/').pop();
    if (href === currentPage) {
      link.classList.add('active');
    }
  });

  // Mobile hamburger toggle
  const hamburger = document.getElementById('hamburger');
  const sidebar = document.querySelector('.sidebar');
  if (hamburger && sidebar) {
    hamburger.addEventListener('click', () => sidebar.classList.toggle('open'));
  }

  // Language switcher
  const langSelect = document.getElementById('lang-select');
  if (langSelect) {
    // Detect current language from path
    const pathParts = window.location.pathname.split('/');
    const langIndex = pathParts.indexOf('docs') + 1;
    const currentLang = (langIndex > 0 && pathParts[langIndex] && pathParts[langIndex].length === 2)
      ? pathParts[langIndex]
      : 'en';
    langSelect.value = currentLang;

    langSelect.addEventListener('change', function () {
      const selectedLang = this.value;
      const currentPath = window.location.pathname;
      const fileName = currentPath.split('/').pop() || '00-overview.html';

      let newPath;
      if (selectedLang === 'en') {
        // Navigate to English (no lang subfolder)
        newPath = currentPath.replace(/\/docs\/[a-z]{2}\//, '/docs/');
      } else {
        // Navigate to language subfolder
        if (currentPath.includes('/docs/') && !currentPath.match(/\/docs\/[a-z]{2}\//)) {
          newPath = currentPath.replace('/docs/', `/docs/${selectedLang}/`);
        } else {
          newPath = currentPath.replace(/\/docs\/[a-z]{2}\//, `/docs/${selectedLang}/`);
        }
      }

      window.location.href = newPath;
    });
  }

});
