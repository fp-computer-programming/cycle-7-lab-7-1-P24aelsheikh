"""
Create a Python file named lab_7-1.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a function called greeting()
Add a docstring to the function that explains how the function can only print "Hello World" on one line
Add a statement in the function to print "Hello World!"
Add a statement that returns the docstring for the greeting function
Add another statement to call the function
"""
def greeting():
    """
    This function prints 'Hello World' on one line and returns the docstring.
    """
    print("Hello World!")

# This is what the function is called
greeting()

# This will retrieve and print the docstring
print(greeting.__doc__)
