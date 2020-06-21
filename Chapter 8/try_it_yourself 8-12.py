#8-12. Sandwiches
def sandwich(*toppings):
    print(f"These are the toppings on your sandwich:")
    for topping in toppings:
        print(f"- {topping}")

sandwich('chicken')
sandwich('beef', 'cheese')
sandwich('bacon', 'lettuce', 'tomato')

#8-13. User Profile
print()
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('vincent', 'chen',
                             location='westview',
                            hair_color='dark brown',
                             ethnicity='taiwanese')

print(user_profile)

#8-14. Cars
print()
def car(manufacturer_name, model_name, **extra_info):
    extra_info['manufacturer name'] = manufacturer_name
    extra_info['model name'] = model_name
    return extra_info

car_info = car('lexus', 'ES',
               color='black',
               year_release='2008')

print(car_info)