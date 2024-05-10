import requests
from bs4 import BeautifulSoup
if __name__ == "__main__":
    print("SUCCESS!")
    print("Hello! Welcome to the climate trends app!")
    city = "Newark"
    url = "https://www.google.com/search?q="+"weather"+city
    requests instance
    html = requests.get(url).content
    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')


