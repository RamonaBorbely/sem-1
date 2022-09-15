import csv

def pokes():
    print("Here are the Pokemon!")
    me_poke = ["Pikachu", "Muk", "Arbok", "Charmander","Mewtoo","Ratatata", "Muk"]
    for pok in me_poke:
        print(pok, '*** ', end="")
    return me_poke


def sounds(p):
    noises = {}
    for pokemon in p:
        sound = input(f"What sounds {pokemon} makes: ")
        noises[pokemon] = sound
    return noises


def store(sounds):
    with open("pok_sounds.csv", "w") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(sounds.items())

pokemons = pokes()
poke_dict = sounds(pokemons)
print(poke_dict)
store(poke_dict)
