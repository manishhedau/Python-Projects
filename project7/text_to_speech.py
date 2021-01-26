import pyttsx3

engine = pyttsx3.init()

# text = 'Hii, good evening , It was nice meeting with you '
text = input('Enter your text to convert into speech : \n')
engine.say(text)
engine.runAndWait()