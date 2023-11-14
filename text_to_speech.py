from gtts import gTTS
import os


# file=open('sample.txt')   # create a folder sample.txt and some text in it before to run the program
# text=file.read()

# text="Hi Mohan ,How are you ? I am Chitti the robot."
language='en'

obj= gTTS(text=text,lang=language,slow=False)

obj.save('sample.mp3')

os.system("sample.mp3")