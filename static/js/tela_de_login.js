var btnSignin = document.querySelector("#signin");
var btnSigup = document.querySelector("#sigup");
var body = document.querySelector("body")

btnSignin.addEventListener("click", function () {
    body.className = "sign-in-js"
});

btnSigup.addEventListener("click", function () {
    body.className = "sign-up-js"
});