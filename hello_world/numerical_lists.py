for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

odd_numbers = list(range(1, 11, 2))
print(odd_numbers)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# this is a comprehension list
sqaures = [value ** 2 for value in range(1, 11)]
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#Try it yourself - Numerical List practice
one_to_twenty = list(range(1, 21))
for value in one_to_twenty:
    print(value)

one_to_million = list(range(1, 1000001))
print(min(one_to_million))
print(max(one_to_million))
print(sum(one_to_million))

even_more_odd_numbers = list(range(1, 21, 2))
print(even_more_odd_numbers)

multiples_of_three = list(range(3, 31, 3))
print(multiples_of_three)

cubed_numbers = []
for value in range(1, 11):
    cubed = value ** 3
    cubed_numbers.append(cubed)
print(cubed_numbers)

apprehension_cubed_numbers = [value ** 3 for value in range(1, 11)]
print(apprehension_cubed_numbers)

# slicing a list [first number is where it starts, second number is where it ends (does not include that number)]
games = ['r6s', 'fortnite', 'minecraft', 'bo2', 'clash of clans']
print(games[0:2])
print(games[1:3])
print(games[:4])
print(games[2:])
print(games[-3:])
print(games[:-3])

# copying a list
print(f"\nThese are the two main games I played during middle school.")
for game in games[:2]:
    print(game.title())

my_foods = ['pizza', 'ramen', 'chicken']
friends_foods = my_foods[:]
my_foods.append('green tea')
friends_foods.append('calpico')

print(f"\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_foods)

#Try it yourself - Slices
my_drinks = ['unsweetened ice tea', 'iced green tea', 'oolong tea', 'milk tea', 'water']
print(my_drinks[0:3])
print(my_drinks[1:4])
print(my_drinks[2:5])

cereals = ['lucky charms', 'frosted flakes', 'cheerios', 'captain crunch', 'fruity pebbles']
for cereal in cereals:
    print(cereal)





