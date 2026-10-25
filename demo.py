import cv2#OpenCV könyvtár importálása a képfeldolgozáshoz
import argparse #Argparse könyvtár importálása a parancssori argumentumok feldolgozásához
import os #OS könyvtár importálása a fájlok és mappák kezeléséhez
import sys #Sys könyvtár importálása a rendszerfunkciókhoz, például a kilépéshez
'''
A program célja, hogy egy bemeneti képet feldolgozzon, és a hisztogram kiegyenlítését alkalmazza rajta.
Az OpenCV hisztogram kiegyenlítő függvényét használja a kép feldolgozásához.
Ez anonban csak szürkeárnyalatos képeken működik, ezért a bemeneti képet szürkeárnyalatos módban olvassa be.
Amennyiben minden sikeresen lefut egy kiegyenlített hisztogramú szürkeárnyalatos képet ment a megadott kimeneti útvonalra.

A program a következő lépéseket hajtja végre:
1. Ellenőrzi, hogy a bemeneti fájl létezik-e.
2. Beolvassa a képet szürkeárnyalatos módban.
3. Kiegyenlíti a kép hisztogramját.
4. Mentse a feldolgozott képet a megadott kimeneti útvonalra.
5. Ellenőrzi, hogy a kép mentése sikeres volt-e.
Bárhol a fenti lépések bármelyike sikertelen, a program hibaüzenetet ír ki, és kilép az 1-es hibakóddal.
Ez a hibakód jelzi a GitHub pipelinak, hogy a program hibába ütközött, ez miatt nem kerül a pipeline a következő lépésre.

A program parancssori argumentumokat használ a bemeneti és kimeneti fájlok elérési útjának megadásához.
Az argparse modul kezeli a parancssori argumentumokat, és biztosítja, hogy a felhasználó megadja a szükséges bemeneti és kimeneti fájlokat.
Hibás argumentumok esetén a modul biztosítja, hogy a felhasználó megkapja magfelelő hibaüzenetet.
-h vagy --help argumentumokkal a felhasználó megkapja a program használatára vonatkozó információkat.
'''


# Függvény a kép feldolgozásához
def process_image(input_path, output_path):

    # Ellenőrizzük, hogy a bemeneti fájl létezik-e, és amennyiben nem, akkor kilépünk a programból
    if not os.path.exists(input_path):
        print(f"A bemeneti fálj nem található: {input_path}")
        sys.exit(1)

    # Beolvassuk a képet szürkeárnyalatos módban, mivel a hisztogram kiegyenlítés szürkeárnyalatos képeken működik
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # Ellenőrizzük, hogy a kép sikeresen be lett-e olvasva, és ha nem, akkor kilépünk a programból
    if img is None:
        print(f"Nem sikerült beolvasni a képet")
        sys.exit(1)

    # Kiegyenlítsük a kép hisztogramját
    eqh = cv2.equalizeHist(img)

    # Mentjük a feldolgozott képet, és ennek sikeressége a result változóban lesz tárolva
    result = cv2.imwrite(output_path, eqh)

    # Ellenőrizzük, hogy a kép mentése sikeres volt-e
    if result :
        print(f"A feldolgozott kép sikeresen mentve: {output_path}")
    else:
        print(f"Hiba történt a kép mentése közben")
        sys.exit(1)


if __name__ == "__main__":
    # Argumentumok feldolgozása
    parser = argparse.ArgumentParser(description="Kép hisztogramjának kiegyenlítése")

    # Argumentumok hozzáadása a parancssori interfészhez
    parser.add_argument("input",  help="Bemeneti kép elérési útja")
    parser.add_argument("output",  help="Kimeneti kép elérési útja")

    # A parancssori argumentumok feldolgozása
    args = parser.parse_args()

    # A process_image függvény meghívása a megadott bemeneti és kimeneti útvonalakkal
    process_image(args.input, args.output)
