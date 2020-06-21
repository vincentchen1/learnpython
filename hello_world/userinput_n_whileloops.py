#important operators in this lesson are !=, +=
#the input function takes in information from the user and assigns it to a variable
#add a space at the end of your prompts to make it clear for the user's repsonse
message = input("Tell me something and I will repeat it back to you: ")
print(message)

name = input(f"\nPlease enter your name: ")
print(f"Hello, {name}!")

#the += operator takes the string that was assigned and adds the new string onto the end
prompt = f"\nIf you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nThat's a cool first name, {name}!")

#the int() function interprets the number as a string, but the value is then converted to a numerical representation
age = input("\nHow old are you? ")
age = int(age)
print(age >= 18)

#ROLLERCOASTER.PY
height = input("\nHow tall are you in inches? ")
height = int(height)

if height >= 48:
    print("You are able to ride the roller coaster!")
else:
    print("Sorry, you are not tall enough to ride this roller coaster.")

#the modulo operator(%) divides one number by the other and returns the remainder; a number divisible by itself will be 0
print()
print(5 % 3)
print(5 % 5)

#EVEN_OR_ODD.PY
number = input("\nEnter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

#the while loop allows runs as long as, or while, a certain condition is true

#COUNTING.PY
#in this case, += is shorthand for "current_number = current_number + 1
current_number = 1
while current_number <=  5:
    print(current_number)
    current_number += 1

#a variable called flag can be used that determines whether or not the entire program is active
#PARROT.PY
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
if message != 'quit':
    print(message)
elif message == 'quit':
    print("You have quit the program.")

#using a flag where "active" == the flag
user_input = "\nSay something and I will repeat it to you. "
user_input += "\nEnter 'quit' to end the program: "
active = True
while active == True:
    response = input(user_input)

    if response == 'quit':
        active = False
    else:
        print(response)
print("You have quit the program")

#the break statement exits any loop immediately without running any remaining code in the loop, regardless of the results of any conditional test
#a loop that starts with "while True" will run forever until it reaches a "break" statement
#CITIES.PY
prompt = "\nEnter a city you have been to: "
prompt += "\nEnter quit to end the program: "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

#you can use the continue statment to "continue" through a loop without executing the code
current_number = 0
while current_number < 10:
    current_number +=1
    if current_number % 2 == 0:
        continue

    print(current_number)

#every while loop needs a way to stop running so it won't continue to run forever
#if the line "x += 1" was omitted, the line would run forever
print()
x = 1
while x <= 5:
    print(x)
    x += 1

# Try it yourself - Pizza toppings
print()
pizza_toppings = ("Enter the pizza toppings you would like: ")
pizza_toppings += ("\nEnter 'quit' to stop your order: ")

while True:
    topping = input(pizza_toppings)

    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza...")

print()
ticket_price = "Enter your age to determine the price of your ticket: "
person_age = input(ticket_price)
person_age = int(person_age)
if person_age < 3:
    print("Your ticket is free")
elif person_age >= 3 and person_age <= 12:
    print("Your ticket price is $10")
else:
    print("Your ticket is $15")

print()
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#
# Start with the users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# removing all instances of a specific values from a list
print()
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# filling a dictionary with user input
responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone is going to take the poll
    repeat = input("Would you like to let another person respond? (yes / no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

# Try it yourself - Sandwich and vacation
print()
print("Sorry we are all out of pastrami.")
sandwich_orders = ['reuben', 'pastrami', 'club', 'pastrami', 'turkey', 'pastrami', 'blt']

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

finished_sandwiches = []

while sandwich_orders:
    made_sandwiches = sandwich_orders.pop()
    finished_sandwiches.append(made_sandwiches)

for sandwich in finished_sandwiches:
    print(f"I made your {sandwich} sandwich")

print()
answers = {}
poll_active = True
while poll_active:
    name = input("What is your name? ")
    poll_answer = input("If you could visit one place in the world, where would you go? ")
    answers[name] = poll_answer

    again = input("Would you like to poll again? (yes / no) ")
    if again == 'no':
        poll_active = False

print("\n Poll Results ")
for name, poll_answer in answers.items():
    print(f"{name.title()} would like to visit {poll_answer.title()}")