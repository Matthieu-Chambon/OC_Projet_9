document.addEventListener("DOMContentLoaded", function () {
  const buttons = document.querySelectorAll("[data-url]");

  buttons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      window.location.href = btn.dataset.url;
    });
  });
});