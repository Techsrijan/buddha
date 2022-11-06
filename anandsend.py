from gtts import *
from playsound import *

import random

s=random.randint(1,20)
print(s)
for i in range(3):
    choice=int(input('enter your choice number='))

    if choice==s:
        def play_sound():
            text = ("you win the game")
            audio = gTTS(text)
            audio.save("gamer.mp3")
            playsound("gamer.mp3")
            print("you win the game")

        play_sound()

        break
    else:

        def play_audio():
            text = ("you lose the game")
            audio = gTTS(text)
            with audio.save("sound.mp3"):
                try:
                    playsound("sound.mp3")
                    print("you lose the game")
                except Exception as e:
                    pass

            play_audio()












