"""
main.py
"""


from Data import data
from Locator import locator


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class LoginPage:


   def __init__(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


   def boot(self):
       self.driver.get(data.WebData().url)
       self.driver.maximize_window()
       self.driver.implicitly_wait(10)


   def quit(self):
       self.driver.quit()


   def enterText(self, locator, textValue):
       element = self.driver.find_element(by=By.ID, value=locator)
       element.clear()
       element.send_keys(textValue)


   def clickButton(self, locator):
       self.driver.find_element(by=By.ID, value=locator).click()


   def login(self):
       try:
           self.boot()


           # Username = 4
           # Password = 5
           # Test Results = 6


           # Rows - 2 to End


           for row in range(2, data.WebData().rowCount()+1):
               username = data.WebData().readData(row, 2)
               password = data.WebData().readData(row, 3)


               self.enterText(locator.WebLocators().usernameLocator, username)
               self.enterText(locator.WebLocators().passwordLocator, password)
               self.clickButton(locator.WebLocators().buttonLocator)


               self.driver.implicitly_wait(10)


               if self.driver.current_url == data.WebData().dashboardURL:
                   print("Successfully Loggedin")
                   data.WebData().writeData(row, 6, "PASSED")


                   # Logout
                   self.clickButton(locator.WebLocators().ButtonLocator)
                   self.clickButton(locator.WebLocators().logoutButton)
               else:
                   print("Login unsuccessfull")
                   data.WebData().writeData(row, 6, "FAILED")




       except NoSuchElementException as e:
           print(e)
       finally:
           self.quit()


obj = LoginPage()
obj.login()

