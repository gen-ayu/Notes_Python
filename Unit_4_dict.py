# Python Dictionaries

# Dictionaries are one of the four built-in data types in Python used to store collections of data.
# The other three are List, Tuple and Set. Dictionaries store data as key:value pairs.

# Syntax: dictionary_name = {key : value}
student = {
    "name": "Ayush",
    "age": 19,
    "course": "B.Tech CSE"
}
print(student)
# Output: {'name': 'Ayush', 'age': 19, 'course': 'B.Tech CSE'}

# Dictionary Characteristics
# • Ordered (Python 3.7+)
# • Mutable (Items can be changed, added or removed) Dictionary keys are unique and immutable while its values can be mutable or immutable.
# • Does not allow duplicate keys
# • Duplicate values are allowed

student = {
    "name": "Ayush",
    "age": 19,
    "age": 20
}
print(student)
# Output: {'name': 'Ayush', 'age': 20} If duplicate keys are provided, the last value overwrites the previous one.

# Dictionary length can be found using the len() function.
student = {
    "name": "Ayush",
    "age": 19,
    "course": "B.Tech CSE"
}
print(len(student))
# Output: 3

# Dictionary values can be of any data type.
student = {
    "name": "Ayush",
    "age": 19,
    "cgpa": 8.5,
    "hosteller": True,
    "skills": ["Python", "Java"],
    "marks": (90, 85)
}

# Type of a dictionary can be found using the type() function.

print(type(student))

# Output:
# <class 'dict'>

# Dictionaries can also be created using the dict() constructor.
# Syntax: dict(key=value)

student = dict(name="Ayush", age=19, course="B.Tech CSE")

print(student)

# Output:
# {'name': 'Ayush', 'age': 19, 'course': 'B.Tech CSE'}


# Access Dictionary Items

# Dictionary items can be accessed using their key.
# Syntax: dictionary_name[key]

student = {
    "name": "Ayush",
    "age": 19,
    "course": "B.Tech CSE"
}

print(student["name"])

# Output:
# Ayush

# The get() method also returns the value of the specified key.
# Syntax: dictionary_name.get(key)

print(student.get("course"))

# Output:
# B.Tech CSE

# Unlike [], get() returns None if the key does not exist.

print(student.get("cgpa"))

# Output:
# None

# The keys() method returns all the keys of the dictionary.

print(student.keys())

# Output:
# dict_keys(['name', 'age', 'course'])

# The values() method returns all the values of the dictionary.

print(student.values())

# Output:
# dict_values(['Ayush', 19, 'B.Tech CSE'])

# The items() method returns the dictionary as key:value pairs.

print(student.items())

# Output:
# dict_items([('name', 'Ayush'), ('age', 19), ('course', 'B.Tech CSE')])

# Checking if a key exists can be done using the in keyword.

if "name" in student:
    print("Key exists")

# Output:
# Key exists


# Change Dictionary Items

# Dictionary values can be changed by assigning a new value to an existing key.
# Syntax: dictionary_name[key] = new_value

student["age"] = 20

print(student)

# Output:
# {'name': 'Ayush', 'age': 20, 'course': 'B.Tech CSE'}

# The update() method can also change existing values.
# Syntax: dictionary_name.update({key : value})

student.update({"course": "Computer Science"})

print(student)

# Output:
# {'name': 'Ayush', 'age': 20, 'course': 'Computer Science'}

# update() can also add a new key if it does not already exist.

student.update({"cgpa": 8.5})

print(student)

# Output:
# {'name': 'Ayush', 'age': 20, 'course': 'Computer Science', 'cgpa': 8.5}

# ----------------------------------------------------------------------------------------------

# Add Dictionary Items

# New items can be added by assigning a value to a new key or by using update().
# Syntax: dictionary_name[key] = value or dictionary_name.update({key:value})

student = {
    "name": "Perli",
    "age": 19,
    "course": "Tech"
}

student["cgpa"] = 8.5

print(student)

# Output: {'name': 'Perli', 'age': 19, 'course': 'Tech', 'cgpa': 8.5}

student.update({"hosteller": True})

print(student)

# Output: {'name': 'Perli', 'age': 19, 'course': 'Tech', 'cgpa': 8.5, 'hosteller': True}

# update() can also modify an existing key if it already exists.

student.update({"age": 20})

print(student)

# Output: {'name': 'Perli', 'age': 20, 'course': 'Tech', 'cgpa': 8.5, 'hosteller': True} Existing keys are updated.


# Remove Dictionary Items

# Dictionary items can be removed using pop(), popitem(), del and clear().

# pop() removes the specified key and returns its value.
# Syntax: dictionary_name.pop(key)

student.pop("hosteller")

print(student)

# Output: {'name': 'Perli', 'age': 20, 'course': 'Tech', 'cgpa': 8.5}

# popitem() removes the last inserted key:value pair.
# Syntax: dictionary_name.popitem()

student.popitem()

print(student)

# Output: {'name': 'Perli', 'age': 20, 'course': 'Tech'}

# del removes a specified key or the entire dictionary.
# Syntax: del dictionary_name[key]

del student["course"]

print(student)

# Output: {'name': 'Perli', 'age': 20}

# Syntax: del dictionary_name

student2 = {
    "name": "Perli",
    "age": 19
}

del student2

# print(student2)

# Output: NameError because the dictionary no longer exists.

# clear() removes all items but keeps the dictionary.
# Syntax: dictionary_name.clear()

student.clear()

print(student)

# Output: {}


# Loop Dictionaries

# Dictionaries can be looped through using a for loop.

student = {
    "name": "Perli",
    "age": 19,
    "course": "Tech"
}

# Loop through all keys.

for key in student:
    print(key)

# Loop through all values using values().

for value in student.values():
    print(value)

# Loop through all keys using keys().

for key in student.keys():
    print(key)

# Loop through both keys and values using items().

for key, value in student.items():
    print(key, ":", value)


# Copy Dictionaries

# Assigning one dictionary to another does not create a copy.
# Both variables refer to the same dictionary object.

student2 = student

student2["age"] = 20

print(student)
print(student2)

# Output: Both dictionaries become {'name': 'Perli', 'age': 20, 'course': 'Tech'}

# copy() creates a shallow copy of the dictionary.
# Syntax: dictionary_name.copy()

student2 = student.copy()

student2["age"] = 21

print(student)
print(student2)

# Output: student remains unchanged while student2 is modified.

# The dict() constructor can also be used to create a copy.
# Syntax: dict(dictionary_name)

student2 = dict(student)

print(student2)

# Output: {'name': 'Perli', 'age': 20, 'course': 'Tech'}

# Nested Dictionaries

# A dictionary can contain another dictionary as its value.
# This is known as a nested dictionary.

student1 = {
    "name": "Perli",
    "age": 19
}

student2 = {
    "name": "Alex",
    "age": 20
}

students = {
    "student1": student1,
    "student2": student2
}

print(students)

# Output: {'student1': {'name': 'Perli', 'age': 19}, 'student2': {'name': 'Alex', 'age': 20}}

# Nested dictionary items can be accessed using multiple keys.
# Syntax: dictionary[key1][key2]

print(students["student1"]["name"])

# Output: Perli


# Dictionary Methods

# fromkeys() creates a dictionary with the specified keys and a common value.
# Syntax: dict.fromkeys(keys, value)

keys = ("name", "age", "course")

student = dict.fromkeys(keys, "Not Assigned")

print(student)

# Output: {'name': 'Not Assigned', 'age': 'Not Assigned', 'course': 'Not Assigned'}

# get() returns the value of the specified key.
# Syntax: dictionary_name.get(key)

print(student.get("name"))

# Output: Not Assigned

# items() returns all key:value pairs.
# Syntax: dictionary_name.items()

print(student.items())

# Output: dict_items([('name', 'Not Assigned'), ('age', 'Not Assigned'), ('course', 'Not Assigned')])

# keys() returns all keys of the dictionary.
# Syntax: dictionary_name.keys()

print(student.keys())

# Output: dict_keys(['name', 'age', 'course'])

# values() returns all values of the dictionary.
# Syntax: dictionary_name.values()

print(student.values())

# Output: dict_values(['Not Assigned', 'Not Assigned', 'Not Assigned'])

# pop() removes the specified key.
# Syntax: dictionary_name.pop(key)

student.pop("course")

print(student)

# Output: {'name': 'Not Assigned', 'age': 'Not Assigned'}

# popitem() removes the last inserted item.
# Syntax: dictionary_name.popitem()

student.popitem()

print(student)

# Output: {'name': 'Not Assigned'}

# setdefault() returns the value of a key.
# If the key does not exist, it inserts the key with the specified value.
# Syntax: dictionary_name.setdefault(key, value)

student.setdefault("cgpa", 8.5)

print(student)

# Output: {'name': 'Not Assigned', 'cgpa': 8.5}

# update() inserts or updates key:value pairs.
# Syntax: dictionary_name.update({key:value})

student.update({"course": "Tech"})

print(student)

# Output: {'name': 'Not Assigned', 'cgpa': 8.5, 'course': 'Tech'}

# clear() removes all items from the dictionary.
# Syntax: dictionary_name.clear()

student.clear()

print(student)

# Output: {}

# copy() returns a shallow copy of the dictionary.
# Syntax: dictionary_name.copy()

student = {
    "name": "Perli",
    "age": 19
}

student2 = student.copy()

print(student2)

# Output: {'name': 'Perli', 'age': 19}