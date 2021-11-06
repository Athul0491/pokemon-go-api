import requests
from bs4 import BeautifulSoup
from flask_restful import Resource
def scraper():
    url = "https://thesilphroad.com/raid-bosses"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    Table=[]
    count = 0
    for divs in soup.findAll('div',{'class':'raid-boss-tier-inner'}):
        group = {}
        name = divs.find('div',{'class':'boss-name'}).text.strip()
        cpRange = divs.find('div',{'class':'cp-standard'}).div.text.strip()
        cpWeather = divs.find('div',{'class':'cp-weather-boosted'}).div.text.strip()
        sect = divs.find('div',{'class':'weather-icons'})
        images = sect.findAll('img')
        raid = []
        for img in images:
            weather = img['src'][56:-4]
            raid.append(weather)
        group['raid']=raid
        group['cpRange'] = cpRange
        group['cpWeather'] = cpWeather
        group['name'] = name
        if(count==0):
            group['tier'] = 'Mega'
        elif (count>=1 & count<4):
            group['tier'] = 'Tier 5'
        elif (count>=4 & count<8):
            group['tier'] = 'Tier 3'
        elif (count>=8):
            group['tier'] = 'Tier 1'
        Table.append(group)
        count +=1
    return Table

class Raid(Resource):
    def get(self):
        output = {"raid_table": scraper()}
        return output
