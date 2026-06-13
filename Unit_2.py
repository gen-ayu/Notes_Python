# We will we to some important concepts that may appear as confusing at first but trust its really easy when you get the hang of. Remember synatx in  python is almost normal english like so things will be really easy moving forward :)
# We will be learning about basic control fllow statements in python. These are the building blocks of any programming language and will allow us to create more complex programs in the future.

# The first control flow statement we will learn about is the "if statement". The if statement allows us to execute a block of code only if a certain condition is true. The syntax for an if statement is as follows:
# if else condition:

'''the syntax for an if statement is as follows:
if(condition):
    # code to execute if condition is true  
    # this code will only execute if the condition is true
else:
    # code to execute if condition is false'''

# elif statement is used to check multiple conditions. It stands for "else if" and allows us to check for additional conditions if the previous condition was false. The syntax for an elif statement is as follows:
'''if(condition1):
    # code to execute if condition1 is true
elif(condition2):
    # code to execute if condition2 is true
else:
    # code to execute if both condition1 and condition2 are false'''
    
# Next we will learn about loops. Loops allow us to execute a block of code multiple times. The two main types of loops in python are the "for loop" and the "while loop".

# For loop is used to iterate over a sequence (such as a list, tuple, or string) and execute a block of code for each item in the sequence. The syntax for a for loop is as follows:
'''for item in sequence:
    # code to execute for each item in the sequence'''
''' Syntax for for loop is as follows:
for item in sequence:
i.e. for item in [1, 2, 3, 4, 5]:
    print(item)'''
    
# While loop is used to execute a block of code as long as a certain condition is true. The syntax for a while loop is as follows:
# There are two types of while loops, the first one is the "while loop" and the second one is the "do while loop". The syntax for a while loop is as follows:
'''while(condition):
    # code to execute as long as condition is true'''
'''Do while loop is used to execute a block of code at least once and then continue executing the block of code as long as a certain condition is true. The syntax for a do while loop is as follows:
do:
    # code to execute at least once
while(condition)'''

# We can now move on to the match case statement. The match case statement is used to execute a block of code based on the value of a variable. The syntax for a match case statement is as follows:
'''match variable:
    case value1:
        # code to execute if variable is equal to value1
    case value2:
        # code to execute if variable is equal to value2
    case _:
        # code to execute if variable does not match any of the above cases'''
# Note we usually use default case as a catch all for any value that does not match the previous cases. This is done using the underscore (_) character.
# We also use break statement to exit a loop or a match case statement. The break statement is used to exit a loop or a match case statement when a certain condition is met. The syntax for a break statement is as follows:
'''while(condition):
    # code to execute as long as condition is true
    if(some_condition):
        break # this will exit the loop when some_condition is true
        match variable:
        case value1:
        print("Value is 1")
        break # this will exit the match case statement when variable is equal to value1'''

# Now that we have talked about break lets learn it along with other statements like continue and pass. The continue statement is used to skip the current iteration of a loop and move on to the next iteration. The syntax for a continue statement is as follows:
'''while(condition):
    # code to execute as long as condition is true
    if(some_condition):
        continue # this will skip the current iteration of the loop when some_condition is true'''
# The pass statement is used as a placeholder for code that is not yet implemented. The syntax for a pass statement is as follows:
'''while(condition):
    # code to execute as long as condition is true
    if(some_condition):
        pass # this will do nothing when some_condition is true'''
        
        
# With this we have covered the basic control flow statements in python. These statements will allow us to create more complex programs in the future.
# We have completed the Unit 2 of Our Python Journy and will look into funtions, variables (global and local), and learn about recursion.