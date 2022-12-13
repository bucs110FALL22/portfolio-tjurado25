import requests 

class Jokes:
  def __init__(self):
    self.url = "https://official-joke-api.appspot.com/random_joke"
            
  def get_joke(self):
    response = requests.get(self.url)
    joke = response.json()
    

    return joke
    
                