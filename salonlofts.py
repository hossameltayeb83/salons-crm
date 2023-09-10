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
    driver.get('https://salonlofts.com/salons')
    driver.implicitly_wait(5)
    driver.maximize_window()
def gather_links():
    links=[]
    anchors = driver.find_elements(By.CSS_SELECTOR,('div[id="footer"] > div:nth-child(2) a'))
    for a in anchors:
        links.append(a.get_attribute('href'))
    return links

        


def gather_data(links):
    for link in links:
        driver.get(link)
        driver.find_element(By.CSS_SELECTOR,('a[class="btn banner-bottom-side-button"]')).click()
        location_contact_1_name = ''
        location_contact_1_phone = ''
        
        location_contact_2_name = ''
        location_contact_2_phone = ''
        
        location_contact_3_name = ''
        location_contact_3_phone = ''
        
        location_contact_4_name = ''
        location_contact_4_phone = ''
        
        number_of_contacts = len(driver.find_elements(By.CSS_SELECTOR,('ul[class*="market-managers"] li')))
        print(number_of_contacts)
        if number_of_contacts == 1:
            location_contact_1_name = driver.find_elements(By.CSS_SELECTOR,('ul[class*="market-managers"] li div[class="name"]'))[0].text
            location_contact_1_phone = driver.find_elements(By.CSS_SELECTOR,('ul[class*="market-managers"] li div[class="phone"]'))[0].text
        elif number_of_contacts == 2:
            location_contact_1_name = driver.find_elements(By.CSS_SELECTOR,('ul[class*="market-managers"] li div[class="name"]'))[0].text
            location_contact_1_phone = driver.find_elements(By.CSS_SELECTOR,('ul[class*="market-managers"] li div[class="phone"]'))[0].text
            location_contact_2_name = driver.find_elements(By.CSS_SELECTOR,('ul[class*="market-managers"] li div[class="name"]'))[1].text
            location_contact_2_phone = driver.find_elements(By.CSS_SELECTOR,('ul[class*="market-managers"] li div[class="phone"]'))[1].text
        elif number_of_contacts ==3:
            location_contact_1_name = driver.find_elements(By.CSS_SELECTOR,('ul[class*="market-managers"] li div[class="name"]'))[0].text
            location_contact_1_phone = driver.find_elements(By.CSS_SELECTOR,('ul[class*="market-managers"] li div[class="phone"]'))[0].text
            location_contact_2_name = driver.find_elements(By.CSS_SELECTOR,('ul[class*="market-managers"] li div[class="name"]'))[1].text
            location_contact_2_phone = driver.find_elements(By.CSS_SELECTOR,('ul[class*="market-managers"] li div[class="phone"]'))[1].text    
            location_contact_3_name = driver.find_elements(By.CSS_SELECTOR,('ul[class*="market-managers"] li div[class="name"]'))[2].text
            location_contact_3_phone = driver.find_elements(By.CSS_SELECTOR,('ul[class*="market-managers"] li div[class="phone"]'))[2].text
        else:
            location_contact_1_name = driver.find_elements(By.CSS_SELECTOR,('ul[class*="market-managers"] li div[class="name"]'))[0].text
            location_contact_1_phone = driver.find_elements(By.CSS_SELECTOR,('ul[class*="market-managers"] li div[class="phone"]'))[0].text
            location_contact_2_name = driver.find_elements(By.CSS_SELECTOR,('ul[class*="market-managers"] li div[class="name"]'))[1].text
            location_contact_2_phone = driver.find_elements(By.CSS_SELECTOR,('ul[class*="market-managers"] li div[class="phone"]'))[1].text    
            location_contact_3_name = driver.find_elements(By.CSS_SELECTOR,('ul[class*="market-managers"] li div[class="name"]'))[2].text
            location_contact_3_phone = driver.find_elements(By.CSS_SELECTOR,('ul[class*="market-managers"] li div[class="phone"]'))[2].text    
            location_contact_4_name = driver.find_elements(By.CSS_SELECTOR,('ul[class*="market-managers"] li div[class="name"]'))[3].text
            location_contact_4_phone = driver.find_elements(By.CSS_SELECTOR,('ul[class*="market-managers"] li div[class="phone"]'))[3].text    
        driver.get(link)
        locations_names = driver.find_elements(By.CSS_SELECTOR,('li[class="store-details"] span'))
        locations_URLs =  driver.find_elements(By.CSS_SELECTOR,('li[class="store-details"] a'))
        locations_addresses = driver.find_elements(By.CSS_SELECTOR,('li[class="store-details"] div[class="address-1"]'))
        locations_cities_and_states = driver.find_elements(By.CSS_SELECTOR,('li[class="store-details"] div[class="address-2"]'))
        for i in range(0,len(locations_names)):          
            location_name = locations_names[i].text
            location_address = locations_addresses[i].text
            city_and_state = locations_cities_and_states[i].text.strip()
            location_city = city_and_state[:city_and_state.find(',')]
            location_state = city_and_state[city_and_state.find(',')+2:-6]
            location_description = ''       
            location_URL = locations_URLs[i].get_attribute('href')
            data.append({'Location Name':location_name,
                        'Location Address':location_address,
                        'Location City':location_city,
                        'Location State':location_state,
                        'Location Description':location_description,
                        'Contact 1 - Contact Name':location_contact_1_name,
                        'Contact 1 - Contact Phone Number':location_contact_1_phone,                      
                        'Contact 2 - Contact Name':location_contact_2_name,
                        'Contact 2 - Contact Phone Number':location_contact_2_phone,                       
                        'Contact 3 - Contact Name':location_contact_3_name,
                        'Contact 3 - Contact Phone Number':location_contact_3_phone,                       
                        'Contact 4 - Contact Name':location_contact_4_name,
                        'Contact 4 - Contact Phone Number':location_contact_4_phone,                       
                        'Location Website URL':location_URL}) 
            file = open('salonlofts.json','w')
            file.write(json.dumps(data))
            file.close()       
main()        