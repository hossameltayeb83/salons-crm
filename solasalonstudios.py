#https://www.solasalonstudios.com/locations
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.chrome.options import Options
import json
import time

options = Options()


options.add_argument('--headless=new')
options.add_argument("--window-size=1920,1080")
data =[]
driver = webdriver.Chrome()
def main():
    config()
    
    gather_data()
def config():
    driver.get('https://www.solasalonstudios.com/locations')
    driver.implicitly_wait(5)
    driver.maximize_window()
def gather_data():
    driver.find_element(By.CSS_SELECTOR,('button[aria-label="ACCEPT AND CONTINUE"]')).click()
    locations = driver.find_elements(By.CSS_SELECTOR,('div[class*="all-"] span'))
    
    for i in range(0,len(locations)):
        location = driver.find_elements(By.CSS_SELECTOR,('div[class*="all-"] span'))[i].click()
        try:
            location_name = driver.find_element(By.CSS_SELECTOR,('div[class="app__wrapper_info detail-text-wrapper MuiBox-root css-0"] p:nth-of-type(2)')).text
        except NoSuchElementException:
            time.sleep(1)
            location_name = driver.find_element(By.CSS_SELECTOR,('div[class="app__wrapper_info detail-text-wrapper MuiBox-root css-0"] p:nth-of-type(2)')).text    
        full_address = driver.find_element(By.CSS_SELECTOR,('div[class*="contact-info"] span')).text
        location_state = full_address[full_address.rfind(',')+2:full_address.rfind(',')+4]
        half_address = full_address[:full_address.rfind(',')]
        location_city = half_address[half_address.rfind(',')+2:]
        location_address = half_address[:half_address.find(location_city)-2]
        location_URL = driver.current_url
        location_description =''
        full_description = driver.find_elements(By.CSS_SELECTOR,('div[class="MuiBox-root css-1dimjgw"] p:nth-child(2) p'))
        for p in full_description:
            location_description = location_description + p.text
        driver.find_element(By.CSS_SELECTOR,('div[class="cta-action MuiBox-root css-1ebnygn"] button')).click()
        contact_info = driver.find_elements(By.CSS_SELECTOR,('p[class="MuiTypography-root MuiTypography-body1 font18-light with-responsive color-secondary css-9l3uo3"]'))
        try:
            location_contact_name = contact_info[0].text

            location_contact_phone = contact_info[1].text
            location_contact_email = contact_info[2].text
        except:
            location_contact_name = ''

            location_contact_phone = ''
            location_contact_email = ''   
        data.append({'Location Name':location_name,'Location Address':location_address,'Location City':location_city,'Location State':location_state,'Location Description':location_description,'Location Contact Name':location_contact_name,'Location Contact Phone':location_contact_phone,'Location Contact Email':location_contact_email,'Location Website URL':location_URL})
        driver.get('https://www.solasalonstudios.com/locations')

        file = open('data5.json','w')
        file.write(json.dumps(data))
        file.close()

main()            
