const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");
const loginSuccessMsg = document.getElementById("login-success-msg");

loginButton.addEventListener("click", (e) => {
  e.preventDefault();
  const username = loginForm.username.value;
  const password = loginForm.password.value;

  if (username === "user" && password === "web_dev") {
    loginSuccessMsg.style.opacity = 1;
  } else {
    loginErrorMsg.style.opacity = 1;
  }
});

function validateCode() {
  var code = document.getElementById("submit").value;

  if (username === "user" && password === "web_dev") {
    window.location.href = "./main.html";
  }
}
