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
    driver.get('https://imagestudios360.com/locations/')
    driver.implicitly_wait(5)
    driver.maximize_window()
def gather_links():
    links=[]
    anchors = driver.find_elements(By.CSS_SELECTOR,('div[class="locations_list_column"] a'))
    for a in anchors:
        links.append(a.get_attribute('href'))
    return links    
def gather_data(links):
    for link in links:
        driver.get(link)
        location_name = driver.find_element(By.CSS_SELECTOR,('h1')).text[16:]
        full_address = driver.find_element(By.CSS_SELECTOR,('div[class="salon_address"]')).text
        location_state = location_name[-2:]
        location_city = full_address[full_address.find(',')+2:full_address.rfind(',')]
        if ',' in location_city:
            location_city = location_city[location_city.find(',')+2:]
            location_address = full_address[:full_address.find(location_city)-2]
        else:    
            location_address = full_address[:full_address.find(',')]
        location_description = ''
        full_contact_name = driver.find_element(By.CSS_SELECTOR,('div[class="pro_location"]')).text
        if ':' in full_contact_name:
            location_contact_name = full_contact_name[full_contact_name.find(':')+2:]
        else:
            location_contact_email = full_contact_name[1:]    
        try:
            location_contact_phone = driver.find_element(By.CSS_SELECTOR,('div[class="salon_phone"] a')).text
        except:
            location_contact_phone = ''    
        location_contact_email = ''
        location_URL = driver.current_url
        data.append({'Location Name':location_name,'Location Address':location_address,'Location City':location_city,'Location State':location_state,'Location Description':location_description,'Location Contact Name':location_contact_name,'Location Contact Phone':location_contact_phone,'Location Contact Email':location_contact_email,'Location Website URL':location_URL}) 
        file = open('imagestudios360.json','w')
        file.write(json.dumps(data))
        file.close()       
main()        