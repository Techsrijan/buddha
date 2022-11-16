import pyttsx3

engine=pyttsx3.init()
for i in range(4):
    print(i)
    engine.say(i)
    engine.runAndWait()
