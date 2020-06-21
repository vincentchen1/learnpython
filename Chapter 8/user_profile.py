#using arbitrary keyword arguments

#the function build_profile() in the example always takes a first and last name, but it also accepts an arbitrary number of keyword arguments
#double asterisks (**) allow you to pack whatever name-value pairs it receives into the dictionary
#You'll often see the parameter name **kwargs used to collect non-specific keyword arguments.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                            field='physics')

print(user_profile)