students_class = ["Mehmet Ünlü", "Orhan Gündogan", "Serkan Aydogan", "Gürsoy Sancakli"]

def printStudentsOnScreen(students):
    print("The class exists of " + str(len(students_class)) + " students and in the class are: ")
    for i in students_class:
        print(i) 


def addStudent(students):
    while True:    
        addstudent = input("Do you want to add a student? Type in yes or no:    ") 
        if addstudent == "yes":
            studentname = input("Type in the student's name: ")
            students.append(studentname)
            print("The class now exists of " + str(len(students)) + " students: ")
            for i in students:
                print(i)
            break

        elif addstudent == "no":
            print("Alright thanks for the answer")
            break
            
        else:
            print("No eglible answer to the question, try again!") 


def deleteStudent(students):
    while True:
        deletestudent = input("Do you want to delete a student? Type in yes or no:    ")
        if deletestudent == "yes":
            studentname = str(input("Type in the student's name: "))
            students.remove(studentname)
            print("The class now exists of " + str(len(students)) + " students: ")
            for i in students:
                print(i)
            break

        elif deletestudent == "no":
            print("Alright thanks for the answer")
            break
            
        else:
            print("No eglible answer to the question, so try again!")
        

def addMoreThanOneStudent(students):
    while True:    
        addstudent=input("Do you want to add more than one student? yes/no ")
        if addstudent == "yes":     
            numberofstudents = int(input("How many students do you want to add? "))
            i=0
            for i in range(numberofstudents):
                name = input("What is the name of the student? ")
                students.append(name)
            print("Students are added. Now the class exists of the following students: ")
            for i in students:
                print(i)
            break

        elif addstudent == "no":
            print("Alright thanks for the answer")
            break

        else:
            print("No eglible answer to the question, so try again!")



def indexOfStudent(students):
    name = input("I can give you the index number of each student in the list. Which student are you looking for? ")
    print(f"Student with the name {name} has the index number: " + str(students.index(name)))


def deleteMoreThanOneStudent(students):
    while True:
        deletestudent=input("Do you want to delete more than one student? yes/no ")
        if deletestudent == "yes":     
            numberofstudents = int(input("How many students do you want to delete? "))
            i=0
            for i in range(numberofstudents):
                name = input("What is the name of the student? ")
                students.remove(name)
            print("Students are deleted from list. Now the class exists of the following students: ")
            for i in students:
                print(i)
            break
        elif deletestudent == "no":
            print("Alright thanks for the answer!")
            break
        else:
            print("No eglible answer to the question, so try again!")


printStudentsOnScreen(students_class)
print("\n")
addStudent(students_class)
print("\n")
deleteStudent(students_class)
print("\n")
addMoreThanOneStudent(students_class)
print("\n")
indexOfStudent(students_class)
print("\n")
deleteMoreThanOneStudent(students_class)