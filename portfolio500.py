from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get('https://sea.500.co/startups?filter=1&region=&sector=&platform=')

while True:
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='btn btn-primary']"))).click()        
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Load More')]"))).click()        
    except Exception as ex:
        if 'intercepted' in str(ex):
            print(str(ex))
            pass
        else:
            break


containers = driver.find_elements(By.XPATH,'//tbody[@id="portfolioContainer"]/tr')
for container in containers:
    # print(container)
    try:
        name = container.find_element(By.XPATH,'.//td[@class="portfolio-name"]').text
        website = container.find_element(By.XPATH,'.//td[@class="portfolio-url"]/a').get_attribute('href')
        country = container.find_element(By.XPATH,'.//td[@class= "portfolio-country"]').text
        platform = container.find_element(By.XPATH,'.//td[@class="portfolio-platform"]').text
        sector = container.find_element(By.XPATH,'.//td[@class="portfolio-sector"]').text
    except:
        name = ''
        website = ''
        country = ''
        platform = ''
        sector = ''
    print(name, website, country, sector, platform)

driver.quit()