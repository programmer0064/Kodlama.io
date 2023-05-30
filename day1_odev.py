students = ["Mert", "Oguzhan", "Merve", "Esra"]
print(students[0])
students.append("Orhan")
for student in students:
    print(student)

print("\n")

students.pop()   #-1 by default: deletes last item in the list 
print(students)

print("\n")

students.remove("Oguzhan")
print(students)

print("\n")

students.extend(["Hamsa", "Mehmet"])
print(students)

print("\n")

for i in range(len(students)):
    print(students[i])    

print("\n")

i=0
while i<10:    #for döngüsünde i bir bir arttiliyor ama while de degil
    print(i)
    break

print(("\n"))
print(("**************************************"))
print(("\n"))

test_format = "test"
print(f"This is a {test_format}")

sayi1 = 5

def test():
    sayi2 = sayi1
    print(sayi2)

test()