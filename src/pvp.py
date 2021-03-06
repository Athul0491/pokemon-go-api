from selenium import webdriver
import os
from flask_restful import Resource,reqparse
from selenium.webdriver.support.ui import Select

pokemon_get_args=reqparse.RequestParser()
pokemon_get_args.add_argument("name",type=str,help="Name is required",required=True)
pokemon_get_args.add_argument("attack",type=str,help="Attack is required",required=True)
pokemon_get_args.add_argument("defence",type=str,help="Defence is required",required=True)
pokemon_get_args.add_argument("hp",type=str,help="Hp is required",required=True)
pokemon_get_args.add_argument("league",type=str,help="League is required",required=True)

#PVP IV

# driver = webdriver.Chrome(ChromeDriverManager().install())
def scraper(name,attack,defence,hp,league):
    chrome_bin = os.environ.get('GOOGLE_CHROME_SHIM', None)

    GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
    CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_bin

    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")    
    # browser = webdriver.Chrome(options=chrome_options)
    # chrome_options.binary_location = GOOGLE_CHROME_PATH
    # PATH = 'C:\Program Files (x86)\chromedriver.exe'
    url = "https://pogostat.com/"
    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    browser.get(url)
    poke = browser.find_element_by_xpath('//*[@id="poke"]')
    poke.send_keys(name)
    attInp = browser.find_element_by_xpath('//*[@id="att_iv"]')
    attInp.send_keys(attack)
    defInp = browser.find_element_by_xpath('//*[@id="def_iv"]')
    defInp.send_keys(defence)
    hpInp = browser.find_element_by_xpath('//*[@id="sta_iv"]')
    hpInp.send_keys(hp)
    if(league==0):
        dd = Select(browser.find_element_by_xpath('//*[@id="cp_cap"]'))
        dd.select_by_index(0)
    if(league==1):
        dd = Select(browser.find_element_by_xpath('//*[@id="cp_cap"]'))
        dd.select_by_index(1)
    if(league==2):
        dd = Select(browser.find_element_by_xpath('//*[@id="cp_cap"]'))
        dd.select_by_index(2)

    browser.find_element_by_xpath('/html/body/div/div[5]/button').click()
    rank0 = browser.find_element_by_xpath('//*[@id="output"]/div[2]/div[1]').text
    att0 = browser.find_element_by_xpath('//*[@id="output"]/div[2]/div[2]').text
    def0 = browser.find_element_by_xpath('//*[@id="output"]/div[2]/div[3]').text
    hp0 = browser.find_element_by_xpath('//*[@id="output"]/div[2]/div[4]').text
    lvl0 = browser.find_element_by_xpath('//*[@id="output"]/div[2]/div[5]').text
    cp0 = browser.find_element_by_xpath('//*[@id="output"]/div[2]/div[6]').text
    perfect0 = browser.find_element_by_xpath('//*[@id="output"]/div[2]/div[7]').text

    rank1 = browser.find_element_by_xpath('//*[@id="output"]/div[3]/div[1]').text
    att1 = browser.find_element_by_xpath('//*[@id="output"]/div[3]/div[2]').text
    def1 = browser.find_element_by_xpath('//*[@id="output"]/div[3]/div[3]').text
    hp1 = browser.find_element_by_xpath('//*[@id="output"]/div[3]/div[4]').text
    lvl1 = browser.find_element_by_xpath('//*[@id="output"]/div[3]/div[5]').text
    cp1 = browser.find_element_by_xpath('//*[@id="output"]/div[3]/div[6]').text
    perfect1 = browser.find_element_by_xpath('//*[@id="output"]/div[3]/div[7]').text
    output = {
        'user_pokemon': {
            'rank':rank0, 
            'att':att0,
            'def':def0,
            'hp':hp0,
            'lvl':lvl0, 
            'cp':cp0, 
            'perfection':perfect0 
        },
        'rank1_pokemon': {
            #  rank, lvl, cp, perfection
            'rank':rank1, 
            'att':att1,
            'def':def1,
            'hp':hp1,
            'lvl':lvl1, 
            'cp':cp1, 
            'perfection':perfect1 
        },
    }
    # print(output)

    browser.quit()
    return output
# print(scraper("Charizard",5,5,5,0))
class Pvp(Resource):
    def get(self):
        args = pokemon_get_args.parse_args()
        output = scraper(args.name,int(args.attack),int(args.defence),int(args.hp),int(args.league))
        return output
# api.add_resource(Pokemon,"/api")
# if __name__ == "__main__":
#     app.run(host="localhost", port=8004, debug=True)