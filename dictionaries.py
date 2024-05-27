#dictionaries allow us to work with key-value pairs: two linked values, where key is unique identifier where we can find our data & value is that data (hashmaps or associative arrays in other coding languages)

student = {'name': 'Jake', 'age': 24, 'courses': ['philosophy', 'compsci']} #name is a string, age is integer, and courses is a list (values in dictioanry can be anything)

student['phone'] = '555-5555' #adds new keys

student.update({'name': 'Jane', 'age': 26, 'phone': '666-6666'}) #updates keys and adds keys all-in-one

del student['courses'] #deletes a specific key

age = student.pop('age') #pops off (deletes) a specific key and then can print and tell you what got deleted
print(age)

print(student)

print(student['name']) #print specific key

print(student.get('weight', 'Not Found')) #indicates when a key doesn't exist

print(len(student)) #gives number of keys
print(student.keys()) #gives keys
print(student.values()) #gives values
print(student.items()) #gives key & value pairs

for key, value in student.items(): #A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)
    print(key, value)
