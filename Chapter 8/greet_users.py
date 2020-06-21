#passing a list
#define greet_users() so it expects a list of names, which assigns to parameters "names", function loops through list and prints a greeting to each user

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)