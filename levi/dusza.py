
class Jatek:
    def __init__(self,sor):
        szervezo, jatek_nev, jatekosok, *esemeny = sor.strip().split(";")
        self.szervezo   = szervezo
        self.jatek_nev  = jatek_nev
        self.jatekosok  = jatekosok
        self.esemeny    = esemeny


class Fogadasok:
    def __init__(self,sor):
        fogado_neve, melyik_jatek, tet, kire_fogad, esemeny , fogadas_merete = sor.strip().split(";")
        self.fogado_neve    = fogado_neve
        self.melyik_jatek   = melyik_jatek
        self.v            = tet
        self.kire_fogad     = kire_fogad
        self.esemeny  = esemeny 
        self.fogadas_merete = fogadas_merete

print("""1-     Játék létrehozása
2-     Fogadás leadása
3-     Játék lezárása
4-     Lekérdezések
5-     Kilépés""")

menu = input("A menüpont kiválasztásához nyomja meg a megfelelő számot! ")


if menu == "1":
    szervezo = input("Ki a szervező?\t")
    jatek_neve = input("Mi a játék megnevezése? (egyedinek kell lennie\t")
    jatekosok = input("Kik az alanyok? (különböznek egymástól)\t")
    lista = []
    while True:
      esemeny = input("Mik az események? (ha végeztél nyomj entert!)\t")
      lista.append(esemeny)
      if esemeny == "":
          break


    with open("jatekok.txt","a",encoding="UTF-8") as f:
        f.write(f"{szervezo};{jatek_neve};{jatekosok};{esemeny}\n")


"""Fogadás leadása
A fogadás leadásához először is szükség van a fogadó fél nevére, ezt a program tehát kérje be.
Ezután a program írja ki, hogy az adott félnek összesen hány pontja van (amit fel tud
használni). Ennek az értéknek a fogadás leadása közben folyamatosan jelen kell lennie a
felületen.
A felhasználó tudjon választani a még le nem zárt játékok közül, majd a program egy alany és
egy esemény kiválasztásával, valamint egy érték (pontosvesszőt nem tartalmaz) és egy tét
(pozitív egész szám) megadásával adhatja le a fogadását.
A program ellenőrizze, hogy van-e a felhasználónak megfelelő mennyiségű pontja.
A fogadást a fogadasok.txt fájlban rögzítse a program. Egy sorban a fogadó neve, a játék
megnevezése, a tét összege, az alany, az esemény és az érték szerepeljen pontosvesszővel
elválasztva."""

if menu == "2":
    
    with open("fogadasok.txt","r",encoding="UTF-8") as f:
        fogadasok = [Fogadasok(sor) for sor in f]

    fogado_neve = input("Fogadó neve:\t")
    melyik_jatek = input("Melyik játkra fogadsz?\t")
    tet = input(f"Hány pontal fogadsz a '{melyik_jatek}'?\t")
    kire_fogad = input("kire fogadsz?\t")
    esemeny = input("Milyen tipusu fogadást teszel? pl: (sebessége, kimenete,hibát dob, stb...)\t")
    fogadas_mertek = input("Mennyire fogadsz?\t")
    try:
        for sor in fogadasok:
            if fogado_neve == sor.fogado_neve and esemeny == sor.esemeny and kire_fogad == sor.kire_fogad:
                tarolo = 1
    except: 
        pass
  
    if tarolo == 0:    
        with open("fogadasok.txt","a",encoding="UTF-8") as f:
            f.write(f"{fogado_neve};{melyik_jatek};{tet};{kire_fogad};{esemeny};{fogadas_mertek}\n")
    else:
        tarolo = 0





if menu == "3":
    jatekos     = input("Adja meg a nevét! ")
    jatek_neve  = input("Adja meg jaték nevét! ")
    with open("jatekok.txt","a",encoding="UTF-8")as f:
        jatek = [Jatek(sor) for sor in f]
    for sor in jatek: 
        while True:   
            if jatekos == sor.szervezo and sor.jatek_nev == jatek_neve:
                alany   = input("Adja meg a játékos nevét!")
                esemeny = input("Melyik esemény!")


    with open("eredmenyek.txt","a",encoding="UTF-8") as f:
        for sor in jatek:
            f.write(f"{sor.jatek_nev}\n")
            break
        

    for sor in fogadasok:
        pont = sor.tet
        sec = sor.fogadas_merete
        
        
            
        
        
    

        

if menu == "4":
    pass
if menu == "5":
    pass

