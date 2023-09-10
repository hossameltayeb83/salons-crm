#https://www.mysalonsuite.com/all-locations/
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import json
import time

options = Options()


options.add_argument('--headless=new')
options.add_argument("--window-size=1920,1080")
data =[]
two_words_states = ['HAMPSHIRE','JERSEY','MEXICO','YORK','CAROLINA','DAKOTA','ISLAND','VIRGINIA']
driver = webdriver.Chrome()
data=[]
def main():
    config()
    links = gather_links()
    gather_data(links)
def config():
    driver.get('https://www.mysalonsuite.com/all-locations/')
    driver.implicitly_wait(5)
    driver.maximize_window()
def gather_links():
    links=[]
    anchors = driver.find_elements(By.CSS_SELECTOR,('div[class="section__body"] li strong a'))
    print(len(anchors))
    for a in anchors:
        links.append(a.get_attribute('href'))
    return links    
def gather_data(links):
    for link in links:
        driver.get(link)
        location_name = driver.find_element(By.CSS_SELECTOR,('h1')).text
        print(location_name)
        full_address = driver.find_element(By.CSS_SELECTOR,('div[class="intro__content"] > p')).get_attribute('innerHTML').strip()
        print(full_address)
        location_address = full_address[:full_address.find('<br>')]
        full_city_and_state= full_address[len(location_address)+4:]
        city_and_state= full_city_and_state[:full_city_and_state.find('<br>')-6]
        location_state = city_and_state[city_and_state.rfind(' ')+1:]
        location_city = city_and_state[:city_and_state.find(location_state)]
        if location_state.upper() in two_words_states:
            location_state = city_and_state[city_and_state.rfind(' ')+1:]
            location_city = city_and_state[:city_and_state.find(location_state)-1]
            location_state = location_city[location_city.rfind(' ')+1:]+' '+location_state
            location_city = location_city[:location_city.rfind(' ')+1]
        location_description = ''
        full_description = driver.find_elements(By.CSS_SELECTOR,('section[class="section-text"] div[class="section__content"] p'))
        for p in full_description:
            location_description = location_description + p.text
        location_contact_name = ''
        try:
            location_contact_phone = driver.find_element(By.CSS_SELECTOR,('div[class="intro__content"] h1 + p a')).text
        except:
            location_contact_phone = ''    
        location_contact_email = ''
        location_URL = driver.current_url
        data.append({'Location Name':location_name,'Location Address':location_address,'Location City':location_city[0:-1],'Location State':location_state,'Location Description':location_description,'Location Contact Name':location_contact_name,'Location Contact Phone':location_contact_phone,'Location Contact Email':location_contact_email,'Location Website URL':location_URL}) 
        file = open('mysalonsuiteV3.json','w')
        file.write(json.dumps(data))
        file.close()       
main()        