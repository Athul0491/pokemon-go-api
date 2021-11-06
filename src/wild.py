import requests
from bs4 import BeautifulSoup, NavigableString, Tag

from flask_restful import  Resource,reqparse
from flask import jsonify




pokemon_get_args=reqparse.RequestParser()
pokemon_get_args.add_argument("id",type=str,help="Pokemon id is required",required=True)


def image(_id):   
    url = "https://gamepress.gg/pokemongo/pokemon/"+ str(_id)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    img = 'https://gamepress.gg/'+soup.find('div', {'class': 'pokemon-image'}).div.img['src']
    return img


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
        vulnerable.append({initial0[item]:initial1[item]})
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
        resistant.append({mid0[item]:mid1[item]})
    return resistant


def fc(_id):
    url = "https://gamepress.gg/pokemongo/pokemon/"+str(_id)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    divs = soup.find('div', {'id': 'evolution-requirements'})
    td = divs.findAll('td')
    flee = td[5].text.strip()
    capture = td[-1].text.strip()
    return {"flee rate":flee,"capture rate":capture}

def table(_id):
    url = "https://gamepress.gg/pokemongo/pokemon/" + str(_id)

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    Table=[]
    group = []
    div = soup.find('div',{'id':'minmaxcpchart'})
    table = div.table

    output = []
    for i in range(len(table.findAll('tr'))):
        group = []
        for td in table.findAll('tr')[i]:
            if isinstance(td, NavigableString):
                continue
            if isinstance(td, Tag):
                group.append(td.text.strip())
        output.append(group[1:])
    return output
class Wild(Resource):
    def get(self):
        args = pokemon_get_args.parse_args()
        _id = args.id;
        img = image(_id)
        vulnerable = vulnerableData(_id)         
        resistant = resistantData(_id)
        types = pType(_id)
        rate = fc(_id)
        _table = table(_id) 
        output = {"img":img,"Types":types,"Vulnerable":vulnerable,"Resistant":resistant,"rates":rate,"table":_table}
        return jsonify(output)



