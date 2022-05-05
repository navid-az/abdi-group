var goUpBtn = document.getElementById("go-up-btn");

function goUpFunction() {
  //scroll to 400 pixels down from the top
  gsap.to(window, { duration: 1, scrollTo: 0 });
}
