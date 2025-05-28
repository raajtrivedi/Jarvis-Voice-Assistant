# Import necessary libraries
import speech_recognition as sr  # For speech recognition
import webbrowser                # To open web pages
import pyttsx3                   # For text-to-speech
import musicLibrary              # Custom music library (assumed to be a dict with song name to URL mapping)
import requests                  # To make HTTP requests (for news API)
import time                      # To add delay between actions

# Initialize recognizer and text-to-speech engine
recgnizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "Your api key"  # Replace with your News API key

# Function to speak the given text aloud
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to process and execute the user's command
def proccessCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "whatsapp" in c.lower():
        webbrowser.open("https://whatsapp.com")
    elif c.lower().startswith("play"):
        # If command starts with "play", extract the song name and play it
        song = c.lower().split(" ")[1]  # Get the second word as song name
        link = musicLibrary.music[song]  # Look up the URL from musicLibrary
        webbrowser.open(link)
    elif "news" in c.lower():
        # Fetch and read out top 5 news headlines using News API
        print("Fetching news...")
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            print("Top Headlines:")
            for article in articles[:5]:  # Speak only top 5 headlines
                title = article.get("title")
                if title:
                    print("Speaking:", title)
                    speak(title)
                    time.sleep(1)  # Add a short delay between headlines
                else:
                    print("Skipped article with no title")
        else:
            # If API request fails
            print("Failed to fetch news.")
            speak("Sorry, I couldn't fetch the news.")

    # Placeholder for adding AI-handling or fallback command processing later
    """
    else:
        # Let OpenAI handle the request 
        pass
    """

# Main entry point of the program
if __name__ == "__main__":
    speak("Initializing Jarvis...")  # Initial greeting
    
    while True:
        r = sr.Recognizer()  # Create a recognizer instance

        print("recognizing...")
        try:
            # First, listen for the wake word "Jarvis"
            with sr.Microphone() as source:
                print("Listening...!")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                command = r.recognize_google(audio)  # Convert speech to text
                
                if command.lower() == "jarvis":
                    speak("I'm here")  # Acknowledge wake word

            # Once wake word is heard, listen for the actual command
            with sr.Microphone() as source:
                print("Jarvis Active...")
                audio = r.listen(source)
                command = r.recognize_google(audio)  # Convert command to text

                proccessCommand(command)  # Handle the command

        except Exception as e:
            # Print and speak error message if something goes wrong
            print("Error; {0}".format(e))