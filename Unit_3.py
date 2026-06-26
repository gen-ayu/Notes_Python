# Let's start with the unit 3 of our python course. In this unit we will learn about functions, modules, packages, recursion.

# Functions are reusable blocks of code that perform a specific task. They let you break a program into smaller, easier-to-manage pieces. By calling a function whenever you need its behavior, you avoid repeating code and make your program easier to read and maintain. The syntax for defining a function in Python is:

''' def function_name(parameters):
        """Optional docstring describing what the function does."""
        # function body
        return value # optional return statement '''
# An example an function that takes two numbers as input and returns their sum is shown below:
'''
def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b
# now if we want to use this function we can call it like this:
result = add_numbers(3, 5)
print (result) # Output: 8
'''
# Now there are different types of functions in python. They are:
# 1. Built-in functions: These are functions that are already defined in Python and can be used directly without any need for definition. Examples include print(), len(), type(), etc.
# 2. User-defined functions: These are functions that you define yourself using the def keyword, as shown in the example above.
# 3. Anonymous functions (lambda functions): These are small, unnamed functions defined using the lambda keyword. They can take any number of arguments but can only have one expression. For example:
'''
result = (lambda x, y: x + y)(3, 5)
print(result) # Output: 8
'''

# Now how we pass the arguments to a funtion also matter as there are different ways to pass the arguments to a function. They are:
# 1. Positional arguments: These are the most common type of arguments. The values are passed to the function in the order in which they are defined.
# 2. Keyword arguments: These are arguments that are passed to the function by explicitly specifying the parameter name. This allows you to pass the arguments in any order.
# 3. Default arguments: These are arguments that have a default value specified in the function definition. If the caller does not provide a value for that argument, the default value is used.
# 4. Variable-length arguments: These are arguments that allow you to pass a variable number of values to a function. They are defined using the *args and **kwargs syntax. The *args syntax allows you to pass a variable number of positional arguments, while the **kwargs syntax allows you to pass a variable number of keyword arguments.

''' 
Now for the examples of the above types of aguments, we can use the following code snippets:
-------------------------------------
1. Positional Arguments
def add(a, b):
    print(a + b)

add(2, 3)
-------------------------------------
2. Keyword Arguments
def add(a, b):
    print(a + b)

add(b=3, a=2)
-------------------------------------
3. Default Arguments
def greet(name="Guest"):
    print(name)

greet()
greet("Ayush")
-------------------------------------
4. Variable-Length Positional Arguments (*args)
def show(*args):
    print(args)

show(1, 2, 3)

Output:

(1, 2, 3)
--------------------------------------
5. Variable-Length Keyword Arguments (**kwargs)
def show(**kwargs):
    print(kwargs)
    
show(name="Ayush", age=19)

Output:

{'name': 'Ayush', 'age': 19}
-------------------------------------'''

# Now that we have covered the different types of functions and arguments, let's move on to the next topic which is local and global variables.
# In Python, variables that are defined inside a function are called local variables. They can only be accessed within that function. On the other hand, variables that are defined outside of any function are called global variables. They can be accessed from anywhere in the program.
# For example, if we see a complete function as a box then an variable that is defined in that box is a local variable and an variable that is defined outside of the box is a global variable.
# Also if we define another box inside the first box then the variable defined in the second box is also a local variable and can only be accessed within that box. But if we want to access the variable defined in the first box then we can do that as well. But if we want to access the variable defined in the second box from outside of it then we cannot do that.

# That more or less covers the what local and global variables are, it is an important concept to understand as it will help you avoid variable name conflicts and make your code more organized.

# Now lets move on to the next topic which is recursion. Recursion is a programming technique where a function calls itself in order to solve a problem. It can be a powerful tool for solving problems that can be broken down into smaller subproblems. However, it can also lead to infinite loops if not implemented correctly.

''' 
A basic example of recursion is the calculation of the factorial of a number. The factorial of a number n is defined as the product of all positive integers less than or equal to n. It can be calculated using recursion as follows:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n = 5
result = factorial(n)'''

# Now if we we to look at how the stack works in recursion then we can see that when the function is called, it is added to the call stack. When the function returns, it is removed from the call stack. This process continues until the base case is reached and the function returns a value. The call stack is a data structure that keeps track of the function calls and their return values.
# Some also refer to this as the "last in, first out" (LIFO) principle, where the last function called is the first one to return. This is important to understand as it can help you avoid stack overflow errors and make your code more efficient. Or more casually called 'ladder'.

'''
How recursion works for factorial(5)
factorial(5)
= 5 × factorial(4)
= 5 × 4 × factorial(3)
= 5 × 4 × 3 × factorial(2)
= 5 × 4 × 3 × 2 × factorial(1)
= 5 × 4 × 3 × 2 × 1
= 120
'''
# Now with this we have covered the basics of functions, arguments, local and global variables, and recursion. In the next unit, we will learn about modules and packages in Python.