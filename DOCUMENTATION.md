Speech Recognition App Documentation
====================================

The Speech Recognition App is a web-based application that allows users to convert speech to text and vice versa. It provides a user-friendly interface for speech input and output, making it convenient to interact with the app using voice commands.

Features
--------

-   Speech-to-Text: Users can speak into their device's microphone, and the app will transcribe the speech into text.
-   Text-to-Speech: Users can input text into the app, and it will convert the text into speech output.
-   Play Functionality: Users can play the synthesized speech to listen to the output.
-   Real-time Transcription: The app provides real-time transcription as the user speaks.
-   Easy-to-Use Interface: The interface is designed to be intuitive and user-friendly.

Installation
------------

1.  Clone the repository: `git clone https://github.com/CovenantJunior/speech-recognition.git`
2.  Open the `index.html` file in your preferred web browser.
3.  Make sure your device has a working microphone for speech input.


How speech.js Works
-------------------

The `speech.js` file is the heart and soul of the Speech Recognition App. It handles the speech-to-text (STT) and text-to-speech (TTS) functionalities with a touch of magic and a sprinkle of humor.

### TTS Synthesis

Let's dive into the TTS (Text-to-Speech) part first. When you click the "Play" button, the fun begins. The code sets up a connection with the speech synthesis engine, represented by the `window.speechSynthesis` object. This engine is responsible for converting your text into audible speech.

To get the party started, an event listener is attached to the "click" event of the "Play" button. When you click the button, a `SpeechSynthesisUtterance` object is created. This object wraps your text input and serves it as a tasty treat for the speech synthesis engine.

Once the `SpeechSynthesisUtterance` is ready, it's time to unleash the power of speech. The `speak` method of the `speechSynthesis` object is invoked, and voilà! The engine springs to life, speaking out your text with its digital vocal cords.

### STT Synthesis

Now, let's shift gears and explore the STT (Speech-to-Text) part. When you're in the mood for some interactive speech action, you click the "Speak" button, and the app listens attentively.

The magic behind the scenes is the `SpeechRecognition` object. It's like an eager listener, waiting to transcribe your spoken words into written text. This object is smart enough to adapt to different browser environments, supporting both the standard `SpeechRecognition` and the `webkitSpeechRecognition` for older browsers.

Once the "Speak" button is clicked, an event listener is triggered, and the `start` method of the `SpeechRecognition` object is called. This starts the listening process, capturing your voice with the device's microphone.

When you finish speaking, the `onresult` event fires up, revealing the transcribed treasure hidden within the captured audio. The code fetches the transcription from the event results and updates the app's output area with your spoken words.

But what if something goes wrong? Fear not! The code is prepared for that too. The `onerror` event is there to catch any mishaps during the speech recognition process. If an error occurs, a friendly error message is displayed in the app's output area, making sure you know that technology has its quirky moments too.

Make sure to include these dependencies in your project for the app to function properly.

Credits
-------

This app was developed by [Tea](https://github.com/CovenantJunior). It is an open-source project hosted on GitHub: [Repository Link](https://github.com/CovenantJunior/speech-recognition)