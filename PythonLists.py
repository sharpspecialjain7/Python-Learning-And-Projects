"""NOTES
1. dynamically sized arrays
2. list may contain DataTypes like Integers, Strings, as well as Objects
3. Not required to be homogenous
4. Lists are mutable, and hence, they can be altered even after their creation.
5. List in Python are ordered and have a definite count
6. duplicates are allowed
7. Lists are a useful tool for preserving a sequence of data and further iterating over it.
"""

# empty list
list = []
print(list)

# list of numbers
list = [10, 1, 2]
print(list)

# accessing list
print(list[0])
print(list[1])
print(list[2])

# multidimensional list
list = [[1, 2], [3, 4]]
print(list)
print(list[0])
print(list[1])
print(list[0][0])
print(list[0][1])
print(list[1][0])
print(list[1][1])

# list with mixed types
list = ["Hello", 1, 1.25, True]
print(list)

# size of list
print(len(list))

# appending in a list
list.append("World")
print(list)

# adding tuples
list.append((1.5, 2.5))
print(list)

# appending a list to list
list.append([5,9])
print(list)

list[5] = "New"
print(list)