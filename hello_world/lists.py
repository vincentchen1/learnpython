# index positions start at 0, not 1
# negative numbers represent their position relative to the last number (-1 = last number, -2 = second to last, etc)

baseball = ['fun', 'action-filled', 'intense', 'casual and competitive']
print (baseball)

print (baseball[0])
print(baseball[0].title())

print(f"\n{baseball[1].title()}")
print(baseball[3].title())

print(f"\n{baseball[-1].title()}")

message = f"\nI like baseball because it is {baseball[0]}, {baseball[1]}, {baseball[2]} and {baseball[3]}."
print(message)

names = ['james', 'sunny', 'tim', 'jacob', 'thomas']
print(f"\n{names[0]}")
print(names[1])
print(names[2])
print(names[3])
print(names[4])

print(f"\nGet on Siege, {names[0].title()}")
print(f"Get on CS, {names[1].title()}")
print(f"Get on Fortnite, {names[2].title()}")
print(f"Get on Clash Royale, {names[3].title()}")
print(f"Get on Clash of Clans, {names[4].title()}")

nature = ['amazing', 'scenic', 'beautiful']
print (f"\nI like nature because it is {nature[0]}, {nature[1]} and {nature[2]}")

nature[0] = 'cool'
print (nature[0])
print(nature)

# the append() function adds an element to the end of the list
nature.append('calming')
print(f"\nnature")
print(f"I like nature because it is {nature[3]}.")

# insert moves the newly added element to that position
# ex: if that were 0, all elements in the list would move to the right by one, with the newly added element taking the place of the 0th position
nature.insert(3, 'bruh')
print(nature)
nature.insert(5, 'bruh')
print(nature)

# del() removes the assigned element from the list
del nature[5]
print(nature)
del nature[3]
print(nature)

# the pop() function removes the last item in a list, but it lets you work with that item after removing it
chicken = ['fried', 'grilled', 'baked', 'broiled']
print(f"\n{chicken}")
popped_chicken = chicken.pop()
print(f"{chicken[0]}, {chicken[1]}, {chicken[2]}")
print(popped_chicken)
favorite_type = chicken.pop(0)
print(f"My favorite kind of chicken is {favorite_type} chicken.")

# remove() allows you to remove an element that you don't know the position of, number-wise
video_games = ['Pokemon', 'PVZ: Garden Warfare', 'BO2', 'R6S']
print(f"\n{video_games}")
not_a_childhood_game = 'R6S'
video_games.remove(not_a_childhood_game)
print(video_games)
print(f"{not_a_childhood_game} is not a game I played when I was young.")

#Try it yourself - Guest List practice
guest_list = ['Jesus', 'Abraham Lincoln', 'Alexander the Great']
print(f"\n{guest_list[2]}")
guest_list.append('Martin Luther King Jr.')
lost_guest = guest_list.pop(2)
print(guest_list)
print(f"Hey {guest_list[0]}, I am having dinner at my house. Would you like to come?")
print(f"Hey {guest_list[1]}, I am having dinner at my house. Would you like to come?")
print(f"Hey {guest_list[2]}, I am having dinner at my house. Would you like to come?")

print(f"\nHey {guest_list[0]}, {guest_list[1]}, and {guest_list[2]}, I have found a bigger table.")
guest_list.insert(0, 'Mama')
guest_list.insert(2, 'Baba')
guest_list.append('Gaga')
print(f"Hey {guest_list[0]}, turns out there will be more people coming. Would you still like to have dinner?")
print(f"Hey {guest_list[1]}, turns out there will be more people coming. Would you still like to have dinner?")
print(f"Hey {guest_list[2]}, turns out there will be more people coming. Would you still like to have dinner?")
print(f"Hey {guest_list[3]}, turns out there will be more people coming. Would you still like to have dinner?")
print(f"Hey {guest_list[4]}, turns out there will be more people coming. Would you still like to have dinner?")
print(f"Hey {guest_list[5]}, turns out there will be more people coming. Would you still like to have dinner?")

print ("\nOh shoot, turns out I can only invite two people. Sorry!")
uninvited_guest = guest_list.pop()
print(f"Sorry, {uninvited_guest}!")
uninvited_guest = guest_list.pop()
print(f"Sorry, {uninvited_guest}!")
uninvited_guest = guest_list.pop()
print(f"Sorry, {uninvited_guest}!")
uninvited_guest = guest_list.pop()
print(f"Sorry, {uninvited_guest}!")

print(f"\nHey {guest_list[0]}, you are still invited!")
print(f"Hey {guest_list[1]}, you are still invited!")
print(len(guest_list))
del guest_list[1]
del guest_list[0]
print(guest_list)
print(len(guest_list))

# the sort() function sorts your function into alphabetical order
dogs = ['fluffy', 'cute', 'chunky', 'nice']
dogs.sort()
print(f"\ndogs")
dogs.sort(reverse=True)
print(dogs)

# the sorted() function allows you to sort a list but keep the original order of the list
lofi = ['chill', 'ambient', 'peaceful']
print(f"\nHere's the original list:")
print(lofi)
print("Here's the sorted list:")
print(sorted(lofi))
print("Here's the orignal list again:")
print(lofi)

# the reverse() function simply flips the order of the list
fruits = ['apples', 'oranges', 'banana', 'cherries', 'plums']
print(f"\n{fruits}")
fruits.reverse()
print(fruits)

#the len() function finds the length of the list
print(len(fruits))

#Try it yourself - Seeing the World practice
locations = ['Switzerland', 'Canada', 'Australia', 'Hawaii', 'Singapore']
print(f"\n{locations}")
print(sorted(locations))
print(locations)
alphabetical_locations = sorted(locations)
alphabetical_locations.reverse()
print(alphabetical_locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)
print(len(locations))

languages = ['English', 'Mandarin', 'Spanish', 'Irish', 'Russian', 'Cantonese', 'Turkish', 'Tagalog', 'Korean', 'Japanese']
print(f"\n{languages}")
languages.reverse()
print(languages)
print(sorted(languages))
alphabetical_languages = sorted(languages)
alphabetical_languages.reverse()
print(alphabetical_languages)













