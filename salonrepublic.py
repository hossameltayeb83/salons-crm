#https://salonrepublic.com/locations/
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
driver = webdriver.Chrome()
data=[]
def main():
    config()
    links = gather_links()
    gather_data(links)
def config():
    driver.get('https://salonrepublic.com/locations/')
    driver.implicitly_wait(5)
    driver.maximize_window()
def gather_links():
    links=[]
    anchors = driver.find_elements(By.CSS_SELECTOR,('div[class="pt-cv-page"] > div a[class*="btn"]'))
    for a in anchors:
        links.append(a.get_attribute('href'))
    return links    
def gather_data(links):
    for link in links:
        driver.get(link)
        print(link)
        if driver.find_elements(By.CSS_SELECTOR,('div[id="loc_header"] h1')):
            location_name = driver.find_element(By.CSS_SELECTOR,('div[id="loc_header"] h1')).text
            full_address = driver.find_element(By.CSS_SELECTOR,('p[class="loc_address"]')).get_attribute('innerHTML').strip()
            
            state_and_city = full_address[:full_address.rfind('<br')]
            #location_state = state_and_city[-8:-6]
            location_state = state_and_city[state_and_city.rfind(',')+2:-6]
            location_city = state_and_city[state_and_city.rfind('"break">')+8:state_and_city.find(location_state)-2]
            location_address = full_address[0:full_address.find(location_city)].replace('<br class="break">','')
            
            location_description = driver.find_element(By.CSS_SELECTOR,('p[class="locations_desc"]')).text
            location_contact_name = ''
            location_contact_phone = driver.find_element(By.CSS_SELECTOR,('div[class="icon_tel"] + a')).text
            location_contact_email = driver.find_element(By.CSS_SELECTOR,('div[class="icon_email"] + a')).text
            location_URL = driver.current_url
            data.append({'Location Name':location_name,'Location Address':location_address,'Location City':location_city.replace('\n',' ').strip(),'Location State':location_state,'Location Description':location_description,'Location Contact Name':location_contact_name,'Location Contact Phone':location_contact_phone,'Location Contact Email':location_contact_email,'Location Website URL':location_URL}) 
        elif '/the-lab-hollywood/' in link:
            1    
        else:
            location_name = driver.find_element(By.CSS_SELECTOR,('div[id="lp-pom-text-12"]')).text
            full_address = driver.find_element(By.CSS_SELECTOR,('div[id="lp-pom-text-211"] p > span')).get_attribute('innerHTML').strip()
            location_address = full_address[:full_address.find('<br>')]
            full_city_and_state= full_address[len(location_address)+4:]
            city_and_state= full_city_and_state[:full_city_and_state.find('<br>')-7]
            location_state = city_and_state[city_and_state.rfind(' ')+1:]
            
            location_city = city_and_state[:city_and_state.find(location_state)-1]
            
            location_description = driver.find_element(By.CSS_SELECTOR,('div[id="lp-pom-text-13"] span')).text
            location_contact_name = ''
            location_contact_phone = driver.find_elements(By.CSS_SELECTOR,('div[id="lp-pom-text-211"] a'))[0].text
            location_contact_email = driver.find_elements(By.CSS_SELECTOR,('div[id="lp-pom-text-211"] a'))[1].text
            location_URL = driver.current_url
            data.append({'Location Name':location_name,'Location Address':location_address,'Location City':location_city,'Location State':location_state,'Location Description':location_description,'Location Contact Name':location_contact_name,'Location Contact Phone':location_contact_phone,'Location Contact Email':location_contact_email,'Location Website URL':location_URL})         
        file = open('salonrepublicV2.json','w')
        file.write(json.dumps(data))
        file.close()          
main()        