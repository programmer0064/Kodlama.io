from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#driver = webdriver.Chrome(ChromeDriverManager().install())
#                             class                function
driver.maximize_window()
driver.get("https://www.google.com/")   #opens this url when driver gets started
# sleep(10)                      #closes program after 10s
input = driver.find_element(By.NAME,"q")
print(f"Input: {input}")
while True:
    continue
# HTML LOCATORS    #html elementlerin yerini bul