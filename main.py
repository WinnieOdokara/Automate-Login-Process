from selenium import webdriver
from selenium.webdriver.common.keys import Keys # Return the 'Enter' key to login to the website. (line 26: + Keys.RETURN) 
import time # to give time between operations: 2 seconds (line 24 & 26)
 
def get_driver():
## Ste options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://automated.pythonanywhere.com/login/")
  return driver


def main():
  driver = get_driver()
## Login, password, Enter
  element = driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)   
  time.sleep(2)
## Click home button 
  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  print(driver.current_url)

  
  # 'automate' is the username for the login (line 23)
  # 'automatedautomated' password for the login (line 25)
  # output url after login (line 29)
  # If it doesn't have the 'return' statment, when testing, Python returns a 'None' object 

# XPath: In Selenium automation, if the elements are not found by the general locators like ID, class, name, etc., then XPath is used to find an element on the web page

print(main())
