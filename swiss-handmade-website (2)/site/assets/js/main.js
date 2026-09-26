// [BRAND_NAME] — main.js (vanilla, no dependencies)

document.addEventListener('DOMContentLoaded', function () {

  /* ---------- Mobile nav toggle ---------- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.style.overflow = open ? 'hidden' : '';
    });
    nav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });
  }

  /* ---------- Magnete: Filter nach Stadt/Region + Suche ---------- */
  var filterRow = document.querySelector('[data-filter-chips]');
  var searchInput = document.querySelector('[data-filter-search]');
  var cards = document.querySelectorAll('[data-product-card]');

  function applyFilters() {
    var activeChip = filterRow ? filterRow.querySelector('[aria-pressed="true"]') : null;
    var activeGroup = activeChip ? activeChip.dataset.group : 'all';
    var query = searchInput ? searchInput.value.trim().toLowerCase() : '';

    cards.forEach(function (card) {
      var group = card.dataset.group || '';
      var name = (card.dataset.name || '').toLowerCase();
      var matchesGroup = activeGroup === 'all' || group === activeGroup;
      var matchesQuery = query === '' || name.indexOf(query) !== -1;
      card.style.display = (matchesGroup && matchesQuery) ? '' : 'none';
    });
  }

  if (filterRow) {
    filterRow.querySelectorAll('.filter-chip').forEach(function (chip) {
      chip.addEventListener('click', function () {
        filterRow.querySelectorAll('.filter-chip').forEach(function (c) {
          c.setAttribute('aria-pressed', 'false');
        });
        chip.setAttribute('aria-pressed', 'true');
        applyFilters();
      });
    });
  }
  if (searchInput) {
    searchInput.addEventListener('input', applyFilters);
  }

  /* ---------- Produktseite: Galerie-Thumbnails ---------- */
  var mainImg = document.querySelector('[data-gallery-main] img');
  var thumbs = document.querySelectorAll('[data-gallery-thumb]');
  thumbs.forEach(function (btn) {
    btn.addEventListener('click', function () {
      if (!mainImg) return;
      mainImg.src = btn.dataset.fullSrc;
      mainImg.alt = btn.dataset.fullAlt || mainImg.alt;
      thumbs.forEach(function (b) { b.setAttribute('aria-current', 'false'); });
      btn.setAttribute('aria-current', 'true');
    });
  });

  /* ---------- Formulare: Kontakt & Grosshandel (Demo, kein Backend) ---------- */
  document.querySelectorAll('form[data-demo-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var success = form.querySelector('.form-success');
      if (success) {
        success.classList.add('is-visible');
        success.setAttribute('tabindex', '-1');
        success.focus();
      }
      form.reset();
    });
  });

});
