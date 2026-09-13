/* Mouseion 慕识书院 — 站点交互
   1) 顶栏状态  2) 移动端导航抽屉  3) 滚动入场
   4) 成长路径切换（书塔逐级点亮）  5) 图集灯箱  6) 年份
   全部交互均为渐进增强：禁用 JS 时内容仍可阅读。 */
(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- 1. 顶栏滚动态 ---------- */
  var header = document.querySelector(".siteheader");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-stuck", window.scrollY > 8);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---------- 2. 移动端导航抽屉 ---------- */
  var toggle = document.querySelector(".navtoggle");
  var drawer = document.getElementById("drawer");
  if (toggle && drawer) {
    var setOpen = function (open) {
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      drawer.classList.toggle("is-open", open);
      document.body.classList.toggle("is-locked", open);
      if (open) {
        var first = drawer.querySelector("a");
        if (first && window.matchMedia("(min-width: 900px)").matches === false) first.focus();
      }
    };
    toggle.addEventListener("click", function () {
      setOpen(toggle.getAttribute("aria-expanded") !== "true");
    });
    drawer.addEventListener("click", function (e) {
      if (e.target.closest("a")) setOpen(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && drawer.classList.contains("is-open")) {
        setOpen(false);
        toggle.focus();
      }
    });
    window.addEventListener("resize", function () {
      if (window.innerWidth >= 900 && drawer.classList.contains("is-open")) setOpen(false);
    });
  }

  /* ---------- 3. 滚动入场 ---------- */
  var reveals = document.querySelectorAll(".reveal");
  if (reveals.length && "IntersectionObserver" in window && !reduceMotion) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) {
            en.target.classList.add("is-in");
            io.unobserve(en.target);
          }
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.08 }
    );
    reveals.forEach(function (el) {
      io.observe(el);
    });
  } else {
    reveals.forEach(function (el) {
      el.classList.add("is-in");
    });
  }

  /* ---------- 4. 成长路径切换 + 书塔点亮 ---------- */
  var stageRoot = document.querySelector("[data-stage-root]");
  if (stageRoot) {
    var tabs = Array.prototype.slice.call(stageRoot.querySelectorAll("[data-stage-tab]"));
    var panels = Array.prototype.slice.call(stageRoot.querySelectorAll("[data-stage-panel]"));
    var steps = Array.prototype.slice.call(document.querySelectorAll("[data-tower-step]"));
    var labels = Array.prototype.slice.call(document.querySelectorAll("[data-tower-label]"));
    var nodes = Array.prototype.slice.call(document.querySelectorAll("[data-path-node]"));

    var select = function (idx, focusPanel) {
      tabs.forEach(function (t, i) {
        t.setAttribute("aria-selected", i === idx ? "true" : "false");
        t.tabIndex = i === idx ? 0 : -1;
      });
      panels.forEach(function (p, i) {
        p.hidden = i !== idx;
      });
      steps.forEach(function (s, i) {
        s.classList.toggle("is-lit", i <= idx);
        s.classList.toggle("is-dim", i === idx);
      });
      labels.forEach(function (l, i) {
        l.classList.toggle("is-on", i <= idx);
      });
      nodes.forEach(function (n, i) {
        n.classList.toggle("is-on", i <= idx);
      });
      if (focusPanel) {
        var head = panels[idx] && panels[idx].querySelector("h3");
        if (head) head.focus({ preventScroll: true });
      }
    };

    tabs.forEach(function (t, i) {
      t.addEventListener("click", function () {
        select(i);
      });
      t.addEventListener("keydown", function (e) {
        var next = null;
        if (e.key === "ArrowRight") next = (i + 1) % tabs.length;
        if (e.key === "ArrowLeft") next = (i - 1 + tabs.length) % tabs.length;
        if (e.key === "Home") next = 0;
        if (e.key === "End") next = tabs.length - 1;
        if (next !== null) {
          e.preventDefault();
          select(next);
          tabs[next].focus();
        }
      });
    });

    var initial = tabs.findIndex(function (t) {
      return t.getAttribute("aria-selected") === "true";
    });
    select(initial < 0 ? 0 : initial);
  }

  /* ---------- 5. 图集灯箱 ---------- */
  var zoomables = document.querySelectorAll("[data-zoom]");
  if (zoomables.length && typeof HTMLDialogElement !== "undefined") {
    var dlg = document.createElement("dialog");
    dlg.className = "lightbox";
    dlg.innerHTML =
      '<form method="dialog"><button class="lightbox__close" aria-label="关闭">×</button></form>' +
      '<figure class="lightbox__fig"><img alt=""><figcaption></figcaption></figure>';
    document.body.appendChild(dlg);
    var dlgImg = dlg.querySelector("img");
    var dlgCap = dlg.querySelector("figcaption");
    zoomables.forEach(function (el) {
      el.addEventListener("click", function (e) {
        var img = el.querySelector("img");
        if (!img) return;
        e.preventDefault();
        dlgImg.src = img.currentSrc || img.src;
        dlgImg.alt = img.alt || "";
        dlgCap.textContent = el.getAttribute("data-caption") || "";
        dlg.showModal();
      });
    });
    dlg.addEventListener("click", function (e) {
      if (e.target === dlg) dlg.close();
    });
  }

  /* ---------- 6. 年份 ---------- */
  var y = document.querySelector("[data-year]");
  if (y) y.textContent = String(new Date().getFullYear());
})();
