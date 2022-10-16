import gtts
from  playsound import *
j=3
text=''
while j<=30:
    print(j)
    text=text+str(j)
    audio = gtts.gTTS(text)
    audio.save('myaudio.mp3')
    playsound('myaudio.mp3')
    j=j+3
#text="These tutorials cover the basics of creating visualizations with Matplotlib, as well as some best-practices in using the package effectively."
#audio=gtts.gTTS(text)
#audio.save('myaudio.mp3')
print("File saved")