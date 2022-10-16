from gtts import *
from  playsound import *
text="gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API. Writes spoken mp3 data to a file, a file-like object (bytestring) for further audio manipulation, or stdout . It features flexible pre-processing and tokenizing."
mymp=gTTS(text)
mymp.save('meragana.mp3')
playsound('meragana.mp3')
print("audio generated")