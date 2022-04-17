var valuesLogo = document.getElementById("values-logo");

if (valuesLogo.offsetWidth >= 200) {
  gsap.to("#value-1-fa,#value-1", {
    scrollTrigger: {
      trigger: ".founder-card-img",
      toggleActions: "restart restart none none",
    },
    opacity: 1,
    delay: 0.5,
    left: "-5rem",
    bottom: "-9rem",
  });
  gsap.to("#value-2-fa,#value-2", {
    scrollTrigger: {
      trigger: ".founder-card-img",
      toggleActions: "restart restart none none",
    },
    opacity: 1,
    delay: 0.5,
    left: "-10rem",
  });
  gsap.to("#value-3-fa,#value-3", {
    scrollTrigger: {
      trigger: ".founder-card-img",
      toggleActions: "restart restart none none",
    },
    opacity: 1,
    delay: 0.5,
    left: "-5rem",
    top: "-9rem",
  });
  gsap.to("#value-4-fa,#value-4", {
    scrollTrigger: {
      trigger: ".founder-card-img",
      toggleActions: "restart restart none pause",
    },
    opacity: 1,
    delay: 0.5,
    left: "5rem",
    top: "-9rem",
  });
  gsap.to("#value-5-fa,#value-5", {
    scrollTrigger: {
      trigger: ".founder-card-img",
      toggleActions: "restart restart none none",
    },
    opacity: 1,
    delay: 0.5,
    right: "-10rem",
  });
  gsap.to("#value-6-fa,#value-6", {
    scrollTrigger: {
      trigger: ".founder-card-img",
      toggleActions: "restart restart none none",
    },
    opacity: 1,
    delay: 0.5,
    left: "5rem",
    bottom: "-9rem",
  });
} else if (valuesLogo.offsetWidth <= 200) {
  gsap.to("#value-1-fa,#value-1", {
    scrollTrigger: {
      trigger: ".values-text",
      toggleActions: "restart restart none none",
    },
    opacity: 1,
    delay: 0.5,
    left: "-3rem",
    bottom: "-5.3rem",
  });
  gsap.to("#value-2-fa,#value-2", {
    scrollTrigger: {
      trigger: ".values-text",
      toggleActions: "restart restart none none",
    },
    opacity: 1,
    delay: 0.5,
    left: "-6.2rem",
  });
  gsap.to("#value-3-fa,#value-3", {
    scrollTrigger: {
      trigger: ".values-text",
      toggleActions: "restart restart none none",
    },
    opacity: 1,
    delay: 0.5,
    left: "-3rem",
    top: "-5.3rem",
  });
  gsap.to("#value-4-fa,#value-4", {
    scrollTrigger: {
      trigger: ".values-text",
      toggleActions: "restart restart none none",
    },
    opacity: 1,
    delay: 0.5,
    right: "-3rem",
    top: "-5.3rem",
  });
  gsap.to("#value-5-fa,#value-5", {
    scrollTrigger: {
      trigger: ".values-text",
      toggleActions: "restart restart none none",
    },
    opacity: 1,
    delay: 0.5,
    right: "-6.2rem",
  });
  gsap.to("#value-6-fa,#value-6", {
    scrollTrigger: {
      trigger: ".values-text",
      toggleActions: "restart restart none none",
    },
    opacity: 1,
    delay: 0.5,
    right: "-3rem",
    bottom: "-5.3rem",
  });
}
