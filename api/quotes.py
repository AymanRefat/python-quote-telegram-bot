import requests as r 
from dataclasses import dataclass

@dataclass
class Quote:
  quote:str 
  author :str

  def generate_quote(self)->str:
    return f"\"{self.quote}\" - {self.author}"


class QuotesAPI:
  def get_today_quote(self)->None:
    response =  r.get("https://zenquotes.io/api/today")
    return self.parse_quote(response).generate_quote()

  def get_random_quote(self)->None:
    response = r.get("https://zenquotes.io/api/random")
    return self.parse_quote(response).generate_quote()

  def parse_quote(self,response:r.Response)->Quote:
    data = response.json()
    quote = data[0]['q'].removesuffix('.')
    author = data[0]['a']
    return Quote(quote,author)




if __name__ == "__main__":
  print(QuotesAPI().get_today_quote()[0]['q'])
  print(QuotesAPI().get_today_quote()[0]['a'])