/* 设计方案 B / C / D 共用交互（轻量、渐进增强）
   - 汉堡菜单：<button data-navtoggle>…<div data-drawer>
   - 滚动入场：<div data-reveal>
   - 年份：<span data-year>
   - 数值滚动：<span data-count="20000" data-suffix="+">
   - 图表入场：<svg data-chart> 内的 [data-bar] 在可见后生长
   说明：三套方案各自独立 CSS，互不影响。 */
(function () {
  "use strict";

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* 汉堡菜单 */
  document.querySelectorAll("[data-navtoggle]").forEach(function (btn) {
    var drawer = document.querySelector("[data-drawer]");
    if (!drawer) return;
    var set = function (open) {
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      drawer.classList.toggle("is-open", open);
      document.body.classList.toggle("is-locked", open);
      document.body.classList.toggle("b-locked", open);
    };
    btn.addEventListener("click", function () {
      set(btn.getAttribute("aria-expanded") !== "true");
    });
    drawer.addEventListener("click", function (e) {
      if (e.target.closest("a")) set(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        set(false);
        btn.focus();
      }
    });
    window.addEventListener("resize", function () {
      if (window.innerWidth >= 900) set(false);
    });
  });

  /* 年份 */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  /* 滚动入场 */
  var revealEls = document.querySelectorAll("[data-reveal]");
  if (revealEls.length && "IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) {
            en.target.classList.add("is-in");
            io.unobserve(en.target);
          }
        });
      },
      { rootMargin: "0px 0px -6% 0px", threshold: 0.06 }
    );
    revealEls.forEach(function (el) {
      io.observe(el);
    });
  } else {
    revealEls.forEach(function (el) {
      el.classList.add("is-in");
    });
  }

  /* 图表入场：为柱状/进度元素加上生长动画 */
  var charts = document.querySelectorAll("[data-chart]");
  if (charts.length && "IntersectionObserver" in window && !reduce) {
    var io2 = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) {
            en.target.classList.add("is-grown");
            io2.unobserve(en.target);
          }
        });
      },
      { threshold: 0.25 }
    );
    charts.forEach(function (el) {
      io2.observe(el);
    });
  } else {
    charts.forEach(function (el) {
      el.classList.add("is-grown");
    });
  }

  /* 数值滚动 */
  var counters = document.querySelectorAll("[data-count]");
  if (counters.length && "IntersectionObserver" in window && !reduce) {
    var io3 = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (en) {
          if (!en.isIntersecting) return;
          var el = en.target;
          io3.unobserve(el);
          var target = parseFloat(el.getAttribute("data-count"));
          var suffix = el.getAttribute("data-suffix") || "";
          var start = performance.now();
          var dur = 1000;
          var step = function (now) {
            var p = Math.min(1, (now - start) / dur);
            var eased = 1 - Math.pow(1 - p, 3);
            el.textContent = Math.round(target * eased).toLocaleString("en-US") + suffix;
            if (p < 1) requestAnimationFrame(step);
          };
          requestAnimationFrame(step);
        });
      },
      { threshold: 0.5 }
    );
    counters.forEach(function (el) {
      io3.observe(el);
    });
  }
})();
