from random import randint
from dictionary import parties, Höger, randomvote

print("\n")

randomvotelist = []

randomvote(parties, randomvotelist)

for i in parties:
    i.update({"vote": randomvotelist[parties.index(i)]})

for i in parties:
    if i["vote"] >= 4:
        print(i["name"], "got", i["vote"], "percent of the vote.\n")
    else:
        print(i["name"], "got too few votes to get in the Riksdag, with",
              i["vote"], "percent of the vote.\n")

vänsterröst = 0
högerröst = 0

småpartröst = 0
oljeblockröst = 0

for i in parties:
    if i[Höger] == True:
        högerröst += i["vote"]
    else:
        vänsterröst += i["vote"]
    if i["Block"] == "Småpartierna":
        småpartröst += i["vote"]
    elif i["Block"] == "Oljeblocket":
        oljeblockröst += i["vote"]

print("\nSmåpartierna got", småpartröst, "percent of vote.")
print("Oljeblocket got", oljeblockröst, "percent of vote.\n")

print("\n Left wing parties got",
      vänsterröst, "percent of vote.")
print("Right wing parties got",
      högerröst, "percent of vote.")



