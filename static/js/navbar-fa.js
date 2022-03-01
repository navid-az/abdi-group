var navList = document.getElementById("navlist");
var desktopNavListUl = document.getElementById("desktop-nav-list-ul");
var desktopNavListLi = document.getElementById("desktop-nav-list-li");
var navListCrossBtn = document.getElementById("nav-list-cross-btn");
var desktopNavListHexa = document.getElementById("desktop-nav-list-hexa");
var desktopNavListStatus = "close";

function NavListClickHandler() {
  if (desktopNavListStatus == "close") {
    openDesktopNavList(0);
    desktopNavListHexa.style.display = "block";
    gsap.to("#nav-list-cross-btn, #desktop-nav-list-hexa", {
      opacity: 1,
      x: "0%",
      delay: 0.3,
    });
    gsap.to(".desktop-nav-list-options-wrapper", {
      x: "5%",
      delay: 0.3,
    });
    gsap.to("#desktop-nav-list-ul", {
      opacity: 1,
      x: "-20%",
      delay: 0.3,
    });
    navList.style.height = "30rem";
    desktopNavListStatus = "open";
  } else if (desktopNavListStatus == "open") {
    navListCrossBtn.style.opacity = "0";
    desktopNavListHexa.style.display = "none";
    gsap.to(
      "#desktop-nav-list-ul, #desktop-nav-list-hexa, .desktop-nav-list-options-wrapper",
      {
        opacity: 0,
        x: "0%",
      }
    );
    setTimeout(() => {
      navList.style.height = "0rem";
    }, 500);
    desktopNavListStatus = "close";
  }
}
