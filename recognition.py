import speech_recognition as sr
import pyttsx3

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand your speech.")
    except sr.RequestError:
        print("Sorry, speech recognition service is unavailable.")

def text_to_speech():
    engine = pyttsx3.init()
    text = input("Enter the text to convert to speech: ")
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        print("Select an option:")
        print("1. Speech-to-Text")
        print("2. Text-to-Speech")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            speech_to_text()
        elif choice == '2':
            text_to_speech()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
