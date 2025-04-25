document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById("back-to-login-btn");
    if (btn) {
      btn.addEventListener("click", function () {
        window.location.href = btn.dataset.url;
      });
    }

  });