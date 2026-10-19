getal1=float(input("Geef getal1:"))
getal2=float(input("geef getal2:"))
bewerking = input("welke bewerking wil je uitvoeren? (+,-,/,*,m):")

if bewerking == "+":  #== : is gelijk aan ; <= : kleiner dan of gelijk aan ; < : kleiner dan; != : Niet gelijk aan
    print(f"{getal1} + {getal2} = {getal1+getal2}.")

if bewerking == "_":
    print(f"{getal1} - {getal2} = {getal1-getal2}.")

if bewerking == "/":
    print(f"{getal1} / {getal2} = {getal1/getal2}.")

if bewerking == "*":
    print(f"{getal1} * {getal2} = {getal1*getal2}.")

if bewerking == "m":
    print(f"{getal1} ** {getal2} =  {getal1**getal2}")