plik = open("tekst.txt", "r", encoding="utf-8")
plik2 = open ("wynik.txt", "w", encoding="utf-8")

alfabet = "ABCDEFGHIJKLMNOPRSTUVWXYZ"

alfabet1 = plik.read()
alfabet1 = alfabet1.upper()

for litera in alfabet:
    for litera1 in alfabet1:
        a = alfabet1.count(litera)
        plik2.write(litera)
        plik2.write("-")
        plik2.write(str(a))
        plik2.write(" ")
        break
    
wynik2 = str(len(alfabet1))  
plik2.write("\nCały tekst zawiera ") 
plik2.write(wynik2)
plik2.write(" znaków")