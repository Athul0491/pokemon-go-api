#pokemon details
import requests
from bs4 import BeautifulSoup
from flask_restful import Resource,reqparse

pokemon_get_args=reqparse.RequestParser()
pokemon_get_args.add_argument("id",type=str,help="Pokemon id is required",required=True)
def data(Pokemon):
    pika = []
    url = "https://gamepress.gg/pokemongo/pokemon-list"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    for divs in soup.findAll('tr', {'class': 'pokemon-row'}):
        
        word = divs.td.find_next('td').text.strip()
        b,c = word.split(' ',1)
        pika.append({b[1:]:c})
    p = {
        "a": pika
    }
    for dicts in p['a']:
        for ind, pok in dicts.items():  
            if pok == Pokemon:
                return ind



def image(_id):   
    url = "https://gamepress.gg/pokemongo/pokemon/"+ str(_id)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    img = 'https://gamepress.gg/'+soup.find('div', {'class': 'pokemon-image'}).div.img['src']
    return(img)



def vulnerableData(_id):
    url = "https://gamepress.gg/pokemongo/pokemon/"+ str(_id)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    vulnerable = []
    divs0 = soup.find('div', {'id': 'weak-div'})
    initial0 = []
    initial1= []

    for src0 in divs0.findAll('img'):
        
        type0 = src0['src'][31:-4]
        initial0.append(type0)
    for src1 in divs0.findAll('span'):
        damage = src1.text.strip()
        initial1.append(damage)

    for item in range(len(initial0)):
        vulnerable.append({"name":initial0[item], "multiplier":initial1[item]})
    return vulnerable


def resistantData(_id):
    url = "https://gamepress.gg/pokemongo/pokemon/"+ str(_id)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    resistant = []

    mid0 = []
    mid1= []
    divs2 = soup.find('div', {'id': 'resist-div'})
    for src2 in divs2.findAll('img'):
        type2 = src2['src'][31:-4]
        mid0.append(type2)
    for src3 in divs2.findAll('span'):
        damage1 = src3.text.strip()
        mid1.append(damage1)
    for item in range(len(mid0)):
        resistant.append({"name":mid0[item], "multiplier":mid1[item]})
    return resistant

def pokeRatings(_id):
    ratings = []
    url = "https://gamepress.gg/pokemongo/pokemon/"+str(_id)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    div = soup.find('div', {'class': 'pokemon-ratings-container'})
    for rows in div.findAll('div',{'class':'rating-cell-item'}):
        attacker = rows.find('span',{'class':'cell-rating-left'}).text.strip()
        score = rows.find('span',{'class':'cell-rating-right'}).b.text.strip()
        ratings.append({attacker:score})
    return ratings

def pType(_id):
    pokeTypes=[]
    url = "https://gamepress.gg/pokemongo/pokemon/"+str(_id)
    types = []
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    div = soup.find('div', {'class': 'field field--name-field-pokemon-type field--type-entity-reference field--label-hidden field__items'})
    for rows in div.findAll('div',{'class':'taxonomy-term vocabulary-type'}):
        a = rows.div.text.strip()
        types.append(a)
    for i in range(len(types)):
        pokeTypes.append({i:types[i]})
    return pokeTypes

def pStats(_id):
    url = "https://gamepress.gg/pokemongo/pokemon/"+str(_id)
    stats = ''
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    for divs in soup.findAll('div', {'class': 'header-stats'}):
        div = divs.find('span',{'class':'stat-text'})
        stats += div.text.strip()[4:] + ','
    return stats[:-1]

class Details(Resource):
   def get(self):
        args = pokemon_get_args.parse_args()
        _id = args.id
        img = image(_id)
        vulnerable = vulnerableData(_id)         
        resistant = resistantData(_id)
        ratings = pokeRatings(_id)
        types = pType(_id)
        stats = pStats(_id)
        output = {"img":img,"Types":types,"Stats":stats,"Vulnerable":vulnerable,'Resistant':resistant,"Rating":ratings}
        return output
