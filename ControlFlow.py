"""
We will go over:
1. if else
2. if elif else
3. nested ifs
4. switch
"""

# if else control flow
isTrue = True

if isTrue:
    print("This is True")
else:
    print("This is false")


# if .. elif ..else

age = 17
if age > 18:
    print("your age is greater than 18")
elif age >= 18:
    print("your age is 18")
else:
    print("you are less than 18")


# nested if else
    if isTrue:
        if age > 18:
            print("your age is greater than 18")
        elif age >= 18:
            print("your age is 18")
        else:
            print("you are less than 18")
    else:
        print("False")


# conditional and or not
number = 15
# or logic
if number > 10 or number < 5:
    print("number is > 10 or < than 5")

name = "Abhishek"
# and logic
if number > 10 and name[0] == 'A':
    print("condition matched")
else:
    print("no match")

# not logic
if number > 10 and not name[0] == 'B':
    print("not condition matched")
else:
    print("no match")