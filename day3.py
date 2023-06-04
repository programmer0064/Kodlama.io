from human import Human
from selenium import webdriver

human1 = Human("Berk", "Merhaba")
#human1.name = "Berk"    -   DRY

human2 = Human("Beren", "Hallo")
#human2.name = "Beren"   -   DRY

Human("Hava", "Merhaba").talk()

human1.talk()
human2.talk()
human1.walk()
human2.walk()
print(human1)
print(human2)


#packages
chromeDriver = webdriver.Chrome()