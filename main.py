import requests
from bs4 import BeautifulSoup
def initializeFiles():
    ## run touch filename for each filename in list
    return 0
def getSurroundingTowns():
    return ["Hackettstown", "Mount Olive", "Great Meadows", "Allamuchy", 
    "Mansfield", "Hopatcong", "Easton", "Phillipsburg",
    "Morristown", "Bethlehem", ""]
def getHourlyTemp(strlist):
    sol = list()
    sol.append(strlist[5])
    sol.append(strlist[12])
    sol.append(strlist[19])
    sol.append(strlist[26])
    return sol

if __name__ == "__main__":
    ##print("SUCCESS!")
    ##print("Hello! Welcome to the climate trends app!")
    city = "Hackettstown"
    url = "https://www.google.com/search?q="+"weather"+city
    # requests instance
    html = requests.get(url).content
    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text 
    # this contains time and sky description
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    # format the data
    data = str.split('\n')
    time = data[0]
    sky = data[1]
    # list having all div tags having particular class name
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    
    # particular list with required data
    strd = listdiv[5].text
    print(getHourlyTemp(strd.split())) 
    # formatting the string
    pos = strd.find('Wind')
    other_data = strd[pos:]
    if(pos != -1):
        print(other_data)
    # printing all the data
    print("Temperature is", temp)
    print("Time: ", time)
    print("Sky Description: ", sky)

