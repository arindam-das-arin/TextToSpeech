import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Define the emotions
emotions = {
    "happy": {"rate": 150, "volume": 1, "voice": "english"},
    "sad": {"rate": 100, "volume": 0.5, "voice": "english"},
    "angry": {"rate": 200, "volume": 1, "voice": "english"},
    "excited": {"rate": 150, "volume": 1, "voice": "english"},
    "fearful": {"rate": 100, "volume": 0.5, "voice": "english"},
    "surprised": {"rate": 200, "volume": 1, "voice": "english"},
}

# Take input text from the user
text = input("Enter the text you want to convert to speech: ")

# Get the emotion from the user
emotion = input("Enter the emotion (happy/sad/angry/excited/fearful/surprised): ")


# Set the voice properties for the selected emotion
engine.setProperty("rate", emotions[emotion]["rate"])
engine.setProperty("volume", emotions[emotion]["volume"])
engine.setProperty("voice", emotions[emotion]["voice"])

# Convert text to speech
engine.say(text)

# Set the file name for the audio file
file_name = input("Enter the file name for the audio file (without extension): ")

# Save the speech as an audio file
engine.save_to_file(text, f"{file_name}.mp3")

# Run the pyttsx3 engine
engine.runAndWait()
