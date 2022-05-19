"""NOTES
1. Python is not “statically typed”. We don't need to use the data type before variable declaration.
2. The value stored in a variable can be changed during program execution.
3. Rules for creating variables in Python
    a. must start with a letter or the underscore character
    b. cannot start with a number
    c. can only contain alpha-numeric characters and underscores
    d. names are case-sensitive
    e. cannot be a reserved word
4. Local variables are the ones that are defined and declared inside a function. We can not call this variable outside the function.
5. Global variables are the ones that are defined and declared outside a function, and we need to use them inside a function.    
"""

name = "Abhishek"
age = "31"
monthly_salary = 1234.56

print(name, age, monthly_salary, sep="\t")

# reuse of variable
monthly_salary = 2345.67
print(monthly_salary)

# assigning single value to multipe variables
a = b = c = 10
print(a, b, c, sep="\t")

# assigning different values to multiple variables
d, e, f = 1, 2.2, "Hello"
print(d, e, f, sep="\t")

# string concatenation
firstName = "Abhishek"
secondName = "Jain"
print(firstName + secondName)
