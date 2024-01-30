import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio).lower()
            print(f"You said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please repeat.")
            return None
        except sr.RequestError as e:
            print(f"Error fetching results from Google Speech Recognition: {e}")
            return None

def handle_command(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}.")
    elif "date" in command:
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}.")
    elif "search" in command:
        search_query = command.replace("search", "").strip()
        speak(f"Searching the web for {search_query}.")
        search_url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(search_url)
    elif "exit" in command or "bye" in command:
        speak("Goodbye! Have a great day.")
        exit()
    else:
        speak("I'm sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak("Hello! I'm your Google assistant. How can I help you today?")
    while True:
        command = get_audio()
        if command:
            handle_command(command)
