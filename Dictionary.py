"""NOTES
1. unordered collection of data values
2. Dictionary holds key:value pair
"""

# defining a dictionary
dict = {
    "Abhishek": 31,
    "Disha": 32,
    "Prateek": 31,
    "Swati": 29
}

# complex dictionary
complex_dict = {
    "Name": "Abhishek",
    "Age": 31,
    "Countries": ["India", "Norway", "Thailand"],
    "relatives": {
        "father": "Adish Jain",
        "mother": "RajKumari",
        "spouse": "Disha"}
}

# printing complete dictionary
# print(complex_dict)

# printing specific key
# print(complex_dict["relatives"])

# printing nested dictionary
# print(complex_dict["relatives"]["spouse"])

# adding to dictionary
complex_dict["relatives"]["sisters"] = ["Sheetal", "Vandana"]
# print(complex_dict)

# accessing list value from a nested dictionary value
# print(complex_dict["relatives"]["sisters"][0])

# looping through complex dictionary
for keys in complex_dict:
    if keys == "relatives":
        for relative in complex_dict["relatives"]:
            if relative == "sisters":
                sisters = complex_dict["relatives"][relative]
                for sis in sisters:
                    print(sis)
