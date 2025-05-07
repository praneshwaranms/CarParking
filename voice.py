import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        execute_command(command.lower())
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print(f"Google Speech Recognition request failed; {e}")

def execute_command(command):
    if "open" in command:
        open_application(command)
    elif "search" in command:
        search_web(command)
    else:
        print("Command not recognized.")

def open_application(command):
    # You can customize this function to open specific applications based on the command
    print(f"Opening application: {command.replace('open', '').strip()}")

def search_web(command):
    # You can customize this function to perform web searches based on the command
    print(f"Searching the web for: {command.replace('search', '').strip()}")

if __name__ == "__main__":
    recognize_speech()
