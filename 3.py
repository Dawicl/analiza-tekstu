plik = open("tekst.txt", "r", encoding="utf-8")


tekst = plik.read()
usuwanie_litery = tekst.upper()
nowy_tekst = usuwanie_litery.replace("A", "")
nowy_tekst = nowy_tekst.capitalize()

plik = open("tekst.txt", "w", encoding="utf-8")
plik.write(nowy_tekst)

plik.close