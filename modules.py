#alias - takmaad: Dosyalari farkli bir isim ile cagirmak
#takmaad sadece bu dosyaya gecerli
import mathmatics as test_import

#kütüphane
import random 

from day3 import Human 

#sadece bazi fonsiyonlari cagirmak
from mathmatics import multiplication,devision #as function

#print(test_import.multiplication(10, 20))  if whole module was imported
print(multiplication(10, 5))   #if only a certain part of code was imported

print(random.randint(0, 100))  #raskele sifir ile yüz arasi sayi üretiyor

human4 = Human("Ersan", "HI")
human4.talk()