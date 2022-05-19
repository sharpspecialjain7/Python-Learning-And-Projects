from math import floor
import random

random_number = random.randint(0, 5)
print(random_number)

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.choice(list_of_numbers))

random = random.random()
print(floor(random * 5))
