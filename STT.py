import speech_recognition as sr
from textblob import TextBlob
from pydub import AudioSegment
filename = "SentTest.wav"
r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)

# Perform sentiment analysis
analysis = TextBlob(text)

# Get sentiment polarity (-1 to 1, where -1 is negative, 1 is positive)
sentiment_polarity = analysis.sentiment.polarity

if sentiment_polarity > 0:
    sentiment_label = "Positive"
elif sentiment_polarity < 0:
    sentiment_label = "Negative"
else:
    sentiment_label = "Neutral"

print(f"Sentiment: {sentiment_label}")
print(f"Polarity: {sentiment_polarity}")
