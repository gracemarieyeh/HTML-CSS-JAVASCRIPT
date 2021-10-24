import speech_recognition as sr

filename = "blahblah.wav"

r = sr.Recognizer()

# open the file RETURNS A TEXT FILE
def audiototext(filename):
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
    
    return text
