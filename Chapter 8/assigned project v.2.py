#.get calls the value of a value from a dictionary

names = {}

while True:
    first_name = input("What is your first name? ")
    while first_name == '':
        print("Please enter a first name.")
        first_name = input("What is your first name? ")
        continue

    middle_name = input("What is your middle name? ")

    last_name = input("What is your last name? ")
    while last_name == '':
        print("Please enter a last name.")
        last_name = input("What is your last name? ")
        continue

    if names.get(last_name) is not None:
        names[last_name].append(f"{first_name} {middle_name} {last_name}")
    else:
        names[last_name] = [f"{first_name} {middle_name} {last_name}"]

    response = input("Do you want to continue? (yes / no) ")
    if response == 'no':
        break

search = input("Enter the last name of the person you are looking for: ")
print(names.get(search))

