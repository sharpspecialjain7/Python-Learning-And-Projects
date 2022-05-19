# This file shows different variation that can be used with print() in python

# simple version of print function
print("Simply printing a string in python")
print("Hello")

# multiline print
print("\nMultiline printing a string in python")
hello = """Hello
World
"""
print(hello)

# Escape characters
print("Escape characters in python")
print("Hello\'")
print("Hello\"")
print("Hello\nWorld")
print("Hello\tWorld")

# Using single and double quotes together
print("\nPriting single and double quotes together")
print('Hello "World"')
print("Hello 'World'")

# The end keyword is used to specify the content that is to be printed at the end of the line
print("Using end argument in print()")
print("Hello",end=">>>>")
print()

# Flush in print. If it is set to true, the output will be written as a sequence of characters one after the other.
# String will not be buffered
print("\nDemonstrating flush in print()")
import time
count_seconds = 3
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        # change flush to True to observe the difference
        print(i, end=">>>",flush=False) 
        time.sleep(1)
    else:
        print('Start')

# using sep in print function. Default separator is space.
print("\nSeparator in print()")        
print("Hello","\t","World")
print("Hello","\t","World",sep=">>>")

