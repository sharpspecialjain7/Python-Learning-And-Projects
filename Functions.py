def printFullName(firstName, lastName):
    fullName = firstName + " " + lastName
    print(fullName)


def returnName(name):
    return name


printFullName("Abhishek", "Jain")
printFullName("Jain", "Abhishek")
printFullName(firstName="Disha", lastName="Jain")
printFullName(lastName="Jain", firstName="Disha")


myName = returnName(name="Champion")
print(myName)
