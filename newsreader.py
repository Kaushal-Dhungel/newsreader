from win32com.client import Dispatch
import requests
import json
def speak(str):
    talk = Dispatch("SAPI.SpVoice")

    talk.Speak(str)


if __name__ == '__main__':
    speak("Hello, welcome to newstoday.com. I am your news anchor")
    speak(" top news for today from India and World are ")
    print("Hello, welcome to newstoday.com. I am your news anchor")
    print(" top news for today from India and World are ")

    #google top ten headlines
    #url = ('https://newsapi.org/v2/top-headlines?sources=google-news&apiKey=301dde8d4fd841e097ffeac8ed52d953') #fetch the url

    #top news from USA
    #url = ('https://newsapi.org/v2/top-headlines?country=us&apiKey=301dde8d4fd841e097ffeac8ed52d953')

    #top news from  India
    url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=301dde8d4fd841e097ffeac8ed52d953')


    news = requests.get(url).text #get the url and store in 'news' as text
    news_json = json.loads(news)  #use json to load
    #print(news_json["articles"])  #print all "articles" present in API

    article = news_json['articles'] #store articles from API in article

    #this is one approach
    #for a in article:               #for each a in article print 'title' of a
     #   print(a['title'])
      #  print("next news")

    for i in range (1,16):   #only limited no of news..generates from 1 to 15
        item = f"news no {i}" # i have used the concept of f strings learned from 'Harry'..feels great
        print(item)
        speak(item)  # speak funcn takes only string so i converted changing val of 'i' to string and passed here.
        print(article[i]['title']) #same as 'for i in articles: print i'
        speak(article[i]['title'])

        if i == 14:

            print("our last news is")
            speak("our last news is")

        if i==15:
            print("thank you for listening,have a great day, goodbye")
            speak("thank you for listening, have a great day, goodbye")
            break



