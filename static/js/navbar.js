var navList = document.getElementById("navlist");
var desktopNavListUl = document.getElementById("desktop-nav-list-ul");
var desktopNavListLi = document.getElementById("desktop-nav-list-li");
var navListCrossBtn = document.getElementById("nav-list-cross-btn");
var desktopNavListHexa = document.getElementById("desktop-nav-list-hexa");
var desktopNavListStatus = "close";
var navListBtns = document.querySelectorAll(".desktop-nav-list-li h2");
var desktopNavListOptionsWrapper = document.querySelectorAll(
  ".desktop-nav-list-options-wrapper"
);

var url = window.location.toString();

// navbar opening and closing function
function openDesktopNavList(navListNum) {
  navListBtns.forEach((i) => {
    i.style.transform = "translateX(0%)";
    i.style.color = "#FFFFFF";
  });
  navListBtns[navListNum].style.color = "#89c958";
  navListBtns[navListNum].style.transform = "translateX(3%)";
  desktopNavListOptionsWrapper.forEach((i) => {
    gsap.to(i, {
      opacity: 0,
      delay: 0.3,
    });
  });
  setTimeout(() => {
    desktopNavListOptionsWrapper.forEach((i) => {
      i.style.display = "none";
    });
    desktopNavListOptionsWrapper[navListNum].style.display = "flex";
  }, 400);
  gsap.to(desktopNavListOptionsWrapper[navListNum], {
    opacity: 1,
    delay: 0.3,
  });
}
function NavListClickHandler() {
  if (desktopNavListStatus == "close") {
    openDesktopNavList(0);
    desktopNavListHexa.style.display = "block";
    gsap.to("#nav-list-cross-btn, #desktop-nav-list-hexa", {
      opacity: 1,
      x: "0%",
      delay: 0.3,
    });
    if (url.includes("/en")) {
      gsap.to(".desktop-nav-list-options-wrapper", {
        x: "-5%",
        delay: 0.3,
      });
      gsap.to("#desktop-nav-list-ul", {
        opacity: 1,
        x: "20%",
        delay: 0.3,
      });
    } else if (url.includes("/fa")) {
      gsap.to(".desktop-nav-list-options-wrapper", {
        x: "5%",
        delay: 0.3,
      });
      gsap.to("#desktop-nav-list-ul", {
        opacity: 1,
        x: "-20%",
        delay: 0.3,
      });
    }
    navList.style.display = "flex";

    setTimeout(() => {
      navList.style.height = "30rem";
      navList.style.opacity = "1";
    }, 50);

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
    setTimeout(() => {
      navList.style.opacity = "0";
      navList.style.display = "none";
    }, 1000);
    desktopNavListStatus = "close";
  }
}

// stick navbar to the top of the screen
var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;

window.onscroll = function () {
  stickyNavBar();
};
function stickyNavBar() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky");
    navbar.style.width = "85%";
  } else {
    navbar.classList.remove("sticky");
    navbar.style.width = "94%";
    navbar.style.background = "#00006A";
    navlist.style.background = "#00006A";
  }
}
