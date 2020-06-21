# testing for equality is case sensitive in python
chicken = "fried"
print(chicken == "grilled")

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car)

    if car == 'bmw':
        print(car == 'bmw')

dogs = ['shibu', 'terrier', 'bulldog', 'pitbull']
for dog in dogs:
        if dog == 'shibu':
            print(f"\n{dog == 'terrier'}")

dogs = ['shibu', 'terrier', 'bulldog', 'pitbull']
dog = 'shibu'
if dog == 'shibu':
        print(dog == 'shibu')

requested_order = 'pizza'
if requested_order != 'pasta':
    print(f"\nSorry, this is the wrong order")

age = 15
print(f"\n{age == 20}")
print(age > 20)
print(age < 20)
print(age >= 20)
print(age <= 20)

answer = 10
if answer != 10:
    print(f"\nThat is not the right answer. Please try again!")
else:
    print("\nCorrect answer!")

# use the and/or function to check multiple conditions
age_0 = 18
age_1 = 22
print(f"\n{age_0 > 19 and age_1 > 21}")
print(age_0 > 17 or age_1 <19)

requested_toppings = ['honey turkey breast', 'lettuce', 'tomatoes', 'cucumbers']
print(f"\n{'cucumbers' in requested_toppings}")
print('chicken' in requested_toppings)

# use the if/not/in function to check whether a value is not in a list
banned_operators = ['jackal', 'montagne', 'echo', 'clash']
operator = 'zofia'
if operator not in banned_operators:
    print(f"{operator.title()} is avaiable")

else:
    print("BANNED OPERATOR")

#Try it yourself - Conditional Tests
cheap_cars = ['subaru', 'ford', 'toyota', 'honda', 'audi']
luxury_cars = ['ferrari', 'lamborghini', 'mercedez-benz', 'lexus', 'bmw']
print(f"\n{cheap_cars[0].title()} is a cheap car. I predict True.")
print(cheap_cars[0] == 'subaru')
print(f"{cheap_cars[1].title()} is a cheap car. I predict True.")
print(cheap_cars[1] == 'ford')
print(f"{cheap_cars[2].title()} is a cheap car. I predict True.")
print(cheap_cars[2] == 'toyota')
print(f"{cheap_cars[3].title()} is a cheap car. I predict True.")
print(cheap_cars[3] == 'honda')
print(f"{cheap_cars[4].title()} is a cheap car. I predict True.")
print(cheap_cars[4] == 'audi')

print(f"\n{luxury_cars[0].title()} is a cheap car. I predict False.")
print(cheap_cars[0] == 'ferrari')
print(f"{luxury_cars[1].title()} is a cheap car. I predict False.")
print(cheap_cars[1] == 'lamborghini')
print(f"{luxury_cars[2].title()} is a cheap car. I predict False.")
print(cheap_cars[2] == 'mercedez-benz')
print(f"{luxury_cars[3].title()} is a cheap car. I predict False.")
print(cheap_cars[3] == 'lexus')
print(f"{luxury_cars[4].title()} is a cheap car. I predict False.")
print(cheap_cars[4] == 'bmw')

# using the elif command is basically adding another "if" statement
# you can use as many elif commands as you would like

age = 4
if age <= 5:
    price = 0
elif age <= 12:
    price = 10
elif age <= 65:
    price = 15
else:
    price = 20
print(f"\nYour cost is ${price}")

pizza_toppings = ['cheese', 'pepperoni', 'mushrooms', 'sausage']
if 'cheese' in pizza_toppings:
    print("Adding cheese...")
if 'pepperoni' in pizza_toppings:
    print("Adding pepperoni...")
if 'mushrooms' in pizza_toppings:
    print("Adding mushrooms...")
if 'sausage' in pizza_toppings:
    print("Adding sausage...")
print("Your pizza is done!")

#Try it yourself - Alien Colors/Stages of Life/Favorite Fruit
alien_color = 'red'
if alien_color == 'green':
    print(f"\nYou just earned 5 points!")
elif alien_color == 'yellow':
    print(f"\nYou just earned 10 points!")
elif alien_color == 'red':
    print(f"\nYou just earned 15 points!")

# code can be simplified in a inequality format, ex. if 2 <= person_age < 4:
person_age = 121
if person_age < 2:
    print(f"\nYou are baby.")
if person_age >= 2 and person_age < 4:
    print(f"\nYou are a toddler.")
if person_age >= 4 and person_age < 13:
    print(f"\nYou are a kid.")
if person_age >= 13 and person_age < 20:
    print(f"\nYou are a teenager.")
if person_age >= 20 and person_age < 65:
    print(f"\nYou are an adult.")
if person_age > 65 and person_age < 120:
    print(f"\nYou are an elder.")
if person_age > 120:
    print(f"\nYou are probably dead.")

favorite_fruits = ['papaya', 'mango', 'passion fruit',]
if 'papaya' in favorite_fruits:
    print(f"\nYou must love papayas!")
if 'mango' in favorite_fruits:
    print("You must love mangoes!")
if 'passion fruit' in favorite_fruits:
    print("You must love passion fruits!")

print()
sandwich_toppings = ['turkey', 'lettuce', 'tomato', 'mayo', 'bacon']
for sandwich_topping in sandwich_toppings:
    if sandwich_topping == 'mayo':
        print("Sorry, we are out of mayo.")
    else:
        print(f"Adding {sandwich_topping}...")

print()
requested_noodle_toppings = []
if requested_noodle_toppings:
    for requested_noodle_topping in requested_noodle_toppings:
        print(f"Adding{requested_noodle_topping}.")
    print(f"\nYour noodles are ready.")
else:
    print(f"\nYou ordered plain noodles?")

print()
available_pizza_toppings = ['chicken', 'pepperoni', 'tomatoes', 'eggplants', 'bell peppers', 'anchovies']
requested_pizza_toppings = ['peanut butter', 'banana', 'lobster meat']
for requested_pizza_topping in requested_pizza_toppings:
    if requested_pizza_topping in available_pizza_toppings:
         print(f"Adding{requested_pizza_topping}")
    else:
         print(f"Sorry, we don't have {requested_pizza_topping}")

#Try it yourself - Usernames
usernames = ['admin', 'percyjackson576', 'thepremiumf2p', 'yu.gen', 'dr.vangogh']
username = 'admin'
if username == 'admin':
    print("Hello admin, would you like to see a status report?")
elif username == 'percyjackson576':
    print("Hello percyjackson576, thank you for logging in again.")
elif username == 'thepremiumf2p':
    print("Hello thepremiumf2p, thank you for logging in again.")
elif username == 'yu.gen':
    print("Hello yu.gen, thank you for logging in again.")
elif username == 'dr.vangogh':
    print("Hello dr.vangogh, thank you for logging in again.")
else:
    print("We need to find some users!")

current_users = ['joe', 'sal', 'q', 'murr', 'john']
new_users = ['sal', 'tokyo', 'denver', 'moscow', 'berlin']
print()
for new_user in new_users:
    new_user = 'sal'
if new_user == 'sal':
    print("This username is not available. Please choose another one.")
else:
    print("This username is available.")

numbers = ['1     ', '2', '3', '4', '5', '6', '7', '8', '9']
for number in numbers:
    if number == '1':
        print(f"{number}st")
    elif number == '2':
        print(f"{number}nd")
    elif number == '3':
        print(f"{number}rd")
    else:
        print(f"{number}th")











