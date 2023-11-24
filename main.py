"""
Fogadás leadása
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
elválasztva.

A fenti példában három fogadás szerepel, mindegyik külön sorban. Az első sor azt jelenti, hogy
Kovács Imre a „Lajos és Bettina programjának futása” megnevezésű játékban 10 ponttal arra
fogadott, hogy Lajos programfutásának sebessége 6 (ms) lesz. A második sor azt jelenti, hogy
ugyanebben a játékban 23 pontot tett fel arra, hogy Lajos programjának kimenete „Hello
World” lesz. A harmadik sor szerint pedig Oláh Margit 20 pontot tett fel arra, hogy Lajos
programfutásának sebessége 8 (ms) lesz.
Ugyanaz a felhasználó ugyanarra az alany + esemény párosra csak egyszer fogadhat.

Ugyanaz a felhasználó ugyanarra az alany + esemény párosra csak egyszer fogadhat.
"""

"""
fogado_neve; jatek_neve; tet; alany; esemeny; ertek
Kovács Imre;Lajos és Bettina programjának futása;10;Lajos;programfutásánaksebessége;6
Kovács Imre;Lajos és Bettina programjának futása;23;Lajos;programjánakkimenete;Hello World
Oláh Margit;Lajos és Bettina programjának futása;20;Lajos;programfutásánaksebessége;8
Loic; soccer; 10; Adriano; skills; 12
Leandro; soccer; 23; Adriano; goals; 3
Hugo; baseball; 14; Thomas; Hits; 35
Max; snooker; 21; Lex; legjobb a bajnoksában a hónapban; 6
"""


class Fogadas():
    def __init__(self, sor):
        fogado_neve, jatek_neve, tet, alany, esemeny, ertek = sor.strip().split(";")
        self.fogado_neve = fogado_neve
        self.jatek_neve = jatek_neve
        self.tet = int(tet)
        self.alany = alany
        self.esemeny = esemeny
        self.ertek = ertek




with open("fogadasok.txt", "a", encoding="utf-8") as g:
    fog_fel = input("Kérem adjon meg egy nevet! ")
    jat_nev = input("Kérem a játék nevét! ")
    tetpont = int(input("Kérem adja meg mennyi creditet szeretne felhasználni! "))
    kire = input("Ki-re szeretnél fogadni? ")
    esem_j = input("Kérem adjon meg egy esemény nevet!(Ha már fogadtál egy eseményre, akkor arra nem fogadhatsz!) ")
    esem_ert = input("Kérem adja meg mire fogadnál! ")
    bekeres = g.write(f"{fog_fel}; {jat_nev}; {tetpont}; {kire}; {esem_j}; {esem_ert}\n")

with open("fogadasok.txt", "r", encoding="utf-8") as f:
    fejlec = f.readline()
    lista = [Fogadas(sor) for sor in f]

credit = int(100)
gyujto = []
maradek_credit = []

beker_esemeny = input("Kérek egy eseményt nevet! ")
esemenyl = []     
def teszt_esemeny():
    for sor in lista:
        for sor in sor.esemeny:
            if sor.esemeny == beker_esemeny:
                esemenyl.append(sor.esemeny)
    return esemenyl

esemenyf = []
beker_ertek = input("Kérek egy értéket! ")
def teszt_ertek():
    for sor in lista:
        for sor in esemenyl:
            if sor.ertek == beker_ertek: 
                esemenyf.append(sor.ertek)
    return esemenyf


