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
# The condition can also be
# omitted, in that case the new list will contain all the items from the original list. For example:
newlist = [x for x in fruits]

# Sorting of a list can be done by using the sort() method. The sort() method takes no arguments and sorts the items in the list in ascending order by default. For example:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) # Output: ['banana', 'kiwi', 'mango', 'orange', 'pineapple'], i.e. sorting the items in the list in ascending order.
# The sort() method can also take a reverse argument which is a boolean value. If the reverse argument is set to True, the items in the list will be sorted in descending order. For example:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) # Output: ['pineapple', 'orange', 'mango', 'kiwi', 'banana'], i.e. sorting the items in the list in descending order.
#Custom sorting can be done by using the key argument of the sort() method. The key argument takes a function as an argument and sorts the items in the list based on the return value of the function. For example:
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) # Output: [50, 65, 82, 23, 100], i.e. sorting the items in the list based on their distance from 50.
# The sort() method is case sensitive, which means that it will sort the items in the list based on their ASCII values. For example:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) # Output: ['Kiwi', 'Orange', 'banana', 'cherry'], i.e. sorting the items in the list based on their ASCII values.
# Producing reverse of a list can be done by using the reverse() method. The reverse() method takes no arguments and reverses the order of the items in the list. For example:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) # Output: ['cherry', 'Kiwi', 'Orange', 'banana'], i.e. reversing the order of the items in the list.


# Coping of a list can be done by using the copy() method. The copy() method takes no arguments and returns a shallow copy of the list. For example:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) # Output: ['apple', 'banana', 'cherry'], i.e. creating a shallow copy of the list.
# A shallow copy means that the new list is a new object but the items in the new list are references to the same objects as the items in the original list. This means that if we modify an item in the new list, it will also modify the item in the original list.
# Creating a copy using list method can also be done by using the list() method.
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist) # Output: ['apple', 'banana', 'cherry'], i.e. creating a shallow copy of the list using the list() method.
# Using the slice Operator to create a copy of a list can also be done by using the slice operator. The slice operator takes two arguments, the start index and the end index, and returns a new list containing the items from the start index to the end index. For example:
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist) # Output: ['apple', 'banana', 'cherry'], i.e. creating a shallow copy of the list using the slice operator.

# Joining two lists can be done by using the + operator. The + operator takes two lists as arguments and returns a new list containing the items from both lists. For example:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) # Output: ['a', 'b', 'c', 1, 2, 3], i.e. joining the two lists into a new list.
# We can also use the extend() method to join two lists. The extend() methods takes one list as an arguments and adds the items from that list to the end of the original list. For example:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1) # Output: ['a', 'b', 'c', 1, 2, 3], i.e. adding the items from list2 to the end of list1.
# One more way to join two lists is by using the append() method in a loop. The append() method takes one item as an argument and adds that item to the end of the list. For example:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for item in list2:
    list1.append(item)
print(list1) # Output: ['a', 'b', 'c', 1, 2, 3], i.e. adding the items from list2 to the end of list1 using a loop and the append() method.

# To end all the list methods we discussed are as follows:
'''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list'''

#----------------------------------------------TUPLES---------------------------------------------

# Tuple is one of the four built-in data types in Python used to store collections of data, the other three are List, Set, and Dictionary, all with different qualities and usage. A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets.
# A tuple is a collection which is ordered and unchangeable. Example of a tuple is given below:
this_tuple = ("apple", "banana", "cherry")
print(this_tuple) # Output: ('apple', 'banana', 'cherry'), i.e. creating a tuple with three items.
# Tuples are ordered, which means that the items have a defined order, and that order will not change. Unchangeable/immutable means that we cannot change, add or remove items after the tuple has been created. Tuples are written with round brackets, and the items are separated by commas.
# Indexong in tuple starts from 0. When we say that tuple are ordered, it means that the items have a defined order, and that order will not change. Though it allows duplicate values, it is not possible to change the value of a tuple item, but we can create a new tuple with the desired values. For examples:
this_tuple = ("apple", "banana", "cherry", "apple", "cherry")
print(this_tuple)
# Tuple lenght can be found by using the len() function. For example:
this_tuple = ("apple", "banana", "cherry")
print(len(this_tuple)) # Output: 3, i.e. finding the length of the tuple.
# Tuple can also be of any data type and can also contain different data types in a single tuple. For example:
mixed_tuple = (1, "apple", 3.14, True, [1, 2, 3], {"name": "Ayush", "age": 19})
# Type of tuple can be found by using the type() function. For example:
print(type(mixed_tuple)) # Output: <class 'tuple'>, i.e. finding the type of the tuple.
# Tuple can also be created without using parentheses, but it is not recommended. For example:
t = 1, 2, 3
print(t) # Output: (1, 2, 3), i.e. creating a tuple without using parentheses. The Comma is the key to defining a tuple, not the parentheses.
# Tuple constructor can also be used to create a tuple. The tuple() constructor takes an iterable as an argument and returns a tuple containing the items from that iterable. For example:
this_tuple = tuple(("apple", "banana", "cherry")) # note the double round brackets, the outer brackets are for the tuple() constructor, and the inner brackets are for the iterable (in this case a list).
print(this_tuple) # Output: ('apple', 'banana', 'cherry'), i.e. creating a tuple using the tuple() constructor.

# Accessing the items of a tuple can be done by using the index of the item. The index of the first item in a tuple is 0, the index of the second item is 1, and so on. We can also use negative indexing to access the items from the end of the tuple. The index of the last item in a tuple is -1, the index of the second last item is -2, and so on. For example:
this_tuple = ("apple", "banana", "cherry")
print(this_tuple[1]) # Output: banana, i.e. accessing the item at index 1 of the tuple.
print(this_tuple[-1]) # Output: cherry, i.e. accessing the item at index -1 of the tuple.
print(this_tuple[2:3]) # Output: ('cherry',), i.e. accessing the items from index 2 to 3 of the tuple. Note that the end index is exclusive, so it will not include the item at index 3.

# Checking if the item exists in a tuple can be done by using the in keyword. The in keyword returns True if the item exists in the tuple, and False if it does not. For example:
this_tuple = ("apple", "banana", "cherry")
if "apple" in this_tuple:
    print("Yes, 'apple' is in the tuple") # Output: Yes, 'apple' is in the tuple, i.e. checking if the item exists in the tuple.
# I said earlier that tuples are unchangeable, which means that we cannot change, add or remove items after the tuple has been created. But we can convert the tuple into a list, change the list, and convert the list back into a tuple. For example:
this_tuple = ("apple", "banana", "cherry")
that_tuple = list(this_tuple)
that_tuple[1] = "kiwi"
this_tuple = tuple(that_tuple)
print(this_tuple) # Output: ('apple', 'kiwi', 'cherry'), i.e. changing the item at index 1 of the tuple by converting it into a list, changing the list, and converting it back into a tuple.

# Adding items to a tuple can be done by converting the tuple into a list, adding the item to the list, and converting the list back into a tuple. For example:
this_tuple = ("apple", "banana", "cherry")
that_tuple = list(this_tuple)
that_tuple.append("kiwi")
this_tuple = tuple(that_tuple)
print(this_tuple) # Output: ('apple', 'banana', 'cherry', 'kiwi'), i.e. adding an item to the tuple by converting it into a list, adding the item to the list, and converting it back into a tuple.
# You can add tuple to a tuple by using the + operator. The + operator takes two tuples as arguments and returns a new tuple containing the items from both tuples. For example:
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3) # Output: ('a', 'b', 'c', 1, 2, 3), i.e. adding two tuples together to create a new tuple.

# Removing items from a tuple can be done by converting the tuple into a list, removing the item from the list, and converting the list back into a tuple. For example:
this_tuple = ("apple", "banana", "cherry")
that_tuple = list(this_tuple)
that_tuple.remove("banana")
this_tuple = tuple(that_tuple)
# or delete the entire tuple by using the del keyword. For example:
this_tuple = ("apple", "banana", "cherry")
del this_tuple
print(this_tuple) # Output: NameError: name 'this_tuple' is not defined, i.e. deleting the entire tuple by using the del keyword.

# Unpacking a tuple can be done by using the unpacking operator *. The unpacking operator * takes a tuple as an argument and returns the items in the tuple as separate values. For example:
this_tuple = ("apple", "banana", "cherry") # This is packing
(a, b, c) = this_tuple # This is unpacking
print(a) # Output: apple, i.e. unpacking the tuple into separate values.
# Using * asterik
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green) # Output will be apple
print(yellow) # Output will be banana
print(red) # Output will be ['cherry', 'straberry', 'raspberry']

# Looping in a tuple : 3 ways
# Looping through a tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  
# looping through the index numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
# Using while loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
  
# Joining tuples using + Operator
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) # Output: ('a', 'b', 'c', 1, 2, 3)

# Multiplying tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) # Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# Methods of a tuple that can be used on tuple 
# count() - Returns the number of times a specific values has occured in a tuple. 
tuple_name.count(value) # Syntax
fruits = ("apple", "banana", "apple", "cherry", "apple")

print(fruits.count("apple")) # Output: 3
print(fruits.count("banana")) # Output: 1
print(fruits.count("mango")) # Output: 0
# index() - Searches the tuple for a specified value and returns the position of where it was found
tuple_name.index(value) # Syntax
fruits = ("apple", "banana", "apple", "cherry", "apple")

print(fruits.index("banana")) # Output: 1
print(fruits.index("apple")) # Output: 0
print(fruits.index("cherry")) # Output: 2
