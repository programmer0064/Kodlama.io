from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#driver = webdriver.Chrome(ChromeDriverManager().install())
#                             class                function

driver.maximize_window()
driver.get("https://www.google.com/")   #opens this url when driver gets started                     #closes program after 10s

sleep(2)

cookies_button = driver.find_element(By.ID,"W0wltc")
cookies_button.click()

sleep(2)

input = driver.find_element(By.NAME,"q")
print(f"Input: {input}")                  #name of input is q and it is a web-element; elementi nasil locate edebiliyorsak, onu tanitmamiz gerek ve name de unique bir info
input.send_keys("kodlamaio")
#input.submit()
sleep(2)
search_button = driver.find_element(By.NAME,"btnK")      #suchen
search_button.click()

sleep(5)

link_of_website = driver.find_element(By.XPATH,"/html/body/div[6]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a/h3")    #kodlamaio  
link_of_website.click()

sleep(2)

listOfCourses = driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"Number of courses on kodlama.io: {len(listOfCourses)}")


while True:
    continue

driver.close()

# HTML LOCATORS    #html elementlerin yerini bul

#Full X-Path
#/html/body/div[6]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a  
#yeni html element eklendiginde path degisecek
#en tepeden basliyor

#X-Path
#//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a
#en yakin unique alanindan basliyor ve ilgilendigimiz elemente kadar gidiyor

#web scraping