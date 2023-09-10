#https://salonsbyjc.com/search/?geodir_search=1&stype=gd_locations&slocation_services_select%5B%5D=&sopen_now=&s=+&snear=&sgeo_lat=&sgeo_lon=

from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
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
    filet = open('byjc.text')
    reader = filet.read()
    links = reader.split("\n")
    
    filet.close()
       
    #links = gather_links()
    gather_data(links[:-1])
def config():
    driver.get('https://salonsbyjc.com/search/?geodir_search=1&stype=gd_locations&slocation_services_select%5B%5D=&sopen_now=&s=+&snear=&sgeo_lat=&sgeo_lon=')
    driver.implicitly_wait(5)
    driver.maximize_window()
'''def gather_links():
    links=[]
    results = driver.find_element(By.CSS_SELECTOR,('div[class="counter"]')).text
    count = results[:results.find(' S')]
    print(count)
    while True:
        anchors = driver.find_elements(By.CSS_SELECTOR,('div[class*="card"] h2 a'))
        print(len(anchors))
        
        
        time.sleep(10)
        try:
            driver.find_element(By.CSS_SELECTOR,('div[class*="loop-paging"] button')).click()
        except ElementNotInteractableException:
            time.sleep(8)
            anchors = driver.find_elements(By.CSS_SELECTOR,('div[class*="card"] h2 a'))
            break

    print(len(anchors),' 13333')
    for a in anchors:
        links.append(a.get_attribute('href'))
    filex = open('byjc.text','w')
    for l in links:
        filex.write(l+'\n')
    filex.close()    
    return links'''    
def gather_data(links):
    for link in links:
        driver.get(link)
        print(link)
        location_name = driver.find_element(By.CSS_SELECTOR,('h1')).text               
        location_address = driver.find_element(By.CSS_SELECTOR,('span[itemprop="streetAddress"]')).text      
        location_city = driver.find_element(By.CSS_SELECTOR,('span[itemprop="addressLocality"]')).text
        location_state = driver.find_element(By.CSS_SELECTOR,('span[itemprop="addressRegion"]')).text       
        location_description = ''       
        location_contact_name = ''
        try:
            location_contact_phone = driver.find_element(By.CSS_SELECTOR,('div[class*="leasing_phone"] a')).text         
        except:
            location_contact_phone = driver.find_element(By.CSS_SELECTOR,('div[class*="field-phone"] a')).text   
        location_contact_email = ''
        location_URL = driver.current_url
        data.append({'Location Name':location_name,'Location Address':location_address,'Location City':location_city,'Location State':location_state,'Location Description':location_description,'Location Contact Name':location_contact_name,'Location Contact Phone':location_contact_phone,'Location Contact Email':location_contact_email,'Location Website URL':location_URL}) 
        file = open('salonsbyjc.json','w',encoding='utf-8')
        file.write(json.dumps(data))
        file.close()       
main()        