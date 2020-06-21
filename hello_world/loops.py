# common indenting errors include forgetting to indent, forgetting to indent additional lines, indenting unnecessarily, indenting unnecessarily after the loop, and forgetting the colon
sports = ['baseball', 'track', 'football', 'soccer', 'basketball']
for sport in sports:
    print(f"I love to play {sport}!")
    print(f"Yeah, {sport} is the best!\n")
print("I like them all equally!")

#Try it yourself - Pizza practice
favorite_pizza = ['buffalo', 'classic pepperoni', 'sausage and mushroom']
friends_pizza = favorite_pizza[:]
favorite_pizza.append('combo')
friends_pizza.append('hawaiian')
for pizza in favorite_pizza:
    print(f"\n{pizza}")
    print(f"I like {pizza} pizza")
print(f"\nI love pizza!")

for pizza in friends_pizza:
    print(f"\n{pizza}")
    print(f"My friend likes {pizza} pizza")

print(f"\n{favorite_pizza}")
print(friends_pizza)


#Try it yourself - Animal practice
