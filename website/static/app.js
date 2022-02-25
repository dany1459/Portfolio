function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST", 
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/notes";
    });
  }
  
const header = document.querySelector('.header');
const about = document.querySelector('.about');
const projects = document.querySelector('.projects');
const myname = document.querySelector('.myname');

const tl = new TimelineMax();

tl.fromTo(header, 1, {y: '-100%'}, {y: '0%', ease: Power2.easeInOut})
.fromTo(about, 1, {x: '-100%'}, {x: '0%', ease: Power2.easeInOut}, '-=1')
.fromTo(projects, 0.5, {opacity: 0, x: 30}, {opacity: 1, x: 0})
.fromTo(myname, 0.5, {opacity: 0, x: 30}, {opacity: 1, x: 0}, '-=0.5');
