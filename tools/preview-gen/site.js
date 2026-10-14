/* Neuronetwrks preview site: progressive enhancement. Everything works as plain HTML without this file. */
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var rm = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var store = { get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } }, set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} } };

  /* ---- Navigation ---- */
  var burger = $('.burger'), nav = $('#nav');
  function closeNav(focus) { if (!nav || !nav.classList.contains('open')) return; nav.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); burger.setAttribute('aria-label', 'Open menu'); if (focus) burger.focus(); }
  if (burger && nav) {
    burger.addEventListener('click', function () { var o = nav.classList.toggle('open'); burger.setAttribute('aria-expanded', o); burger.setAttribute('aria-label', o ? 'Close menu' : 'Open menu'); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeNav(true); });
    document.addEventListener('click', function (e) { if (!nav.contains(e.target) && !burger.contains(e.target)) closeNav(); });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) closeNav(); });
    matchMedia('(min-width: 901px)').addEventListener('change', function () { closeNav(); });
  }

  /* ---- Reveal on scroll ---- */
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }); }, { threshold: 0, rootMargin: '0px 0px -6% 0px' });
    $$('.rv').forEach(function (el) { if (!rm && el.getBoundingClientRect().top > innerHeight) { el.classList.add('pend'); io.observe(el); } });
  }


  /* ---- Feature card: scroll-linked art and count-up numbers ---- */
  (function () {
    var cards = $$('.prog-feature, .pcard--lead'); if (!cards.length) return;
    var tick = false;
    function run() {
      tick = false;
      cards.forEach(function (c) { var r = c.getBoundingClientRect(); if (r.bottom < 0 || r.top > innerHeight) return; c.style.setProperty('--pf', ((innerHeight - r.top) / (innerHeight + r.height) * 2 - 1).toFixed(3)); });
    }
    if (!rm) { addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(run); } }, { passive: true }); run(); }
    $$('.prog-feature .meta b').forEach(function (b) {
      var n = parseInt(b.textContent, 10); if (rm || isNaN(n) || String(n) !== b.textContent.trim() || !('IntersectionObserver' in window)) return;
      var o = new IntersectionObserver(function (es) { if (!es[0].isIntersecting) return; o.disconnect(); var t0 = performance.now(); (function step(t) { var k = Math.min(1, (t - t0) / 900); b.textContent = Math.round(n * (1 - Math.pow(1 - k, 3))); if (k < 1) requestAnimationFrame(step); })(t0); }, { threshold: 0.6 });
      o.observe(b);
    });
  })();


  /* ---- Programs section: reveals, scroll-linked banner art, live loops, 3D tilt ---- */
  (function () {
    var sec = $$('.pp'); if (!sec.length) return;
    var parts = $$('.pp-head, .pp-banner, .pp-filters, .pp-grid'), loopers = $$('.pt, .pp-banner'), banners = $$('.pp-banner');
    if ('IntersectionObserver' in window && !rm) {
      var ro = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); ro.unobserve(e.target); } }); }, { threshold: 0.15 });
      parts.forEach(function (el) { ro.observe(el); });
      var lo = new IntersectionObserver(function (es) { es.forEach(function (e) { e.target.classList.toggle('live', e.isIntersecting); }); }, { threshold: 0.2 });
      loopers.forEach(function (el) { lo.observe(el); });
      /* safety net: anything already scrolled past is revealed */
      addEventListener('scroll', function () { parts.forEach(function (el) { if (!el.classList.contains('in') && el.getBoundingClientRect().top < innerHeight * 0.9) el.classList.add('in'); }); }, { passive: true });
    } else { parts.forEach(function (el) { el.classList.add('in'); }); }
    if (!rm) {
      var tick = false;
      var run = function () { tick = false; banners.forEach(function (b) { var r = b.getBoundingClientRect(); if (r.bottom < 0 || r.top > innerHeight) return; b.style.setProperty('--bp', ((innerHeight - r.top) / (innerHeight + r.height) * 2 - 1).toFixed(3)); }); };
      addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(run); } }, { passive: true }); run();
      $$('[data-count-to]').forEach(function (el) {
        var n = +el.getAttribute('data-count-to'); if (!('IntersectionObserver' in window)) return;
        var o = new IntersectionObserver(function (es) { if (!es[0].isIntersecting) return; o.disconnect(); var t0 = performance.now(); (function step(t) { var k = Math.min(1, (t - t0) / 1000); el.textContent = Math.round(n * (1 - Math.pow(1 - k, 3))); if (k < 1) requestAnimationFrame(step); })(t0); }, { threshold: 0.6 });
        o.observe(el);
      });
      if (matchMedia('(hover: hover)').matches) {
        $$('.pt').forEach(function (t) {
          t.addEventListener('pointermove', function (e) { var r = t.getBoundingClientRect(); t.classList.add('tilting'); t.style.setProperty('--mx', ((e.clientX - r.left) / r.width - 0.5).toFixed(2)); t.style.setProperty('--my', ((e.clientY - r.top) / r.height - 0.5).toFixed(2)); });
          t.addEventListener('pointerleave', function () { t.classList.remove('tilting'); t.style.setProperty('--mx', 0); t.style.setProperty('--my', 0); });
        });
      }
    }
  })();

  /* ---- Generic chip filter (programs list) ---- */
  $$('[data-filter-group]').forEach(function (g) {
    var chips = $$('[data-filter]', g), items = $$('[data-cat]', document), out = $('[data-count]');
    function apply(f, push) {
      var n = 0;
      chips.forEach(function (c) { c.setAttribute('aria-pressed', c.getAttribute('data-filter') === f ? 'true' : 'false'); });
      items.forEach(function (it) { var show = f === 'all' || it.getAttribute('data-cat') === f; it.hidden = !show; if (show && it.matches('.pcard')) n++; });
      if (out) out.textContent = (out.classList.contains('pp-count') ? '' : 'Showing ') + n + (n === 1 ? ' program' : ' programs');
      if (push && !rm) { var k = 0; items.forEach(function (it) { if (!it.hidden && it.matches('.pt')) { it.classList.remove('pt-enter'); void it.offsetWidth; it.style.setProperty('--k', k++); it.classList.add('pt-enter'); } }); }
      if (push) history.replaceState(null, '', f === 'all' ? location.pathname : '?f=' + f);
    }
    chips.forEach(function (c) { c.addEventListener('click', function () { apply(c.getAttribute('data-filter'), true); }); });
    var q = new URLSearchParams(location.search).get('f'); if (q && chips.some(function (c) { return c.getAttribute('data-filter') === q; })) apply(q, false);
  });

  /* ---- Tabs (keyboard: arrows, home, end) ---- */
  function tabKeys(list, tabs, select) {
    list.addEventListener('keydown', function (e) {
      var i = tabs.indexOf(document.activeElement); if (i < 0) return; var n = i;
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') n = (i + 1) % tabs.length; else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') n = (i - 1 + tabs.length) % tabs.length; else if (e.key === 'Home') n = 0; else if (e.key === 'End') n = tabs.length - 1; else return;
      e.preventDefault(); tabs[n].focus(); select(tabs[n]);
    });
  }

  /* ---- Curriculum: program selector + year tabs, state kept in the URL hash and storage ---- */
  var cur = $('#cur');
  if (cur) {
    var pbtn = $$('[data-prog-btn]', cur), lists = $$('[data-year-list]', cur), panels = $$('[data-panel]', cur), live = $('#cur-live');
    var st = { p: pbtn[1] ? pbtn[1].getAttribute('data-prog-btn') : pbtn[0].getAttribute('data-prog-btn'), y: 1 };
    function show(push) {
      pbtn.forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-prog-btn') === st.p ? 'true' : 'false'); });
      lists.forEach(function (l) { var on = l.getAttribute('data-year-list') === st.p; l.hidden = !on; $$('[role=tab]', l).forEach(function (t) { var s = t.getAttribute('data-year') === String(st.y); t.setAttribute('aria-selected', s); t.tabIndex = s ? 0 : -1; }); });
      panels.forEach(function (p) { p.hidden = !(p.getAttribute('data-panel') === st.p + '-' + st.y); });
      var h = '#' + st.p + '-y' + st.y; if (push) history.replaceState(null, '', h); store.set('nn.cur', st.p + '-' + st.y);
      var lab = $('[data-prog-btn="' + st.p + '"] b', cur); if (live && lab) live.textContent = lab.textContent + ', year ' + st.y + ' shown';
    }
    var m = (location.hash || '').match(/^#([a-z]+)-y(\d)$/) || (store.get('nn.cur') || '').match(/^([a-z]+)-(\d)$/);
    if (m && $('[data-prog-btn="' + m[1] + '"]', cur) && $('[data-panel="' + m[1] + '-' + m[2] + '"]', cur)) { st.p = m[1]; st.y = +m[2]; }
    pbtn.forEach(function (b) { b.addEventListener('click', function () { st.p = b.getAttribute('data-prog-btn'); st.y = 1; show(true); }); });
    lists.forEach(function (l) { var tabs = $$('[role=tab]', l); tabs.forEach(function (t) { t.addEventListener('click', function () { st.y = +t.getAttribute('data-year'); show(true); }); }); tabKeys(l, tabs, function (t) { st.y = +t.getAttribute('data-year'); show(true); }); });
    show(false);
  }

  /* ---- Projects: program and year filters, show more ---- */
  var pj = $('#pj');
  if (pj) {
    var items = $$('.pj', pj), pb = $$('[data-pj-prog]', pj), yb = $$('[data-pj-year]', pj), more = $('#pj-more'), cnt = $('#pj-count'), PAGE = 12;
    var s = { p: 'aiml', y: 'all', n: PAGE };
    function render() {
      pb.forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-pj-prog') === s.p ? 'true' : 'false'); });
      var multi = (pb.filter(function (b) { return b.getAttribute('data-pj-prog') === s.p; })[0] || {}).getAttribute ? pb.filter(function (b) { return b.getAttribute('data-pj-prog') === s.p; })[0].getAttribute('data-years') === '3' : true;
      $('#pj-years').hidden = !multi; if (!multi) s.y = 'all';
      yb.forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-pj-year') === s.y ? 'true' : 'false'); });
      var match = items.filter(function (it) { return it.getAttribute('data-p') === s.p && (s.y === 'all' || it.getAttribute('data-y') === s.y); });
      items.forEach(function (it) { it.hidden = true; });
      match.slice(0, s.n).forEach(function (it) { it.hidden = false; });
      if (more) more.hidden = match.length <= s.n;
      if (cnt) cnt.textContent = 'Showing ' + Math.min(s.n, match.length) + ' of ' + match.length + ' projects';
    }
    pb.forEach(function (b) { b.addEventListener('click', function () { s.p = b.getAttribute('data-pj-prog'); s.y = 'all'; s.n = PAGE; render(); history.replaceState(null, '', '#' + s.p); }); });
    yb.forEach(function (b) { b.addEventListener('click', function () { s.y = b.getAttribute('data-pj-year'); s.n = PAGE; render(); }); });
    if (more) more.addEventListener('click', function () { s.n += PAGE; render(); });
    var hh = (location.hash || '').slice(1); if (pb.some(function (b) { return b.getAttribute('data-pj-prog') === hh; })) s.p = hh;
    render();
  }

  /* ---- FAQ categories ---- */
  var fq = $('#faq');
  if (fq) {
    var fb = $$('[data-faq-cat]', fq), fi = $$('details[data-cat]', fq), fc = $('#faq-count');
    function fshow(c, push) {
      var n = 0; fb.forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-faq-cat') === c ? 'true' : 'false'); });
      fi.forEach(function (d) { var on = c === 'all' || d.getAttribute('data-cat') === c; d.hidden = !on; if (on) n++; });
      if (fc) fc.textContent = n + (n === 1 ? ' question' : ' questions');
      if (push) history.replaceState(null, '', c === 'all' ? location.pathname : '#' + c);
    }
    fb.forEach(function (b) { b.addEventListener('click', function () { fshow(b.getAttribute('data-faq-cat'), true); }); });
    var fh = (location.hash || '').slice(1); fshow(fb.some(function (b) { return b.getAttribute('data-faq-cat') === fh; }) ? fh : 'all', false);
  }

  /* ---- Contact form: validation with associated errors ---- */
  var form = $('#enq');
  if (form) {
    var f = { name: $('#f-name'), email: $('#f-email'), prog: $('#f-prog'), consent: $('#f-consent') };
    var labels = { name: 'Your name', email: 'Email', prog: 'Program', consent: 'Consent' };
    var sum = $('#err-sum'), send = $('#send'), under = $('#under');
    function set(k, msg) { var el = f[k], m = $('#m-' + k); m.textContent = msg; m.className = 'msg' + (msg ? ' e' : ''); if (msg) el.setAttribute('aria-invalid', 'true'); else el.removeAttribute('aria-invalid'); }
    function check() {
      var errs = [];
      if (!f.name.value.trim()) errs.push(['name', 'Enter your name.']);
      if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(f.email.value.trim())) errs.push(['email', 'Enter a full email address, for example name@example.com.']);
      if (!f.prog.value) errs.push(['prog', 'Choose the program you are asking about.']);
      if (!f.consent.checked) errs.push(['consent', 'Tick the box so we can reply to your enquiry.']);
      Object.keys(f).forEach(function (k) { set(k, ''); }); errs.forEach(function (e) { set(e[0], e[1]); });
      return errs;
    }
    function summary(errs) {
      if (!errs.length) { sum.hidden = true; sum.innerHTML = ''; return; }
      sum.hidden = false; sum.innerHTML = '<h2 class="h4" style="font-size:1.05rem">Please fix ' + errs.length + (errs.length === 1 ? ' thing' : ' things') + ' to send your enquiry</h2><ul>' + errs.map(function (e) { return '<li><a href="#f-' + e[0] + '">' + labels[e[0]] + ': ' + e[1] + '</a></li>'; }).join('') + '</ul>';
    }
    ['name', 'email', 'prog'].forEach(function (k) { f[k].addEventListener('blur', function () { if (f[k].value || f[k].getAttribute('aria-invalid')) check(); }); });
    $$('input[name=role]', form).forEach(function (r) { r.addEventListener('change', function () { var u = r.checked && r.value === 'under'; if (r.checked) { under.hidden = !u; send.disabled = u; send.setAttribute('aria-disabled', u); } }); });
    form.addEventListener('submit', function (e) { e.preventDefault(); var errs = check(); summary(errs); if (errs.length) { sum.setAttribute('tabindex', '-1'); sum.focus(); return; } var v = function (id) { var el = document.getElementById(id); return el ? el.value.trim() : ''; };
      var role = (form.querySelector('input[name=role]:checked') || {}).value || '';
      var body = 'Name: ' + v('f-name') + '\nEmail: ' + v('f-email') + '\nPhone: ' + v('f-phone') + '\nProgram: ' + v('f-prog') + '\nI am: ' + role + '\n\n' + v('f-msg');
      window.location.href = 'mailto:Hussain@neuronetwrks.com?subject=' + encodeURIComponent('Website enquiry') + '&body=' + encodeURIComponent(body);
      form.hidden = true; var ok = $('#ok'); ok.classList.add('show'); ok.setAttribute('tabindex', '-1'); ok.focus(); });
    var qs = new URLSearchParams(location.search); if (qs.get('topic') === 'fees' && $('#f-msg') && !$('#f-msg').value) { $('#f-msg').value = 'I would like to know the fees for: '; }
    $('#again').addEventListener('click', function () { form.reset(); form.hidden = false; $('#ok').classList.remove('show'); under.hidden = true; send.disabled = false; f.name.focus(); });
  }

  /* ---- Staircase (3D, lazy) with still fallback ---- */
  var run = !rm && !(navigator.connection && navigator.connection.saveData) && (navigator.hardwareConcurrency || 8) > 4 && (navigator.deviceMemory || 8) > 4;
  var cans = $$('canvas[data-stack]');
  if (run && cans.length) {
    var go = function () {
      var sc = document.createElement('script'); sc.src = '/assets/module-stack.js';
      sc.onload = function () {
        var MS = window.ModuleStack; var H = {};
        cans.forEach(function (c, i) { try { var h = MS.mount(c, JSON.parse(c.getAttribute('data-stack'))); H[c.id || 'c' + i] = h; c.style.opacity = 1; var p = c.previousElementSibling; if (p && p.tagName === 'IMG') setTimeout(function () { p.style.opacity = 0; }, 400); } catch (e) {} });
        var hero = H.heroStair, tags = $$('.lab-tag');
        if (hero && tags.length) { var n = 0; setInterval(function () { n = (n + 1) % tags.length; hero.setProgress((n + 1) / tags.length); tags.forEach(function (t, k) { t.classList.toggle('on', k === n); }); }, 2200); }
        var sp = H.heroStair; if (sp) addEventListener('scroll', function () { sp.setProgress(0.2 + Math.min(1, (scrollY || 0) / 900) * 0.6); }, { passive: true });
      };
      document.head.appendChild(sc);
    };
    ('requestIdleCallback' in window) ? requestIdleCallback(go, { timeout: 2500 }) : setTimeout(go, 1200);
  }
  /* Path diagram: highlight steps in turn when visible */
  var path = $('.path');
  if (path && !rm && 'IntersectionObserver' in window) {
    var li = $$('li', path), k = 0, t;
    new IntersectionObserver(function (es) { if (es[0].isIntersecting) { if (!t) t = setInterval(function () { li.forEach(function (x, j) { x.classList.toggle('on', j === k); }); k = (k + 1) % li.length; }, 1600); } else { clearInterval(t); t = null; } }).observe(path);
  }
})();
