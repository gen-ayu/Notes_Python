# In this unit we will cover the following topics:
# Strings, Lists, Tuples, Sets, Dictionaries, and their methods.

#------------------------------------------------------------------------------

'''LISTS'''
"""
We will now be begining with lists.
List is a collection of items that are ordered and changedable which means that the items in a list can be modified after the list is created.
List is defiend by using square brackets [] and the items in a list are separated by commas.
For example, a list of numbers can be defined as follows:
a = [1, 2, 3, 4, 5]
We can also have a list of strings, for example:
str_list = ["apple", "banana", "cherry"]
""""   

# If you add new item to a list, it will be added to the end of the list.
# List allows duplicate items and these items present in the list are mutable (changeable) but the object of the  list may be immutable (unchangeable) depending on the type of the object. 
# For example, if the list contains only immutable objects like strings or numbers, then the list itself is mutable but the objects inside it are immutable. However, if the list contains mutable objects like other lists or dictionaries, then both the list and the objects inside it are mutable.

# List can be of any data type and can also contain different data types in a single list. For example:
mixed_list = [1, "apple", 3.14, True, [1, 2, 3], {"name": "Ayush", "age": 19}]
int_list = [1, 2, 3, 4, 5]

# We can use type() function to check the type of the list.
print(type(mixed_list)) # Output: <class 'list'>
# We can also define list with list constructor which is a built-in function in python list(). For example:
thislist = list(("apple", "banana", "cherry"))
print(thislist)

# Accessing the items of a list can be done by using the index of the item. The index of the first item in a list is 0, the index of the second item is 1, and so on. We can also use negative indexing to access the items from the end of the list. 
# The index of the last item in a list is -1, the index of the second last item is -2, and so on. For example:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #Output: cherry, Indexing done from the end of the list
print(thislist[2]) #Output: banana, Indexing done from the start of the list


# We can also use slicing to access a range of items in a list. Slicing is done by specifying the start and end index of the range. The start index is inclusive and the end index is exclusive. For example:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # Output: ['cherry', 'orange', 'kiwi']

# Now while we are using slicing but we dont mention either the start or the end index then it will take the default value of 0 for start index and the length of the list for end index. For example:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) # Output: ['apple', 'banana', 'cherry', 'orange']
print(thislist[2:]) # Output: ['cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[:]) # Output: ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango'], i.e. simply printing the whole list.
print(thislist[-4:-1]) # Output: ['orange', 'kiwi', 'melon']

# Changing item of a list can be done by using the index of the item and assigning a new value to it. For example:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) # Output: ['apple', 'blackcurrant', 'cherry']
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) # Output: ['apple', 'blackcurrant', 'watermelon'], i.e. replacing the items at index 1 and 2 with new items.
# Even if we dont give the same number of items in the new list then it will still work and the new items will be added to the list. For example:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[0:4] = ["blackcurrant"]
print(thislist)

# Inserting an item in a list can be done by using the insert() method. The insert() method takes two arguments, the index at which the item should be inserted and the item itself. For example:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) # Output: ['apple', 'orange', 'banana', 'cherry'], i.e. inserting the item at index 1 and shifting the other items to the right.

# we the index we provide for insert is greater or less than the length of the list then it will simply add the item to the end of the list. For example:
thislist = ["apple", "banana", "cherry"]
thislist.insert(10, "orange")
print(thislist) # Output: ['apple', 'banana', 'cherry', 'orange']

# Now moving on to append. We can use the append() method to add an item to the end of the list. The append() method takes one argument, the item to be added. For example:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # Output: ['apple', 'banana', 'cherry', 'orange'], i.e. adding the item to the end of the list.

# Extend() can be used to add multiple items to the end of the list. The extend() method takes an iterable (list, tuple, set, etc.) as an argument and adds each item of the iterable to the end of the list. For example:
thislist = ["apple", "banana", "cherry"]
thislist.extend(["orange", "kiwi"])
print(thislist) # Output: ['apple', 'banana', 'cherry', 'orange', 'kiwi'], i.e. adding the items to the end of the list.
# while using extend() we dont just have to use a list as an argument but we can also use other iterables like tuple, set, etc. For example:
thislist = ["apple", "banana", "cherry"]
thislist.extend(("orange", "kiwi")) # using a tuple as an argument
print(thislist) # Output: ['apple', 'banana', 'cherry', 'orange', 'kiwi'], i.e. adding the items to the end of the list.

# Removing an item from a list can be done by using the remove() method. The remove() method takes one argument, the item to be removed. For example:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # Output: ['apple', 'cherry'], i.e. removing the item from the list.

# The pop() method can also be used to remove an item from a list. The pop() method takes one argument, the index of the item to be removed. If no index is specified, the last item in the list is removed. For example:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # Output: ['apple', 'cherry'], i.e. removing the item at index 1 from the list.

# The del keyword can also be used to remove an item from a list. The del keyword takes one argument, the index of the item to be removed. If no index is specified, the entire list is deleted. For example:
thislist = ["apple", "banana", "cherry"]
del thislist[1]
print(thislist) # Output: ['apple', 'cherry'], i.e. removing the item at index 1 from the list.

# The clear() method can be used to remove all items from a list. The clear() method takes no arguments and removes all items from the list. For example:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # Output: [], i.e. removing all items from the list.
'
# Looping through a list can be done by using a for loop. The for loop iterates over each item in the list and executes a block of code for each item. For example:
thislist = ["apple", "banana", "cherry"]
for item in thislist:
    print(item) # Output: apple, banana, cherry, i.e. printing each item in the list.
# Looping throug the idexes of a list can be done by using the range() function and the len() function. The range() function generates a sequence of numbers and the len() function returns the length of the list. For example:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i]) # Output: apple, banana, cherry, i.e. printing each item in the list by using its index.
# using while loop to loop through a list can be done by using a while loop and the len() function. The while loop executes a block of code as long as a condition is true. For example:
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i]) # Output: apple, banana, cherry, i.e. printing each item in the list by using its index.
    i += 1
# Looping through list comprehension can be done by using a list comprehension. A list comprehension is a concise way to create a list by iterating over an iterable and applying a condition or an expression to each item. For example:
thislist = ["apple", "banana", "cherry"]
print([item for item in thislist]) # Output: ['apple', 'banana', 'cherry'], i.e. creating a new list by iterating over each item in the list.
[print(item) for item in thislist] # Output: apple, banana, cherry, i.e. printing each item in the list by using a list comprehension.

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list. One of its example is given above, below will be few more :
'''fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)''' 
# this same code can also be written as follows using list comprehension:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)

# The Syntax
# newlist = [expression for item in iterable if condition == True]
# Condition is like a filter that only accepts the items that valuate to True. For example:
newlist = [x for x in fruits if x != "apple"]
# if The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".
# The condition can also be omitted, in that case the new list will contain all the items from the original list. For example:
newlist = [x for x in fruits]