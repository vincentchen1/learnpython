user_input = 'hello'
active = True
while active:
    response = input(user_input)

    if response == 'quit':
        active = False
    else:
        print(response)