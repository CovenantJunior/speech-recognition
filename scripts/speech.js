const play = $('#play');
const speak = $('#speak');
const text = $('#text');
const output = $('#output');

// TTS Synthesis
const synthesis = window.speechSynthesis;

play.on('click', () => {
    // Utterance
    let _u = new SpeechSynthesisUtterance(text.val());
    synthesis.speak(_u);
});


// STT Synthesis
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const _r = new SpeechRecognition();

speak.on('click', () => {
    // Recognition
    _r.start();
});

_r.onresult = (e) => {
    let transcription = e.results[0][0].transcript;
    // output.text(transcription);
    text.val(transcription);
};

_r.onerror = (e) => {
    output.text("Error: " + e.error);
};