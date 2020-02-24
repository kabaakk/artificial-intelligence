import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import pyaudio
import os
import sys

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Yapay zeka')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Bilgisayar: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Günaydın!')

    if currentH >= 12 and currentH < 18:
        speak('İyi günler!')

    if currentH >= 18 and currentH !=0:
        speak('İyi akşamlar!')

greetMe()

speak('Merhaba efendim ben asistanım.')
speak('Size nasıl yardımcı olabilirim?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Bekleniyor...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='tr-Tr')
        print('Sen: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Üzgünüm efendim komut anlaşılamadı')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'youtube aç' in query:
            speak('tamam')
            webbrowser.open('www.youtube.com')

        elif 'google aç' in query:
            speak('tamam')
            webbrowser.open('www.google.com')

        elif 'gmail aç' in query:
            speak('tamam')
            webbrowser.open('www.gmail.com')

        elif "hello" in query or 'nasilsin' in query:
            stMsgs = ['Bildigin gibi!', 'İyiyim!', 'Güzel!', 'Güzel zaman geçiriyorum']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Kime gönderilecek? ')
            recipient = myCommand()

            if 'bana' in recipient:
                try:
                    speak('Ne yazmamı istersiniz? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email gönderildi!')

                except:
                    speak('Üzgünüm efendim mesaj anlaşılamadı')


        elif 'hiçbir şey' in query or 'iptal' in query or 'dur' in query:
            speak('tamam')
            speak('Görüşürüz efendim iyi günler')
            sys.exit()
           
        elif 'merhaba' in query:
            speak('merhaba efendim')

        elif 'görüşürüz' in query:
            speak('Görüşürüz efendim iyi günler.')
            sys.exit()
                                    
        elif 'play music' in query:
            music_folder = Your_music_folder_path
            music = [music1, music2, music3, music4, music5]
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
                  
            speak('Okay, here is your music! Enjoy!')
            

        else:
            query = query
            speak('Aranıyor...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA diyorki - ')
                    speak('Anlaşıldı.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Anlaşıldı.')
                    speak('WIKIPEDIA diyorki - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Bir sonraki komut efendim')
