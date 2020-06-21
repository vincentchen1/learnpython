#the keyword def informs python that you're defining a function
#any indented lines that follow def greet_user(): makes up the BODY of this function
#a function call tells python to execute the code in the function
#to call a function, write the name of the function
#comments for functions are called docstrings

def greet_user():
    """Display a simple greeting"""
    print("Hello!")

greet_user()

#by adding username, you allow the function to accept any value of username you specify
#the function now expects you to provide a value for username each time you call it

#the variable username in the definition of greet_user() is an example of a parameter
#a paramter is a piece of information the function needs to do its job
#the value 'jesse' in greet_user('jesse') is an example of an argument
#an argument is a piece of information that's passed from a function call to a function

def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

