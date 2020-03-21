import smtplib
import config
from gtts import gTTS
import playsound
import os

from bnbphoneticparser import BanglishToBengali

def send_email(subject, msg):
    try:
        subject = "NetraJal"
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, text)
        server.sendmail(config.EMAIL_ADDRESS, config.SEND_ADDRESS, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")

def SpeakLanguage(text):
    tts = gTTS(text, lang='bn')
    tts.save("TextedToVoice.mp3")
    os.system("mpg321 TextedToVoice.mp3")
    playsound.playsound('TextedToVoice.mp3', True)
    os.remove("TextedToVoice.mp3")

def GazeOutputText(text):
    with open("GazeOutputText.txt", 'w') as f:
        f.write(text)
        
def BanglaConverter(text):
    banglish2bengali = BanglishToBengali()
    texta = banglish2bengali.parse(text.strip())
    #print(texta)