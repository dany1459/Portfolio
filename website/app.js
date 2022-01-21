const header = document.querySelector(".header-main");

const tl = new TimelineMax();
tl.fromTo(header, 1, {height:"0%"}, {height: "80"})
