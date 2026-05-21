import text_to_speech
import datetime
import webbrowser
import weather

def action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        ans = "My Name is Virtual Assistant"

    elif "hello" in user_data:
        ans = "Hey, sir how can I help you"

    elif "good morning" in user_data:
        ans = "Good Morning Sir"

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        ans = str(current_time.hour) + " Hours " + str(current_time.minute) + " Minutes"

    elif "shutdown" in user_data:
        ans = "Shutting down the system"

    elif "play music" in user_data:
        ans = "Playing music"
        webbrowser.open("https://open.spotify.com")

    elif "youtube" in user_data:
        ans = "Opening YouTube"
        webbrowser.open("https://www.youtube.com")

    elif "open google" in user_data:
        ans = "Opening Google"
        webbrowser.open("https://www.google.com")

    elif "weather" in user_data:
        ans = weather.get_weather()

    else:
        ans = "Sorry, I didn't understand that."

    text_to_speech.text_to_speech(ans)
    return ans