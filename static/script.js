document.addEventListener("DOMContentLoaded", function () {
  function addRedirectListener(buttonId) {
    const btn = document.getElementById(buttonId);
    if (btn) {
      btn.addEventListener("click", function () {
        window.location.href = btn.dataset.url;
      });
    }
  }

  addRedirectListener("back-to-login-btn");
  addRedirectListener("create-ticket-btn");
  addRedirectListener("edit-ticket-btn");
  addRedirectListener("delete-ticket-btn");
  addRedirectListener("ticket-cancel-btn");
});