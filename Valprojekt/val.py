from random import randint
from dictionary import parties, Höger, randomvote // importar listan med partier, boolen och random funktionen

print("\n")

randomvotelist = []

randomvote(parties, randomvotelist)

for i in parties:
    i.update({"vote": randomvotelist[parties.index(i)]})

for i in parties:
    if i["vote"] >= 4:
        print(i["name"], "got", i["vote"], "percent of the vote.\n") // skriver ut om partiet fick över 4% av rösterna och kom in på riksdagen
    else:
        print(i["name"], "got too few votes to get in the Riksdag, with",
              i["vote"], "percent of the vote.\n") // skriver ut om partiet inte fick över 4% och då inte kom in i riksdagen

vänsterröst = 0 // sätter startvärdet för antal röster vänsterinriktade partier fått
högerröst = 0 // sätter startvärdet för antal röster högerinriktade partier fått

småpartröst = 0 // sätter startvärdet för antal röster småpartierna fått
oljeblockröst = 0 //sätter startvärdet för antal röster oljeblocket fått

for i in parties:
    if i[Höger] == True:
        högerröst += i["vote"] // om partiet är ett höger inriktat partie och har fått en röst kommer den läggas till i högerröst
    else:
        vänsterröst += i["vote"] // om partiet är ett vänster inriktat partie och har fått en röst kommer den läggas till i vänsterröst
    if i["Block"] == "Småpartierna": // om partiet tillhör småpartierna och har fått en röst kommer den läggas till i småpartröst
        småpartröst += i["vote"]
    elif i["Block"] == "Oljeblocket": // om partiet tillhör oljeblocket och har fått en röst kommer den läggas till i oljeblockröst
        oljeblockröst += i["vote"]

print("\nSmåpartierna got", småpartröst, "percent of vote.") // skriver ut hur många % av rösterna småpartierna har fått
print("Oljeblocket got", oljeblockröst, "percent of vote.\n") // skriver ut många % av rösterna oljeblocket har fått

print("\n Left wing parties got",
      vänsterröst, "percent of vote.") // skriver ut hur många % av rösterna vänster inriktade partier fått
print("Right wing parties got",
      högerröst, "percent of vote.") // skriver ut hur många % av rösterna höger inriktade partier fått



