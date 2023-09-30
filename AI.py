from vosk import Model, KaldiRecognizer
import pyttsx3
import datetime
import pyaudio
import json
import webbrowser
import os
import msvcrt as m

def wait():
    m.getch()

Assistаnt=pyttsx3.init()
voise=Assistаnt.getProperty('voices')
Assistаnt_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0'
Assistаnt.setProperty('voice', Assistаnt_voice_id)

def speak(audio):
    print('Bach_assistant:' + audio)
    Assistаnt.say(audio)
    Assistаnt.runAndWait()

def welcome():
    hour=datetime.datetime.now().hour
    if hour >=3 and hour <12:
        speak('Good morning boss')
    elif hour >=12 and hour <18:
        speak('Good afternoon boss')
    elif hour >=18 and hour <21:
        speak('Good evening boss')
    elif hour >=21 and hour <24:
        speak('Good night and have a nice dream boss!')
    elif hour >=0 and hour <3:
        speak('It is late boss, let us take a nap')
    speak('How can I help you now')
    print('')
    print('listening ...')
    print('')

model = Model("D:\ProjectAI\models\small")
os.system('cls')
rec = (model, 16000)
rec = KaldiRecognizer(model, 16000)

cap=pyaudio.PyAudio()
stream=cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
welcome()

stream.start_stream()

a=0

while True:
    data=stream.read(4000, exception_on_overflow=False)
    if len(data)==0:
        break

    if rec.AcceptWaveform(data):
        result=rec.Result()
        result=json.loads(result)
        print('Boss: ' + result['text'])

        searchbox = ["знайди", "найди", "знайти"]
        browserbox = ["браузер","веб-браузер"]
        urlbox = []

        if any(word in result['text'] for word in searchbox):
            os.system('cls')
            stream.stop_stream()
            for word in searchbox:
                text = result['text'].replace(word, "").strip()
            webbrowser.open(f'https://www.google.com/search?q={text}')
            speak('Открываю')   
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif any(word in result['text'] for word in browserbox):
            os.system('cls')
            stream.stop_stream()
            webbrowser.open('') 
            speak('відкриваю браузер')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "ютуб" in result['text']:
            os.system('cls')
            stream.stop_stream()
            webbrowser.open('https://www.youtube.com/') 
            speak('відкриваю ютуб')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        else:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak('Не шарю')
            stream.start_stream()
            print('')
            print('listening ...')
            print()
            
        
