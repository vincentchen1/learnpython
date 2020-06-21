#positional arguments match each argument in the function call with a parameter in the function definition
#order matters in positional arguments

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('dog', 'luna')
describe_pet('chicken', 'max')

#a keyword argument is a name-value pair that you pass to a function
#they free you from having to worry about correctly ordering your arguments in the function call and they clarify the role of each value in the function call

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')

#you can also set a default value
#with no animal_type specified, python knows to use the value 'dog' for this parameter
def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
#you could also just put the name of the dog since it is the only argument and matches up to the first parameter in the definition pet_name
#because no argument is provided for animal_type, it uses the default value 'dog'
describe_pet('willie')

#recap: these are equivalent functions
#to avoid errors, make sure there are function arguments for the parameter
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')