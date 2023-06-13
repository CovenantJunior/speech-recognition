const play = $('#play');
const speak = $('#speak');
const text = $('#text');

const synthesis = window.speechSynthesis;

play.on('click', () => {
    let _u = new SpeechSynthesisUtterance(text.val());
    synthesis.speak(_u);
})