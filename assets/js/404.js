(function () {
  function updateRequestedUrl() {
    var el = document.getElementById('requested-url');
    if (!el) return;

    try {
      var resolved = window.location.href || window.location.pathname || '';
      if (!resolved) return;

      el.textContent = resolved;
    } catch (error) {
      // No-op: fallback leaves placeholder text in place
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updateRequestedUrl);
  } else {
    updateRequestedUrl();
  }
})();
