plik = open("tekst.txt", "r", encoding="utf-8")

litera = plik.read()
litera = litera.upper()
litera = litera.replace("A", "")
print(litera)
