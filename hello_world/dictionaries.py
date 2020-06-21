#dictionaries allow you to store multiple values to multiple variable in a single line of code
zombie_0 = {'color': 'gray', 'strength': 'low'}
print(zombie_0['color'])
print(zombie_0['strength'])

zombie_color = zombie_0['color']
print(f"The zombie's color is {zombie_color}")

zombie_0['x_position'] = 0
zombie_0['y_position'] = 25
print(zombie_0)

#Alien speed project
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the aline to the right
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
#This alien is fast
else:
    x_increment = 3
# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

#You can use the del function to remove a piece of information stored in a dictionary
apple = {'texture': 'smooth', 'taste': 'sweet', 'color': 'red'}
print(f"\nWhat does an apple feel, taste, and look like?")
print(f"An apple is {apple['texture']}, {apple['taste']}, and {apple['color']}.")
del apple['color']
print(apple)
#Note: apple 'color' is deleted permanently
apple['color'] = 'red'
print(apple)

favorite_foods = {
    'john': 'chicken',
    'joe': 'pasta',
    'mark': 'pizza',
    'luke': 'steak'
    }

print(f"\nJoe's favorite food is {favorite_foods['joe']}")
joes_favorite = favorite_foods['joe']
print(f"Joe's favorite food is {joes_favorite}")

for name in favorite_foods.keys():
    print(name.title())
for name in favorite_foods:
    print(name.title())

print()
friends = ['john', 'mark']
for name in favorite_foods.keys():
    print(f"Hi {name.title()}!")

    if name in friends:
        food = favorite_foods[name]
        print(f"\t{name.title()}, I see you love {favorite_foods[name]} too!")

if 'peter' not in favorite_foods:
    print(f"What's your favorite food, Peter?")

#the sorted function can also be used in dictionaries
#keys funcion prings the keys
print()
favorite_pets = {
    'matthew': 'dog',
    'charles': 'cat',
    'bartholomew': 'salamander',
    'walter': 'chicken'
}
for name in sorted(favorite_pets.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

#set function removes duplicate items in a dictionary
#values function prints the values
print()
favorite_states = {
    'jim': 'colorado',
    'tom': 'california',
    'luke': 'new york',
    'dan': 'california'
}
print(f"The people who took the poll are:")
for name in (favorite_states.keys()):
    print(name.title())

print()
print(f"The mentioned states are:")
for state in set(favorite_states.values()):
    print(state.title())

# Try it yourself - Glossaries and polls
print()
information = {
    'first name': 'vincent',
    'last name': 'chen',
    'age': '15',
    'city': 'san diego'
}
for key in information.keys():
    print(key.title())
print()
for value in information.values():
    print(value.title())

print()
rivers = {
    'nile': 'egypt',
    'gagnes': 'india',
    'songhua': 'china'
}
# for river in ['nile', 'gagnes', 'songhua']:
for river in rivers.keys():
    print(f"The {river.title()} river is in {rivers[river].title()}")

#nesting allows you to store multiple dictionaries in a list, or a list of items as a value in a dictionary
print()
monster_0 = {'color': 'green', 'points': '5'}
monster_1 = {'color': 'yellow', 'points': '10'}
monster_2 = {'color': 'red', 'points': '15'}

monsters = [monster_0, monster_1, monster_2]
for monster in monsters:
    print(monster)

print()
chickens = []
for chicken_number in range(30):
    new_chicken = {'color': 'white', 'points': '5', 'speed': 'slow',}
    chickens.append(new_chicken)

for chicken in chickens[:3]:
    if chicken['color'] == 'white':
        chicken['color'] = 'yellow'
        chicken['speed'] = 'medium'
        chicken['points'] = '10'
    elif chicken['color'] == 'yellow':
        chicken['color'] = 'red'
        chicken['speed'] = 'fast'
        chicken['points'] = '15'

for chicken in chickens[:5]:
    print(chicken)
print("...")

print(f"Total number of chickens: {len(chickens)}")

#nesting a list of items as values in a dictionary
pizza = {
    'crust': 'thin',
    'toppings': ['cheese', 'pepperoni', 'mushrooms'],
}
print(f"You ordered a {pizza['crust']} crust "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"{topping}")

#nesting a dictionary within a dictionary
users = {
    'thepremiumf2p': {
        'first name': 'vincent',
        'last name': 'chen',
        'favorite game': 'R6S',
        },
    'yu.gen': {
    'first name': 'vincent',
    'last name': 'chen',
    'favorite game': 'pokemon',
    },
    'dr.vangogh': {
    'first name': 'vincent',
    'last name': ' chen',
    'favorite game': 'fortnite'
    },
    'casserole123123': {
    'first name': 'thomas',
    'last name': 'aristar',
    'favorite game': 'gta 5'
    },
}

#for k, v in variable.items, you can use any variables for k and v and they would replace the key and value 
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first name']} {user_info['last name']}"
    favorite_game = f"{user_info['favorite game']}"

    print(f"Full name: {full_name.title()}")
    print(f"Favorite game: {favorite_game.title()}")

#Try it yourself - Final task
print()
people = f"{users['thepremiumf2p']}, {users['yu.gen']}, {users['dr.vangogh']}, {users['casserole123123']}"
for user in users.values():
    print(user)

print()
dog = {'owner name': 'shelly', 'type': 'golden retriever'}
cat = {'owner name': 'casey', 'type': 'persian'}
chicken = {'owner name': 'benjamin', 'type': 'broiler'}

pets = [dog, cat, chicken]
for pet in pets:
    print(pet)

print()
favorite_places = {'frank': ['costco', 'dominos',], 'robin': ['trader joes', 'sprouts'], 'maple': ['the beach', 'the mall']}
for name in favorite_places.keys():
    print(name)

for places in favorite_places.values():
    print(places)

cities = {
    'san diego': {
    'country': 'United States',
    'approximate population': '1.5 million',
    'fact': 'The top employer in the city is the US Navy'
    },
    'kaosiung': {
    'country': 'taiwan',
    'approximate population': '2.7 million',
    'fact': 'It is where my grandparents live'
    },
    'new york city': {
    'country': 'United States',
    'approximate population': '8.4 million',
    'fact': 'I have been there twice'
    },
}

print()
for key, key_info in cities.items():
    print(f"\nCity: {key.title()}")
    country = f"{key_info['country'.title()]}"
    approximate_population = f"{key_info['approximate population']}"
    fact = f"{key_info['fact']}"
    print(country)
    print(approximate_population)
    print(fact)


