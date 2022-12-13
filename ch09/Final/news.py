import requests

class News:
  def __init__(self):
    self.url = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=a25042a25c9c4b8ea055c44cb2228b12"


  def get_news(self):
    response = requests.get(self.url)
    news = response.json()
    


    return news

