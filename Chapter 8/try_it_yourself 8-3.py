#8-3. T-Shirt
def make_shirt(shirt_size, shirt_message):
    print(f"\nThe size of the shirt is a {shirt_size}.")
    print(f"The message of the shirt says {shirt_message}.")

make_shirt('medium', '"This shirt is epic!"')
make_shirt(shirt_size='medium', shirt_message='"This shirt is epic"')

def make_shirt(shirt_size = 'large', shirt_message = '"I love Python."'):
    print(f"\nThe size of the shirt is a {shirt_size}.")
    print(f"The message of the shirt says {shirt_message}.")

#8-4. Large Shirts
make_shirt()
make_shirt(shirt_size='medium')
make_shirt(shirt_size='small', shirt_message='"Ninja coming through"')

#8-5. Cities
print()
def describe_city(city, country = 'taiwan'):
    print(f"{city.title()} is in {country.title()}")

describe_city('kaosiung')
describe_city('taipei')
describe_city('tainan')