import pyttsx3
import speech_recognition as sr

def getSpeech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say Something ... ')
        data = r.listen(source)
        print('Done....')
    
        try:
            text = r.recognize_google(data)
            print('You said : '+ text)
        except Exception as e:
            print('Error : ',e)



getSpeech()