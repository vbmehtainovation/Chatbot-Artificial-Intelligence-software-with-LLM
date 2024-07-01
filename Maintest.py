import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import requests

print("Initializing...")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 


def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("JSK.....")

Sir = "Sir"
#def sendEmail(to,content):
#    server = smtplib.SMTP('smtp.gmail.com', 587)
 #   server.ehlo()
  # server.login('@gmail.com','password')
   # server.sendmail(to,content)
    #server.close()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if hour>=0 and hour <12:
        speak("Good morning" + Sir)
    elif hour>=12 and hour < 18:
        speak("Good afternoon" + Sir)
    else:
        speak("Good Evening" + Sir)
wishMe()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.record(source, duration=5)
    try: 
        print("Recognizing...")    
        #query=r.recognize_google(audio,language='en-in')
        #print(f"user said: {query}\n")
        query=r.recognize_google(audio , language='gu') 
        print(f"user said: {query}\n")
    except Exception as _e:
        print("Could you please repeat")        
        query = None
    return query        
query = takeCommand()



if 'wikipedia' in query.lower():
    speak('Searching...')
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)
             
 

elif 'open google' in query.lower():
    url = "google.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)



elif 'open youtube' in query.lower():
    url = "youtube.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)        



elif 'open facebook' in query.lower():
    url = "facebook.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url) 



elif 'open amazon' in query.lower():
    url = "amazon.in"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url) 



elif 'play music for inner peace'  in query.lower():
    speak("Playing some music for inner peace...")
    url = "https://www.youtube.com/watch?v=sKSGqeJ8U4Y&list=PLzF9IPDwkV6cgo1N5_lGFZ1G163sRejuL"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)        


     

elif 'play some powerful music'  in query.lower():
    speak("Playing some Powerfull music sir...")
    url = "https://www.youtube.com/watch?v=hMBKmQEPNzI&list=PLzF9IPDwkV6fgZxuDSWa7fuOF1esB4yXh"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)        



elif 'play music for motivation'  in query.lower():
    speak("Playing Songs for your Motivation sir...")
    url = "https://www.youtube.com/watch?v=8DMF0U6xV78&list=PLzF9IPDwkV6e8lab80ZgFW1RnPnzmYxJJ"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)        



elif 'play motivation music'  in query.lower():
    speak("Playing Songs for your Motivation sir...")
    url = "https://www.youtube.com/watch?v=8DMF0U6xV78&list=PLzF9IPDwkV6e8lab80ZgFW1RnPnzmYxJJ"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)  



elif 'play music for bliss' in query.lower():
    speak("Playing the music for your bliss sir...")
    url = "https://www.youtube.com/watch?v=4HRC6c5-2lQ&list=PLzF9IPDwkV6eSlLM1j4Mjo8Fz2SmQW7Mf"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)  



elif 'play some mild songs' in query.lower():
    speak("Playing the music for your bliss sir...")
    url = "https://www.youtube.com/watch?v=4HRC6c5-2lQ&list=PLzF9IPDwkV6eSlLM1j4Mjo8Fz2SmQW7Mf"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
      


elif 'play some english motivation music'  in query.lower():
    speak("Playing Songs for your Motivation sir...")
    url = "https://www.youtube.com/watch?v=snx5qGUtVi8&list=PLzF9IPDwkV6cOA9CoVvVXMnwnXn7FnHph"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)      



elif 'play old is gold music' in query.lower():
    speak("Playing the music for awesome enjoyment...")
    url = "https://www.youtube.com/watch?v=mX7g17mSfDg&list=PLzF9IPDwkV6c3En4NJIErNEpbMhd5WTSt"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)  



elif 'play old songs' in query.lower():
    speak("Playing the music for awesome enjoyment...")
    url = "https://www.youtube.com/watch?v=mX7g17mSfDg&list=PLzF9IPDwkV6c3En4NJIErNEpbMhd5WTSt"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)  



elif "tell the time" in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{Sir} The Time is {strTime}")

elif 'open stack overflow' in query:
     webbrowser.open("stackoverflow.com")

elif 'weather' in query.lower():
    api_key = "bc336708db83986a348245b41c9ab127"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # Give city name
    
    #city_name = input("Enter city name : ")
    speak('Tell me your City:')
    city_name = takeCommand()

    
    
    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    
    # get method of requests module
    # return  object
    response = requests.get(complete_url)
    
    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()
    
    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    
    if x["cod"] != "404":
    
        # store the value of "main"
        # key in variable y
        y = x["main"]
    
        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
    
        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]
    
        # store the value corresponding
        # to the "humidity" key of y
        current_humidiy = y["humidity"]
    
        # store the value of "weather"
        # key in variable z
        z = x["weather"]
    
        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]

        temp = int(current_temperature)-273

        # print following values
        r = (" The Temperature in " + city_name + "  is " +
          str(temp) + " degrees centigrade " +
          "\n atmospheric pressure (in hPa unit) is " +
          str(current_pressure) +
          "\n humidity is " +
          str(current_humidiy) + "%" +
          "\n description is " +
          str(weather_description))
        print(r)
        speak(r)

    
    else:
        print(" City Not Found ")



#elif 'email to ' in query.lower():
    #try:
     #   speak("what should I send")
      #  content = takeCommand()
       # to =     
        #sendEmail(to,content)
       # speak("Email has been sent successfully")
    #except Exception as _e:
     #   print("There might be a little error Sir") 



#chatbot



elif 'કેમ છો'  in query.lower():
    speak("હું  મજામાં  છું  સર... મારુ મશીન જોરદાર ચાલે છે... તમે કેમ છો")    
elif 'hey hi'  in query.lower():
    speak(" Hii Sir, How are you Doing ? Finally you broke the ice for talking with me...")    
elif 'તમે કેમ છો'  in query.lower():
    speak("હું સારું કામ કરું છું, મારું મશીન બધા સરસ રીતે કામ કરી રહ્યા છે સર ... ")
elif 'how are you'  in query.lower():
    speak("Well I am doing good, my machine is all working fine Sir...")
elif 'તમારા સર્જક કોન  છે '  in query.lower():
    speak("મને લાગે છે કે ... હું ભગવાન દ્વારા બનાવવામાં આવ્યો હતી !! અને તેણે કેટલાક માનવને મધ્યમ તરીકે પસંદ કર્યા ")
elif 'who created you'  in query.lower():
    speak("I think that... I was created by God!! and he chose some Human as Medium")
elif 'તમારો જન્મ ક્યારે થયો હતો'  in query.lower():
    speak(" તમરા કૅલેન્ડર સારી રીતે અને મારા જન્મદિવસ તરીકે કોઈ પણ શુભ દિવસની પસંદગી કરો ... ") 
elif 'when were you born'  in query.lower():
    speak("Well , Take a good look at you Calander and Choose any Auspicious day as my birthday...") 
elif 'where were you born'  in query.lower():
    speak("I was Born in India also known as Bharat , Hindustan ")
elif 'you are funny'  in query.lower():
    speak("You are right Sir!! I am , anyways Thanks for the Appreciation Sir...")
elif 'you are good'  in query.lower():
    speak("Thanks Sir , I just want you to know that I am here for you whenever you need Help Sir...") 
elif "what's up"  in query.lower():
    speak("Well , Just Chilling with you Sir...")
elif "motivate me"  in query.lower():
    speak("You have many talent's Sir...But I have a Speech for you")
    url = "https://www.youtube.com/watch?v=cUQwyHw8k10"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)          

#Google anything         

elif '' in query.lower():
    speak("There you go Sir...")
    url = ('google.com//?#q='+ query )
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

