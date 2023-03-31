# Arna Togayeva
# Lupita's lookup app

import json


pathToFile = "/Users/arna.togayeva/Documents/GitHub/lupita/src/birthday.json"


# try to open a file and throw a error if it is not found
try:
    jsonFile = open(pathToFile, 'r')
except OSError:
    print("ERROR: Unable to open the file %s" % pathToFile)
    exit(-1)


# read the whole json file into a variable
birthdayList = json.load(jsonFile)

# create an empty dictionary
birthdayDictionary = {}

# loop json list of data and put each name and birthday into a dictionary
for elem in birthdayList:

    # fetch name and birthday
    name = elem["name"]
    birthday = elem["birthday"]

    #print("name = " + name)
    #print("birthday = " + birthday)

    birthdayDictionary[name] = birthday


# to print a value in the dictionary by giving it a string with the name as the key
#print("Jocelyn Jones's birthday is: " + birthdayDictionary["Jocelyn Jones"])

# to get user input
name = str(input("Enter a name: "))
# print("name = " + name)

nameLow = name.lower()

# if name in birthdayDictionary:
   # print("His/her birthday is " + birthdayDictionary[name])
#else:
#    print("Lupe doesn't have a friend that matches the name " + name)


# convert keys to lower case in birthdayDictionary 
# search name in lower case keys
substring_key = [key for key, value in birthdayDictionary.items() if nameLow in key.lower()]
substring_value = [value for key, value in birthdayDictionary.items() if nameLow in key.lower()]

# combine key and value, print with left aligned width 
if substring_key and substring_value:
    print("Lupe's friends that match the name " + name + " are:")
    print("--------------------------  ---------------")
    print("Name                         Birthday")
    print("--------------------------  ---------------")
    for key, value in zip(substring_key, substring_value):
        print("%-20s" % key + "       " +  "%-10s" % value)
else:
    print("Lupe does not have any friends that matche the name " + name)