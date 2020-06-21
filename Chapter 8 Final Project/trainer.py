from pokemon import create_pokemon
from user_info import user_name


def create_trainer():
    user_info = {
        'User': [
        ],
        'Pokemon': [
        ],
    }

    add_trainer = input("Do you want to add a trainer? (yes/no) ")
    if add_trainer == 'no':
        quit()
    else:
        user_info['User'].append(user_name())

    while True:
        add_pokemon = input("Do you want to add a Pokemon? (yes/no) ")
        if add_pokemon == 'no':
            add_trainer = input("Do you want to add a trainer? (yes/no) ")
            if add_trainer == 'no':
                break
            else:
                user_info['User'].append(user_name())
        else:
            user_info['Pokemon'].append(create_pokemon())

    print(user_info)


create_trainer()
