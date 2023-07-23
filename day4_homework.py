from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class Saucedemo:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window()


    def noUsername(self):
        username = self.driver.find_element(By.NAME,"user-name")
        username.send_keys("")
        sleep(2)
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        button = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/input")
        button.click()
        if username == "":
            errorMessage.clear()
            errorMessage.send_keys("Du Hund")
            sleep(2)
        sleep(5)





saucedemo = Saucedemo()
saucedemo.noUsername()