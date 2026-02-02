
from datetime import datetime
import webbrowser
import requests
#corpus
greet_msg = ["hi","hello","hey","hi there","hey there"]
date_msg = ["what's the date","date","tell me date","today's date"]
time_msg = ["what's the time","time","tell me time","today's time"]
news_intent = ["news","Tell me news","what is news"]
def get_location():
    respose = requests.get("http://ip-api.com/json/")
    obj = respose.json()
    return obj['city']
def get_news():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=695e07af402f4b119f0703e9b19f4683"
    respone = requests.get(url)
    obj = respone.json()
    articles = obj['articles']
    for i in range(len(articles)):
        print(f"Headlines {i+1}:{articles[i]['title']}")
def get_weather():
    apikey = '88b9eda5d0b764565a67bed8bd7e9ef8'
    location = get_location()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={apikey}&units=metric"
    response = requests.get(url)
    obj = response.json()
    if obj.get("cod") != 200:
        return "Could not fetch weather data."
    description = obj['weather'][0]['description']
    temp = obj['main']['temp']
    humidity = obj['main']['humidity']
    return f"Weather in {location}: {description}, Temp: {temp}°C, Humidity: {humidity}%"

chat = True
while chat:
    msg = input("Enter your message: ").lower()
    if msg in greet_msg:
        print("Hello how are you ?")
    elif msg in date_msg:
        print(datetime.now().date())
    elif msg in time_msg:
        current_time = datetime.now().time()
        print(current_time.strftime("%I:%M:%S"))
    elif "open" in msg:
        site = msg.split("open")[-1].strip()
        url = f"https://www.{site}.com"
        webbrowser.open(url)
        print(f"opening {site}")
    elif "cal" in msg:
        print(eval(msg.split()[-1]))
    elif msg == "city":
        print(get_location())
    elif msg in news_intent:
       get_news()
    elif msg == "weather":
        print(get_weather())
    elif msg == "bye":
        chat = False
    else:
        print("I can't understand")