from random import *

class Kind:
    def __init__(self, _nafn, _tyngd, _mjokl, _ull, _fjoldiafkvaema, _laeri, _frjosemi, _bakvodvi, _malir, _papi, _madre):
        self.nafn = _nafn
        self.tyngd = _tyngd
        self.mjokl = _mjokl
        self.ull = _ull
        self.afkvaemi = _fjoldiafkvaema
        self.laeri = _laeri
        self.frjosemi = _frjosemi
        self.bakvodvi = _bakvodvi
        self.malir = _malir
        self.papi = _papi
        self.madre = _madre
        self.listi = [_tyngd, _mjokl, _ull, _fjoldiafkvaema, _laeri, _frjosemi, _bakvodvi, _malir]

def PrentaSpil(_spilari):
    print("xd rawr")

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
        print("Þú vinnur þennan leik!")
    elif sigurvegari == 0:
        print("Tölvan vinnur þennan leik!")
    afgangur.clear()
    return sigurvegari

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

while True:
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
            flag == False
        gera = sigurvegari
        print(spilari[0].nafn, spilari[0].listi)
        numerADotiTilAdNotaTilTessAdBeraSamanVidOnnurDotHjaOdrumSpilurum = -1

        print("Spilari:", len(spilari), "Tölva:", len(tolva))
        if gera == 1:
            numerADotiTilAdNotaTilTessAdBeraSamanVidOnnurDotHjaOdrumSpilurum = input("Hvaða eiginleika viltu nota?: ")
        elif gera == 0:
            numerADotiTilAdNotaTilTessAdBeraSamanVidOnnurDotHjaOdrumSpilurum = randint(1,8)
            print("Tölvan dróg",tolva[0].nafn, tolva[0].listi)
            print("tölvan ákvað eftir mikla íhugun að nota númer", numerADotiTilAdNotaTilTessAdBeraSamanVidOnnurDotHjaOdrumSpilurum)
        if gera == 1:
            print("Tölvan dróg",tolva[0].nafn, tolva[0].listi)
        sigurvegari = Turn(numerADotiTilAdNotaTilTessAdBeraSamanVidOnnurDotHjaOdrumSpilurum)