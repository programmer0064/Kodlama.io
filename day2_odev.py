students_class = ["Mehmet Ünlü", "Orhan Gündogan", "Serkan Aydogan", "Gürsoy Sancakli"]
print("The class exists of " + str(len(students_class)) + " students and in the class are: ")
for i in students_class:
    print(i)

print("\n") 

def addStudent(students):
    addstudent = input("Do you want to add a student? Type in yes or no:    ")
    print("\n") 

    do{
        if addstudent == "yes":
        studentname = input("Type in the student's name: ")
        students.append(studentname)
        print("The class now exists of " + str(len(students)) + " students: ")
        for i in students:
            print(i)

    elif addstudent == "no":
        print("Alright thanks for the answer")
    
    else:
          exit("No eglible answer to the question. So try again!")
          } while(addstudent == "yes" or addstudent == "no"); 

print("\n")

def deleteStudent(students):
    deletestudent = input("Do you want to delete a student? Type in yes or no:    ")
    print("\n") 

    if deletestudent == "yes":
        studentname = str(input("Type in the student's name: "))
        students.remove(studentname)
        print("The class now exists of " + str(len(students)) + " students: ")
        for i in students:
            print(i)

    elif deletestudent == "no":
        print("Alright thanks for the answer")
    
    else:
          exit("No eglible answer to the question")

print("\n")



addStudent(students_class)
deleteStudent(students_class)