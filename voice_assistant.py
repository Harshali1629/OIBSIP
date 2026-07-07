"""
Voice Assistant - Beginner Tier
OIBSIP Python Programming Track - Task 1

Objective:
Build a Python-based voice assistant that listens to spoken commands and
responds with useful actions.

Features implemented (Beginner Tier Feature Checklist):
1. Capture voice input using speech_recognition (microphone)
2. Respond to "Hello" with a predefined greeting
3. Tell the current time and date on request
4. Perform a web search on a user-specified topic (opens browser with query)
5. Graceful error handling: if voice is not understood, ask the user to repeat
6. Text-to-speech feedback using pyttsx3 for all responses

Author: <YOUR FULL NAME HERE>
Track: Python Programming
"""

import datetime
import webbrowser

import pyttsx3
import speech_recognition as sr


# ---------------------------------------------------------------------------
# Text-to-Speech Engine Setup
# ---------------------------------------------------------------------------
engine = pyttsx3.init()
engine.setProperty("rate", 170)  # speaking speed


def speak(text: str) -> None:
    """Speak the given text out loud and print it for visibility."""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


# ---------------------------------------------------------------------------
# Speech Recognition
# ---------------------------------------------------------------------------
recognizer = sr.Recognizer()


def listen() -> str:
    """
    Capture audio from the microphone and convert it to text.
    Returns an empty string if speech could not be understood.
    """
    with sr.Microphone() as source:
        print("\nListening... (speak now)")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
            return ""

    try:
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        # Graceful error handling: could not understand audio
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return ""
    except sr.RequestError:
        speak("I'm having trouble reaching the speech recognition service.")
        return ""


# ---------------------------------------------------------------------------
# Command Handlers
# ---------------------------------------------------------------------------
def tell_time_and_date() -> None:
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    current_date = now.strftime("%A, %d %B %Y")
    speak(f"The current time is {current_time} and today's date is {current_date}.")


def perform_web_search(query: str) -> None:
    """
    Extracts the search topic from the command and opens a browser
    with the search results.
    """
    # Remove the trigger words to isolate the actual search topic
    for trigger in ["search for", "search", "look up", "google"]:
        if trigger in query:
            query = query.replace(trigger, "")
            break

    topic = query.strip()
    if not topic:
        speak("What would you like me to search for?")
        topic = listen()
        if not topic:
            speak("I couldn't get a search topic, cancelling the search.")
            return

    speak(f"Searching the web for {topic}")
    url = f"https://www.google.com/search?q={topic.replace(' ', '+')}"
    webbrowser.open(url)


def handle_command(command: str) -> bool:
    """
    Decides what action to take based on the recognized command.
    Returns False if the user wants to exit, True otherwise.
    """
    if not command:
        return True  # nothing understood, just keep listening

    if "hello" in command or "hi" in command:
        speak("Hello! I'm your voice assistant. How can I help you today?")

    elif "time" in command or "date" in command:
        tell_time_and_date()

    elif "search" in command or "google" in command or "look up" in command:
        perform_web_search(command)

    elif "exit" in command or "quit" in command or "stop" in command:
        speak("Goodbye! Have a great day.")
        return False

    else:
        speak("I'm not sure how to help with that yet. "
              "You can say hello, ask for the time or date, "
              "or ask me to search something for you.")

    return True


# ---------------------------------------------------------------------------
# Main Loop
# ---------------------------------------------------------------------------
def main() -> None:
    speak("Voice assistant is starting. Say 'hello' to begin, "
          "or say 'exit' anytime to quit.")

    running = True
    while running:
        command = listen()
        running = handle_command(command)


if __name__ == "__main__":
    main()