prijs = float(input("Hoeveel euro betaalde je voor je zonnepanelen? "))
premie = prijs * 0.20
if premie <= 600:
    print(f"Je krijgt een premie van", premie, "euro.")

if premie > 600:
    print(f"Je krijgt een premie van 600 euro")