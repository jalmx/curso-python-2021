import requests
import ast

def get_weather():

    header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
    page = requests.get('https://www.accuweather.com/en/mx/coatzacoalcos/236228/weather-forecast/236228', headers=header)

    content = page.text

    lines = content.splitlines()

    text_to_find = 'recentLocations'
    text_finded = ''

    for l in lines:
        if l.find(text_to_find) >=0:
            text_finded = l.strip()
            break

    text_split = text_finded.split(" ")
    data = text_split[-1]
    ##cleaning data
    data = data.replace("[",'').replace(']','').replace(';','')

    #print(type(data))#esto fue para ver que tipo era el objeto

    #print(data)

    data = ast.literal_eval(data)
    
    country = data['adminArea']['localizedName']
    temp = data['temp']
    city = data['localizedName']

    return {
        'city':city,
        'temp': temp,
        'country': country
    }
