def printFullName(firstName, lastName):
    """Returns full name"""
    fullName = firstName + " " + lastName
    print(fullName)


def returnName(name):
    """Returns name"""
    return name


printFullName("Abhishek", "Jain")
printFullName("Jain", "Abhishek")
printFullName(firstName="Disha", lastName="Jain")
printFullName(lastName="Jain", firstName="Disha")


myName = returnName(name="Champion")
print(myName)
