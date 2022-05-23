// scroll to the top of the screen
var goUpBtn = document.getElementById("go-up-btn");

function goUpFunction() {
  gsap.to(window, { duration: 1, scrollTo: 0 });
}
