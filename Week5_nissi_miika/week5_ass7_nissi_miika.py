finengdict = {
    "Punainen":"Red",
    "Sininen":"Blue",
    "Vihreä":"Green",
    "Yksisarvinen":"Unicorn",
    "Epämuodostunut":"Deformed",
    "Vuosi":"Year",
    "Puu":"Tree",
    "Pannukakku":"Pancake",
    "Apina":"Monkey",
    "Kissa":"Cat",
    "Koira":"Dog"
}
while True:
    sana = input("Enter a finnish word, 0 to exit: ")
    if sana == "0": break
    try:
        x = finengdict[sana.capitalize()]
        print(sana, "in English is", x)
    except KeyError:
        print("Word not found in dictionary.")
