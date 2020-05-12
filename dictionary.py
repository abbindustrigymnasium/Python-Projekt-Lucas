from random import randint

Höger = bool

Göling = {
    "name": "Gröngölingarna",
    Höger: False,
    "Block": "Småpartierna",
    min: 3,
    max: 12,
}
Partikel = {
    "name": "Partikelpartiet",
    Höger: False,
    "Block": "Småpartierna",
    min: 2,
    max: 8,
}
Mälar = {
    "name": "Mälarpartiet",
    Höger: True,
    "Block": "Småpartierna",
    min: 8,
    max: 18,
}
Rövar = {
    "name": "Sjörövarpartiet",
    Höger: True,
    "Block": "Småpartierna",
    min: 3,
    max: 12,
}
Extrem = {
    "name": "Extremisterna",
    Höger: True,
    "Block": "Oljeblocket",
    min: 3,
    max: 6,
}
Maskin = {
    "name": "Maskinpartiet",
    Höger: False,
    "Block": "Oljeblocket",
    min: 12,
    max: 22,
}
Fram = {
    "name": "Framtidspartiet",
    Höger: True,
    "Block": "Oljeblocket",
    min: 12,
    max: 18,
}
All = {
    "name": "Allpartiet",
    Höger: False,
    "Block": "None",
    min: 20,
    max: 34,
}

parties = [
    Göling,
    Partikel,
    Mälar,
    Rövar,
    Extrem,
    Maskin,
    Fram,
    All
]




def randomvote(a, b):
    for i in a:
        b.append(randint(i[min], i[max]))
    if sum(b) != 100:
        b.clear()
        randomvote(a, b)
