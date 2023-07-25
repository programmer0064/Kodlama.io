vade = int(input("Lütfen istediginiz vade sayisini giriniz: "))
print(type(vade))
vade = vade + 12

print("Girdiginiz vade: " + str(vade))
print("Girdiginiz vade: {vade_sayisi}" .format(vade_sayisi = vade))

name = "Berk"
print(f"My name is {name}")

print(f"The number is {1+1}")

def calculateWithParams(price, money):
    print(money-price)

calculateWithParams(80, 100)

def calculateNewPrice (price, discount):
    return price - discount     #neden print degil: cünkü print de sadece ekrana yazar, ama ben degeri ele alabilmek istiyorum ve onunla bir sey yapmak istiyorum yani print demek "ekrana yaz ve at" demek; bir degisken mis gibi kullanbiliyoruz return keyword ile

newPrice = calculateNewPrice(100, 20)
print(newPrice)

