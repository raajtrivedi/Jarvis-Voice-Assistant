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
newsapi = "9a8e4a6461544c5087cddf151f8beba0"  # Replace with your News API key

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
    elif "play" in c.lower():
        query = c.replace("play","").strip()
        for name, link in musicLibrary.music.items():
            if query in name.lower():
                webbrowser.open(link)
                speak("Playing " + name)
                return
        speak("Song not found in your library")
    elif "news" in c.lower():
        # Fetch and read out top 5 news headlines using News API
        print("Fetching news...")
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=9a8e4a6461544c5087cddf151f8beba0")
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
                print("Say 'Jarvis' to wake me...")
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source)
                command = r.recognize_google(audio)  # Convert speech to text
                
                if "jarvis" in command.lower():
                    speak("I'm here")  # Acknowledge wake word

            # Once wake word is heard, listen for the actual command
            with sr.Microphone() as source:
                print("Listening to command...")
                r.adjust_for_ambient_noise(source, duration=0.3)
                audio = r.listen(source, phrase_time_limit=5)
                command = r.recognize_google(audio)  # Convert command to text

                proccessCommand(command)  # Handle the command

        except Exception as e: 
            # Print and speak error message if something goes wrong
            print("Error:",e)
            
