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

# Since we know what a function is, we can also move on to modules and packages in Python. A module is a file containing Python code that can define functions, classes, and variables. A package is a collection of modules that are organized in a directory hierarchy. Modules and packages allow you to organize your code into reusable components, making it easier to manage and maintain.
# Example of such functions are math, pytorch, numpy, pandas, etc. These are called modules and packages in python. We will cover them in the next unit.

# We will discuss one such modules here that is the math module. The math module provides a wide range of mathematical functions and constants. Some of the commonly used functions in the math module include:
# 1. math.sqrt(x): Returns the square root of x.
# 2. math.pow(x, y): Returns x raised to the power of y.
# 3. math.sin(x): Returns the sine of x (x is in radians).
# 4. math.cos(x): Returns the cosine of x (x is in radians).
# 5. math.tan(x): Returns the tangent of x (x is in radians
# 6. math.log(x, base): Returns the logarithm of x to the specified base.
# 7. math.exp(x): Returns e raised to the power of x.
# 8. math.pi: Returns the value of pi (3.14159...).
# 9. math.e: Returns the value of e (2.71828...).
# 10. math.factorial(x): Returns the factorial of x (x must be a non-negative integer).
# 11. math.ceil(x): Returns the smallest integer greater than or equal to x.
# 12. math.floor(x): Returns the largest integer less than or equal to x.
# 13. math.fabs(x): Returns the absolute value of x.
# 14. math.gcd(x, y): Returns the greatest common divisor of x and y.
# 15. math.random(): Returns a random float number between 0.0 and 1.0.
# https://docs.python.org/3/library/math.html this is the link to the official documentation of the math module in python. You can refer to this for more information on the math module and its functions.
# Now I will show you an example of how to use the math module in Python. Let's say we want to calculate the square root of a number. We can do this using the math.sqrt() function as follows:
'''
import math 
x = 16
result = math.sqrt(x)
print(result) # Output: 4.0
'''
# Like the above example, we can import the math library and use its functions to perform various mathematical oprations. This is just a samll part of what a math module can do feel free to explore the documentation.

# Now with this we have covered the basics of functions, arguments, local and global variables, and recursion. In the next unit, we will learn about modules and packages in Python.