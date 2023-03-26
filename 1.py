plik = open("tekst.txt", "r", encoding="utf-8")
plik2 = open ("wynik.txt", "w", encoding="utf-8")

alfabet = "ABCDEFGHIJKLMNOPRSTUVWXYZ"

tekst = plik.read()
tekst = tekst.upper()

for litera in alfabet:
    ilosc_znakow = tekst.count(litera)
    plik2.write(litera)
    plik2.write("-")
    plik2.write(str(ilosc_znakow))
    plik2.write(" - jest to ")
    tekst_bezspacji = tekst.replace(" ", "") 
    dzielnik = int(len(tekst_bezspacji))
    procent = ilosc_znakow / dzielnik
    procent = round(procent, 2)
    plik2.write(str(procent))
    plik2.write("% znaków w tekście.")
    plik2.write("\n")

usuwanie_spacji = tekst.replace(" ", "")    
zliczanie_znakow = str(len(usuwanie_spacji))  
plik2.write("\nCały tekst zawiera ") 
plik2.write(zliczanie_znakow)
plik2.write(" znaków")

plik.close
plik2.close