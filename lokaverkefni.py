from random import *
import time

class Kind:
    def __init__(self, _nafn, _tyngd, _mjolk, _ull, _fjoldiafkvaema, _laeri, _frjosemi, _bakvodvi, _malir, _papi, _madre):
        self.nafn = _nafn
        self.tyngd = _tyngd
        self.mjolk = _mjolk
        self.ull = _ull
        self.afkvaemi = _fjoldiafkvaema
        self.laeri = _laeri
        self.frjosemi = _frjosemi
        self.bakvodvi = _bakvodvi
        self.malir = _malir
        self.papi = _papi
        self.madre = _madre
        self.listi = [_tyngd, _mjolk, _ull, _fjoldiafkvaema, _laeri, _frjosemi, _bakvodvi, _malir]

spilari = []
tolva = []

def Deal():
    while len(spil) > 0:
        spilari.append(spil.pop(randint(0, len(spil) - 1)))
        tolva.append(spil.pop(randint(0, len(spil) - 1)))

def Turn(_numerADoti):
    sigurvegari = gera
    numerADoti = int(_numerADoti) - 1
    afgangur = []
    if spilari[0].listi[numerADoti] > tolva[0].listi[numerADoti]:
        sigurvegari = 1
        spilari.append(spilari.pop(0))
        spilari.append(tolva.pop(0))
    elif spilari[0].listi[numerADoti] < tolva[0].listi[numerADoti]:
        sigurvegari = 0
        tolva.append(tolva.pop(0))
        tolva.append(spilari.pop(0))
    elif spilari[0].listi[numerADoti] == tolva[0].listi[numerADoti]:
        afgangur.append(spilari.pop(0))
        afgangur.append(tolva.pop(0))
    time.sleep(3)
    while True:
        if len(afgangur) > 0:
            if spilari[0].listi[numerADoti] > tolva[0].listi[numerADoti]:
                sigurvegari = 1
                for i in afgangur:
                    spilari.append(i)
                afgangur.clear()
                spilari.append(spilari.pop(0))
                spilari.append(tolva.pop(0))
            elif spilari[0].listi[numerADoti] < tolva[0].listi[numerADoti]:
                sigurvegari = 0
                for i in afgangur:
                    tolva.append(i)
                afgangur.clear()
                tolva.append(tolva.pop(0))
                tolva.append(spilari.pop(0))
            elif spilari[0].listi[numerADoti] == tolva[0].listi[numerADoti]:
                afgangur.append(spilari.pop(0))
                afgangur.append(tolva.pop(0))
        else:
            break
    if sigurvegari == 1:
        print("  _     __       _                   _ ")
        print(" | |_ _/_/  __ _(_)_ _  _ _ _  _ _ _| |")
        print(" | -_) || | \ V / | ' \| ' \ || | '_|_|")
        print(" |_|  \_,_|  \_/|_|_||_|_||_\_,_|_| (_)\n")
        time.sleep(3)
    elif sigurvegari == 0:
        print("  _____ _   _ _                     _                   _ ")
        print(" |_   _(_)_(_) |_ ____ _ _ _   __ _(_)_ _  _ _ _  _ _ _| |")
        print("   | |  / _ \| \ V / _` | ' \  \ V / | ' \| ' \ || | '_|_|")
        print("   |_|  \___/|_|\_/\__,_|_||_|  \_/|_|_||_|_||_\_,_|_| (_)\n")
        time.sleep(3)
    afgangur.clear()
    return sigurvegari

def Spil(spilari):
    bil19 = "                   "
    bil11 = "           "
    bil6 = "      "
    nafn = bil19.replace(" ", spilari[0].nafn.split(" ")[0] + " " + spilari[0].nafn.split(" ")[1], 1)[0:19]
    stadur = bil19.replace(" ", spilari[0].nafn.split(" ")[2], 1)[0:19]
    tyngd = bil6.replace(" ", spilari[0].tyngd, 1)[0:6]
    mjolk = bil6.replace(" ", spilari[0].mjolk, 1)[0:6]
    ull = bil6.replace(" ", spilari[0].ull, 1)[0:6]
    afkvaemi = bil6.replace(" ", spilari[0].afkvaemi, 1)[0:6]
    laeri = bil6.replace(" ", spilari[0].laeri, 1)[0:6]
    frjosemi = bil6.replace(" ", spilari[0].frjosemi, 1)[0:6]
    bakvodvi = bil6.replace(" ", spilari[0].bakvodvi, 1)[0:6]
    malir = bil6.replace(" ", spilari[0].malir, 1)[0:6]
    papi = bil11.replace(" ", spilari[0].papi, 1)[0:11]
    madre = bil11.replace(" ", spilari[0].madre, 1)[0:11]
    print("\t              _                  _ _ ")
    print("\t             | |                | (_)")
    print("\t  _ __   ___ | |_ __ _ _ __   __| |_ ")
    print("\t | '_ \ / _ \| __/ _` | '_ \ / _` | |")
    print("\t | | | | (_) | || (_| | | | | (_| | |")
    print("\t |_| |_|\___/ \__\__,_|_| |_|\__,_|_|")
    print("\t╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮")
    print("\t┃      ┌──╮               ╭──┐      ┃")
    print("\t┃      │┌─┴───────────────┴─┐│      ┃")
    print("\t┃      ││" + nafn + "││      ┃")
    print("\t┃      └┤" + stadur + "├┘      ┃")
    print("\t┃   ╭───╰───────────────────╯───╮   ┃")
    print("\t┃   │                  ,@;@,    │   ┃")
    print("\t┃   │     ,@;@;@;@;@;@/ )@;@;   │   ┃\t\t\t1 = Þyngd í kílóum")
    print("\t┃   │   ,;@;@;@;@;@;@|_/@' e\   │   ┃")
    print("\t┃   │  (|@;@:@\@;@;@;@:@(    \  │   ┃\t\t\t2 = Mjólkurlagni dætra")
    print("\t┃   │    '@;@;@|@;@;@;@;'`''''  │   ┃")
    print("\t┃   │     '@;@;/;@;/;@;'        │   ┃\t\t\t3 = Einkunn ullar")
    print("\t┃   │      ) //   | ||          │   ┃")
    print("\t┃   │      \ \    | ||          │   ┃\t\t\t4 = Fjöldi afkvæma")
    print("\t┃   │       \  \  ) \           │   ┃")
    print("\t┃   │        '''  ''''          │   ┃\t\t\t5 = Einkunn læris")
    print("\t┃   ├──────┬──────┬──────┬──────┤   ┃")
    print("\t┃   │     1│     2│     3│     4│   ┃\t\t\t6 = Frjósemi")
    print("\t┃   │" + tyngd + "│" + mjolk + "│" + ull + "│" + afkvaemi + "│   ┃")
    print("\t┃   ├──────┼──────┼──────┼──────┤   ┃\t\t\t7 = Gerð / þykkt bakvöðva")
    print("\t┃   │     5│     6│     7│     8│   ┃")
    print("\t┃   │" + laeri + "│" + frjosemi + "│" + bakvodvi + "│" + malir + "│   ┃\t\t\t8 = Einkunn fyrir malir")
    print("\t┃   ╰───╭──┴──────┴──────┴──╮───╯   ┃")
    print("\t┃      ┌┤Faðir:  " + papi + "├┐      ┃")
    print("\t┃      ││Móðir:  " + madre + "││      ┃")
    print("\t┃      │└┬─────────────────┬┘│      ┃")
    print("\t┃      └─╯                 ╰─┘      ┃")
    print("\t╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯")

def SpilTolva(spilari):
    bil19 = "                   "
    bil11 = "           "
    bil6 = "      "
    nafn = bil19.replace(" ", spilari[0].nafn.split(" ")[0] + " " + spilari[0].nafn.split(" ")[1], 1)[0:19]
    stadur = bil19.replace(" ", spilari[0].nafn.split(" ")[2], 1)[0:19]
    tyngd = bil6.replace(" ", spilari[0].tyngd, 1)[0:6]
    mjolk = bil6.replace(" ", spilari[0].mjolk, 1)[0:6]
    ull = bil6.replace(" ", spilari[0].ull, 1)[0:6]
    afkvaemi = bil6.replace(" ", spilari[0].afkvaemi, 1)[0:6]
    laeri = bil6.replace(" ", spilari[0].laeri, 1)[0:6]
    frjosemi = bil6.replace(" ", spilari[0].frjosemi, 1)[0:6]
    bakvodvi = bil6.replace(" ", spilari[0].bakvodvi, 1)[0:6]
    malir = bil6.replace(" ", spilari[0].malir, 1)[0:6]
    papi = bil11.replace(" ", spilari[0].papi, 1)[0:11]
    madre = bil11.replace(" ", spilari[0].madre, 1)[0:11]
    print("\t  _  _   _ _                  ")
    print("\t | |(_) (_) |                 ")
    print("\t | |_ ___ | |_   ____ _ _ __  ")
    print("\t | __/ _ \| \ \ / / _` | '_ \ ")
    print("\t | || (_) | |\ V / (_| | | | |")
    print("\t  \__\___/|_| \_/ \__,_|_| |_|")
    print("\t╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮")
    print("\t┃      ┌──╮               ╭──┐      ┃")
    print("\t┃      │┌─┴───────────────┴─┐│      ┃")
    print("\t┃      ││" + nafn + "││      ┃")
    print("\t┃      └┤" + stadur + "├┘      ┃")
    print("\t┃   ╭───╰───────────────────╯───╮   ┃")
    print("\t┃   │    ._________________.    │   ┃")
    print("\t┃   │    | _______________ |    │   ┃")
    print("\t┃   │    | I             I |    │   ┃")
    print("\t┃   │    | I             I |    │   ┃")
    print("\t┃   │    | I             I |    │   ┃\t\t\t1 = Þyngd í kílóum")
    print("\t┃   │    | I             I |    │   ┃")
    print("\t┃   │    | I_____________I |    │   ┃\t\t\t2 = Mjólkurlagni dætra")
    print("\t┃   │    !_________________!    │   ┃")
    print("\t┃   │       ._[_______]_.       │   ┃\t\t\t3 = Einkunn ullar")
    print("\t┃   │   .___|___________|___.   │   ┃")
    print("\t┃   │   |::: ____           |   │   ┃\t\t\t4 = Fjöldi afkvæma")
    print("\t┃   │   |    ~~~~ [CD-ROM]  |   │   ┃")
    print("\t┃   │   !___________________!   │   ┃\t\t\t5 = Einkunn læris")
    print("\t┃   ├──────┬──────┬──────┬──────┤   ┃")
    print("\t┃   │     1│     2│     3│     4│   ┃\t\t\t6 = Frjósemi")
    print("\t┃   │" + tyngd + "│" + mjolk + "│" + ull + "│" + afkvaemi + "│   ┃")
    print("\t┃   ├──────┼──────┼──────┼──────┤   ┃\t\t\t7 = Gerð / þykkt bakvöðva")
    print("\t┃   │     5│     6│     7│     8│   ┃")
    print("\t┃   │" + laeri + "│" + frjosemi + "│" + bakvodvi + "│" + malir + "│   ┃\t\t\t8 = Einkunn fyrir malir")
    print("\t┃   ╰───╭──┴──────┴──────┴──╮───╯   ┃")
    print("\t┃      ┌┤Faðir:  " + papi + "├┐      ┃")
    print("\t┃      ││Móðir:  " + madre + "││      ┃")
    print("\t┃      │└┬─────────────────┬┘│      ┃")
    print("\t┃      └─╯                 ╰─┘      ┃")
    print("\t╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯")

spil = []
with open("spilastokkur.txt", "r", encoding="utf-8") as f:
    for i in f.readlines():
        a = i.split(",")
        if "\n" in a[10]:
            a[10] = a[10].replace("\n", "")
        spil.append(Kind(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10]))
#Leikreglur eru settar í þennan allt of langa texta
print("\nLEIKREGLUR")
print("\n\tLeikurinn, eins og flestir leikir, gengur út á það að sigra.")
print("\tSá leikmaður hlotnast sigur sem eftir stendur þegar hinu/m leikmönnum er tortýmt.")
print("\tSpilunum 52 er skipt á milli leikmanna, sama hversu margir þeir eru.")
print("\tAllir leikmenn draga spil og sá sem á leikinn velur eiginleika,")
print("\tsíðan bera allir leikmenn saman töluna undir eiginleikanum sem varð fyrir valinu.")
print("\n\t1 = Þyngd í kílóum\t\t2 = Mjólkurlagni dætra\t\t3 = Einkunn ullar\t\t\t\t4 = Fjöldi afkvæma")
print("\n\t5 = Einkunn læris\t\t6 = Frjósemi\t\t\t\t7 = Gerð / þykkt bakvöðva\t\t8 = Einkunn fyrir malir")

sigurvegari = 1
flag = True
while flag == True:
    Deal()
    print("\nNú hefst leikurinn!\n")
    while flag == True:
        if len(spilari) <= 0:
            print("Tölvan er sigurvegarinn!")
            break
            flag = False
        elif len(tolva) <= 0:
            print("Þú ert sigurvegarinn!")
            break
            flag = False
        gera = sigurvegari
        Spil(spilari)
        numerADotiTilAdNotaTilTessAdBeraSamanVidOnnurDotHjaOdrumSpilurum = -1

        print("Það eru", len(spilari), "spil í stokknum þínum")
        if gera == 1:
            numerADotiTilAdNotaTilTessAdBeraSamanVidOnnurDotHjaOdrumSpilurum = input("Hvaða eiginleika viltu nota?: ")
        elif gera == 0:
            numerADotiTilAdNotaTilTessAdBeraSamanVidOnnurDotHjaOdrumSpilurum = randint(1,8)
            print("Spil tölvunnar er...")
            SpilTolva(tolva)
            print("Tölvan velur", str(numerADotiTilAdNotaTilTessAdBeraSamanVidOnnurDotHjaOdrumSpilurum)+"!")
        if gera == 1:
            print("Spil tölvunnar er...")
            SpilTolva(tolva)
        sigurvegari = Turn(numerADotiTilAdNotaTilTessAdBeraSamanVidOnnurDotHjaOdrumSpilurum)
