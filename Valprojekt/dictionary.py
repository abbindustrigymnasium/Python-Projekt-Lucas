from random import randint

Höger = bool  // en bol som visar om partiet är höger eller vänster inriktat

Göling = {
    "name": "Gröngölingarna", // namnet på partier
    Höger: False, // om det är false är partiet vänster inriktat och om det är true är det tvärt om.
    "Block": "Småpartierna", // vilket block partiet tillhör
    min: 3, // minsta antal röster som partiet kan få
    max: 12, // hur många röster partiet kan få som mest
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

parties = [ // en lista med alla partierna 
    Göling,
    Partikel,
    Mälar,
    Rövar,
    Extrem,
    Maskin,
    Fram,
    All
]




def randomvote(a, b): // funktionen för att få fram ett random antal röster
    for i in a:
        b.append(randint(i[min], i[max])) // säger att de ska vara ett värde mellan partiets min och max värde
    if sum(b) != 100: // om det är över 100% av antal röster kommer allt funktionen köras igen.
        b.clear()
        randomvote(a, b)
