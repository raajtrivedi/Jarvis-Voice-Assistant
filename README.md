# **Jarvis-Voice-Assistant**
Jarvis is a simple, speech-enabled virtual assistant built with Python that responds to voice commands to open websites, play music, and read out the latest news headlines. Inspired by the fictional assistant from Iron Man, this project demonstrates the use of speech recognition, text-to-speech, and web integration using Python libraries.

---

## **🚀 Features :**
 - 🎧 Voice Wake Word Detection — Activates when you say “Jarvis”
 - 🌐 Open Popular Websites — Supports Google, YouTube, LinkedIn, WhatsApp
 - 🎵 Play Songs from Your Music Library — Command Jarvis to play a song by name
 - 📰 Fetch Top News Headlines — Reads out top 5 news from India using the NewsAPI
 - 🗣️ Text-to-Speech Response — Gives vocal feedback for actions performed

---

## **🛠️ Technologies Used :**
  1. **speech_recognition** – For converting speech to text
  2. **pyttsx3** – For text-to-speech output
  3. **webbrowser** – To open URLs in your browser
  4. **requests** – To fetch real-time news via News API
  5. **musicLibrary** – A custom Python module (dictionary) with predefined songs and their URLs

---

## **🧠 How It Works :**
 - Jarvis waits for the wake word "Jarvis" using your system's microphone.
 - Once activated, it listens for a follow-up command like:
     - "Open Google"
     - "Play believer"
     - "News"
- Based on the command, it opens web pages, plays songs from your music library, or fetches and reads out top news headlines.
- Uses text-to-speech (TTS) to give vocal confirmations and output.

---

## **👤 Author**
 - Raj Trivedi
  - 📍 Junagadh, India
  - 💡 Python & ML Enthusiast
