def create_pokemon():
    return {'Pokemon name': input("What is your Pokemon? ").title(),
            'Pokemon level': input("What level is your Pokemon? "),
            'Pokemon type': input("What is your Pokemon's type? ").title()}
