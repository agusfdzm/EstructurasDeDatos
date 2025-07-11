# Array
personajes_one_piece = [
    "Monkey D. Luffy",
    "Roronoa Zoro",
    "Nami",
    "Usopp",
    "Sanji",
    "Tony Tony Chopper",
    "Nico Robin",
    "Franky",
    "Brook",
    "Jinbe",
    "Portgas D. Ace",
    "Gol D. Roger",
    "Shanks",
    "Marshall D. Teach (Barbanegra)",
    "Trafalgar D. Water Law",
    "Eustass Kid",
    "Boa Hancock",
    "Dracule Mihawk",
    "Donquixote Doflamingo",
    "Kaido"
]

# Acceder por ejemplo a la posición 10:
for i in range(len(personajes_one_piece)):
    if i == 10:
        print(f"{personajes_one_piece[i]} es el personaje en la posición 10 del array")