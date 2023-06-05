from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_Kodlamaio:
    def test_invalid_login(self): #kisinin dogru giris yapip yapmadigini test ediyor
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.youtube.com/redirect?event=live_chat&redir_token=QUFFLUhqa3lWWUVEQjVwazdiZjZOeHd2a01BQzhydFB3Z3xBQ3Jtc0tuNlcya0R0b1lXZWpLdExKYkZKb0czdWV5b0NoZXJ4ODBtWk9aZFFFNGVHOE9nTjhpS1ljU0tzalhkNUlzbGJQZnVNUHBFaHBfWmZ0WFlCbTFiMm92YVFWOGh3Y3ZFZDRYdzBhb2l0cVFZdTFpbmtaSQ&q=https%3A%2F%2Fwww.saucedemo.com%2F")
        #sleep(2)
        website_aufrufen = driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/a[1]")
        website_aufrufen.click()
        #sleep(2)
        usernameInput = driver.find_element(By.ID,"user-name")
        password = driver.find_element(By.ID,"password")
        #sleep(2)
        usernameInput.send_keys("1")
        password.send_keys("1")
        #sleep(2)
        login = driver.find_element(By.ID,"login-button")
        login.click()
        #sleep(2)
        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(errorMessage)
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"Test Sonucu: {testResult}")
        
        """
        username = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")
        username.send_keys("standard_user")
        sleep(2)
        password = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")
        password.send_keys("secret_sauce")
        sleep(2)
        login = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/input")
        login.click()
        sleep(30)
        """

        """
        loginBtn = driver.find_element(By.XPATH,"/html/body/header/div/div/div/div/ul/li[3]/a")
        loginBtn.click()
        sleep(300)
        """

test_kodlamaio = Test_Kodlamaio()
test_kodlamaio.test_invalid_login()
