from playsound import playsound

from gtts import gTTS

text = "hello"

file_name = "sample.mp3"

tts_en = gTTS(text=text, lang='en')
tts_en.save("./"+file_name)