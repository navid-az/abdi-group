var navOptions = document.querySelectorAll("#navbar > ul li");
var navOptionsHexa = document.querySelectorAll("#navbar > ul li > img");
var hamburgerBtn = document.getElementById("mobile-menu-btn");
var closeMenuBtn = document.getElementById("close-menu-btn");
var goBackBtn = document.getElementById("go-back-btn");
var mobileMenu = document.getElementById("mobile-menu");
var menuBtns = document.getElementById("menu__btns");

var menuList = document.getElementById("menu-list");
var menuSubList = document.getElementById("menu-sub-list"); //this menu is under menu list
var menuSubListSub = document.getElementById("menu-sub-list-sub"); // this menu is under sub list

var menuListOpts = document.querySelectorAll("#menu-list li");
var menuSubListOpts = document.querySelectorAll("#menu-sub-list li");
var menuSubListSubOptsUl = document.querySelectorAll("#menu-sub-list-sub ul");
var menuSubListSubOptsLi = document.querySelectorAll(
  "#menu-sub-list-sub ul li"
);
var child = 0;
let goBack = false;
let goTo = "go to mainMenu";

var products = document.getElementById("products");

const timeline = gsap.timeline({ defaults: { duration: 0.4 } });

for (var i = 0; i < navOptions.length; i++) {
  navOptions[i].addEventListener("mouseover", navOptionHoverOn);
  navOptions[i].addEventListener("mouseout", navOptionHoverOff);
}
function navOptionHoverOn() {
  this.children[0].style.transform = " scale(1)";
  this.children[1].style.color = "#89C958";
}
function navOptionHoverOff() {
  this.children[0].style.transform = "scale(0)";
  this.children[1].style.color = "#FFFFFF";
}

// hamburger btn and mobile menu

hamburgerBtn.addEventListener("click", menuBtnClickHandle);
closeMenuBtn.addEventListener("click", menuCloseBtnClickHandle);
products.addEventListener("click", productsMenuOpen);

function menuBtnClickHandle() {
  mobileMenu.style.display = "flex";
  setTimeout(() => {
    mobileMenu.style.right = "0px";
    mobileMenu.style.position = "fixed";
  }, 200);
  hamburgerBtn.style.opacity = "0";

  setTimeout(() => {
    closeMenuBtn.style.opacity = "1";
  }, 300);
  timeline.from("#menu-list li ", {
    opacity: 0,
    x: "-200%",
    stagger: 0.08,
    delay: 0.4,
  });
  menuList.style.display = "flex";
}
function menuCloseBtnClickHandle() {
  mobileMenu.style.right = "-100%";
  mobileMenu.style.position = "fixed";
  hamburgerBtn.style.opacity = "1";
  closeMenuBtn.style.opacity = "0";
  goBackBtn.style.opacity = "0";

  timeline.to("#menu-list li ", {
    opacity: 1,
    x: "0%",
  });
  gsap.to("#menu-sub-list li ", {
    opacity: 1,
    x: "0%",
    stagger: 0.08,
    delay: 0.1,
  });

  menuListOpts.forEach((i) => {
    i.style.display = "flex";
  });
  menuSubListOpts.forEach((i) => {
    i.style.display = "none";
  });
  menuSubList.style.display = "none";
  menuSubListSub.style.display = "none";
  menuSubListSubOptsUl.forEach((i) => {
    i.style.display = "none";
  });
  setTimeout(() => {
    mobileMenu.style.display = "none";
  }, 300);
}

// products and services list will open up
function productsMenuOpen() {
  goBackBtn.style.display = "flex";
  menuBtns.style.justifyContent = "space-between";
  timeline.to("#menu-list li ", {
    opacity: 0,
    x: "200%",
    stagger: 0.08,
    delay: 0.08,
  });
  setTimeout(() => {
    menuList.style.display = "none";
    menuSubList.style.display = "flex";
    menuSubListOpts.forEach((i) => {
      i.style.display = "flex";
    });
    goBackBtn.style.opacity = "1";
  }, 400);
  gsap.from("#menu-sub-list li", {
    opacity: 0,
    x: "-200%",
    stagger: 0.08,
    delay: 0.1,
  });
  if (goBack == true) {
    gsap.to("#menu-sub-list > li", {
      opacity: 1,
      x: "0%",
      stagger: 0.08,
      delay: 0.1,
    });
    goBack = false;
  }
  goTo = "go to mainMenu";
  console.log(goBack);
}
function changeSubMenu() {
  var child = 0;
  while (true) {
    if (child <= 5) {
      menuSubListSubOptsLi[child].style.display = "none";
    } else {
      menuSubListSubOptsLi[child].style.display = "flex";
    }
    child++;
  }
}

// This will open subMenuSub
function openSubMenuSub(x) {
  gsap.to("#menu-sub-list li ", {
    opacity: 0,
    x: "200%",
    stagger: 0.08,
    delay: 0.1,
  });
  setTimeout(() => {
    menuSubList.style.display = "none";
    menuSubListSub.style.display = "flex";
    menuSubListSubOptsLi.forEach((i) => {
      i.style.display = "flex";
    });
    menuSubListSubOptsUl[x].style.display = "flex";
    while (true) {
      if (child <= 5) {
        menuSubListSubOptsLi[child].style.display = "flex";
      } else if (child > 5) {
        menuSubListSubOptsLi[child].style.display = "none";
      }
      child++;
    }
  }, 500);
  gsap.from("#menu-sub-list-sub ul > li", {
    opacity: 0,
    x: "-200%",
    delay: 0.25,
    stagger: 0.05,
  });
  // gsap.to("#menu-sub-list-sub ul > li", {
  //   opacity: 1,
  //   x: "0%",
  //   delay: 0.25,
  //   stagger: 0.05,
  // });
  menuSubListSubOptsUl.forEach((i) => {
    i.style.display = "none";
  });
  if (goBack == true) {
    gsap.to("#menu-sub-list-sub ul > li", {
      opacity: 1,
      x: "0%",
      stagger: 0.08,
      delay: 0.1,
    });
    goBack = false;
    console.log("this is working");
  }
  goTo = "go to subMenu";
  console.log(goTo);
}

function goBackBtnF() {
  goBack = true;
  if (goTo == "go to mainMenu") {
    timeline.to("#menu-list li ", {
      opacity: 1,
      x: "0%",
      stagger: 0.08,
      delay: 0.08,
    });
    setTimeout(() => {
      menuList.style.display = "flex";
      menuSubList.style.display = "none";
      menuSubListOpts.forEach((i) => {
        i.style.display = "none";
        goBackBtn.style.opacity = "0";
      });
    }, 400);
    gsap.to("#menu-sub-list li", {
      opacity: 0,
      x: "-200%",
      stagger: 0.08,
      delay: 0.1,
    });
  } else if (goTo == "go to subMenu") {
    console.log("this should be the sub menu");

    gsap.to("#menu-sub-list li ", {
      opacity: 1,
      x: "0%",
      stagger: 0.08,
      delay: 0.08,
    });
    setTimeout(() => {
      menuSubList.style.display = "flex";
      menuSubListSub.style.display = "none";
      menuSubListSubOptsLi.forEach((i) => {
        i.style.display = "none";
      });
    }, 400);
    gsap.to("#menu-sub-list-sub ul li", {
      opacity: 0,
      x: "-200%",
      stagger: 0.08,
      delay: 0.1,
    });
    goTo = "go to mainMenu";
  }

  console.log(goBack);
  console.log(goTo);
}
