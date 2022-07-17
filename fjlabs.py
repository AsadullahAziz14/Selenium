from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC



# s=Service(r'C:\Users\Asadullah\Desktop\selenium\chromedriver.exe')
# browser = webdriver.Chrome(service=s)
# url='https://www.google.com'
# browser.get(url)

driver = webdriver.Chrome()
# driver = webdriver.Chrome(service=Service(r'C:\Users\Asadullah\Desktop\selenium\chromedriver.exe'))
driver.get('https://fjlabs.com/portfolio/')
height = 0

while True:
    new_height = driver.execute_script("return document.body.scrollHeight")
    if height == new_height:
        break
    driver.find_element(By.TAG_NAME,"body").send_keys(Keys.END)
    time.sleep(3)
    height = new_height
    print(height)

containers = driver.find_elements(By.XPATH,'//div[@id="companies"]')

for container in containers:
    # print(container)
    title = container.find_element(By.XPATH,'.//img[@class="Centered img-hide"]').get_attribute('alt')
    link = container.find_element(By.XPATH,'.//a[@target="_blank"]').get_attribute('href')
    year = container.find_element(By.XPATH,'.//span[@class="year"]').get_attribute('innerText')
    stage = container.find_element(By.XPATH,'.//span[@class="investment_stage"]').get_attribute('innerText')
    desc = container.find_element(By.XPATH,'.//div[@class="description"]').get_attribute('innerText')

    print(title,link,year,stage,desc)

driver.quit()

