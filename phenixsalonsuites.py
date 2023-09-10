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
    driver.get('https://phenixsalonsuites.com/locations-list/')
    driver.implicitly_wait(5)
    driver.maximize_window()
def gather_links():
    links=[]
    anchors = driver.find_elements(By.CSS_SELECTOR,('div[class="location_details_page_link"] a'))
    for a in anchors:
        links.append(a.get_attribute('href'))
    return links    
def gather_data(links):
    for link in links:
        driver.get(link)
        location_name = driver.find_element(By.CSS_SELECTOR,('div[class="firstloc_section_left"] h2')).text
        location_address = driver.find_element(By.CSS_SELECTOR,('div[class="location_adress"]')).text
        location_city = driver.find_elements(By.CSS_SELECTOR,('div[class="location_tot"] span'))[0].text
        location_state = driver.find_elements(By.CSS_SELECTOR,('div[class="location_tot"] span'))[1].text
        location_description = ''
        location_contact_name = ''
        location_contact_phone = driver.find_element(By.CSS_SELECTOR,('div[class="location_phone"] a')).text
        location_contact_email = ''
        location_URL = driver.current_url
        data.append({'Location Name':location_name,'Location Address':location_address,'Location City':location_city[0:-1],'Location State':location_state,'Location Description':location_description,'Location Contact Name':location_contact_name,'Location Contact Phone':location_contact_phone,'Location Contact Email':location_contact_email,'Location Website URL':location_URL}) 
        file = open('phenissalonsuitesDATA.json','w')
        file.write(json.dumps(data))
        file.close()       
main()        