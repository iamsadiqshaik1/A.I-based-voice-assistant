import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

en=pyttsx3.init()

#en.say("hello this is Jarvis")
voices = en.getProperty('voices')
en.setProperty('voice' ,voices[1].id)
def speak(audio):
    en.say(audio)

    en.runAndWait()

speak("hey boss this is friday and I am ai assistant")

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("time in  24 hrs format and is")
    speak(Time)

#time()

def date():
    year= int(datetime.datetime.now().year)
    month= int(datetime.datetime.now().month)
    date= int(datetime.datetime.now().day)
    speak("date is")
    speak(date)
    speak("month is")
    speak(month)
    speak("year is")
    speak(year)
#date()

def wishme():
    speak("welcome back boss!")
    #speak("current time in  24 hrs format and it is")
    ##time()
    #speak("current date is")
    ##date()
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<15:
        speak("good afternoon")
    elif hour>=15 and hour<20:
        speak("good evening")
    elif hour>=20 and hour<24:
        speak("good night")
    else:
        speak("good night")
    speak("friday at your service tell meh how can i help you")

#wishme()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("recognizing..")
        query=r.recognize_google(audio,language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("say that again boss....")
        return "none"
    return query

def sendemail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.eclo()
    server.starttls()
    server.login('sadiqshaik1211@gmail.com','Sadiqshaik@1234')
    server.sendmail('sadiqshaik1211@gmail.com',to,content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\sadiq shaik\\Desktop\\car\\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at"+usage)
    battery = psutil.sensors_battery()
    speak("the battery is at")
    speak(battery.percent )

def jokes():
    speak(pyjokes.get_joke())

if __name__=="__main__":
    wishme()
    while True:
        query=takecommand().lower()

        if 'time'in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("boss I am searching.....")
            query = query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print("friday:",result)
            speak(result)

        elif 'send mail' in query:
            try:
                speak("what should i write ")
                content =takecommand()
                to='sadiqshaik1211@gmail.com'
                sendemail(to,content)
                speak("email is sent successfully" )
            except Exception as e:
                print(e)
                speak("I cant able to send due to bad network connection")

        elif 'search' in query:
            speak("what you want to search")
            chromepath="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search= takecommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'log out' in query:
            os.system("shutdown -l")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'note this one' in query:
            speak("what to remember boss")
            data = takecommand()
            speak("you said me to remember that"+data)
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you remember anything' in query:
            remember=open('data.txt','r')
            speak("you said to remember that "+remember.read())

        elif 'play songs'in query:
            song_dir='C:\\Users\sadiq shaik\Desktop\Musicfiles'
            songs=os.listdir(song_dir)
            os.startfile(os.path.join(song_dir,songs[1]))

        elif 'screenshot' in query:
            screenshot()
            speak("yeah screenshot is done and yeah it is great content")

        elif 'battery' in query:
            cpu()
            speak("percent")

        elif 'joke' in query:
            jokes()
            speak("it is really good right hahahaha")

        elif "offline" in query:
            speak("yep   done!")
            quit()
