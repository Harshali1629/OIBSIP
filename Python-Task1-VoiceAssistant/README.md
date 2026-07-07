# Voice Assistant (Python Programming - Task 1, Beginner Tier)

**OIBSIP Folder path:** `OIBSIP/Python-Task1-VoiceAssistant/`

## Objective
A Python-based voice assistant that listens to spoken commands via the
microphone and responds using text-to-speech.

## Tech Stack
- Python 3
- `speech_recognition` (captures and converts voice to text)
- `pyttsx3` (text-to-speech feedback)
- `datetime` (time/date)
- `webbrowser` (opens search results)

## Features (Beginner Tier)
- [x] Captures voice input using the microphone
- [x] Responds to "hello"/"hi" with a greeting
- [x] Tells the current time and date on request
- [x] Performs a web search on a spoken topic (opens the default browser)
- [x] Graceful error handling — asks the user to repeat if unclear
- [x] All responses are spoken aloud using `pyttsx3`

## Setup Instructions

1. Install Python 3.8+.
2. Install the required libraries:
   ```bash
   pip install SpeechRecognition pyttsx3 pyaudio
   ```
   - **Windows:** `pip install pyaudio` usually works directly.
   - **Mac:** `brew install portaudio` then `pip install pyaudio`.
   - **Linux:** `sudo apt-get install python3-pyaudio` or
     `sudo apt-get install portaudio19-dev` then `pip install pyaudio`.
3. Make sure your microphone is connected and enabled.
4. Run the assistant:
   ```bash
   python voice_assistant.py
   ```

## How to Use
Speak clearly after you see `Listening...` in the terminal. Try commands like:
- "Hello"
- "What's the time?" / "What's the date?"
- "Search for the latest smartphones"
- "Exit" / "Quit" / "Stop" — to close the assistant

If the assistant doesn't understand you, it will politely ask you to repeat.

## Notes
- Requires an active internet connection (Google's speech recognition API is
  used).
- Tested on Windows/Linux with a standard USB/built-in microphone.

## Demo Video
See the linked demo video in the LinkedIn submission post — it shows the
title card (Name + Track + Task Title) followed by a live walkthrough of the
assistant responding to greeting, time/date, and search commands.
