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

spilarar = []

def Deal(_spilarar):
    tel = 0
    for i in range(spilararSpurning):
        spilarar.append([])
    for i in range(500):
        if 52 - i >= spilararSpurning - tel:
            randomTala = randint(0, len(spil) - 1)
            spilarar[tel].append(spil.pop(randomTala))
        else:
            break
        print(tel)
        if tel >= spilararSpurning - 1:
            tel = 0
        else:
            tel += 1

def Turn(_spilari, _numerADoti):
    sigurvegari = gera
    _numerADoti-=1
    afgangur = []
    for i in range(len(spilarar)):
        if _spilari.listi[_numerADoti] < spilarar[i][0].listi[_numerADoti]:
            sigurvegari = i
        elif _spilari.listi[_numerADoti] == spilarar[i][0].listi[_numerADoti]:
            afgangur.append()#dabdabdabdabdabdabdabdabdabdabdabdabdabdabdabdabdabdabdabdabdabdabdabdabdabdabdabdabdabdabdabdabdabdab

spil = []
with open("spilastokkur.txt", "r", encoding="utf-8") as f:
    for i in f.readlines():
        a = i.split(",")
        if "\n" in a[10]:
            a[10] = a[10].replace("\n", "")
        spil.append(Kind(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10]))
print("Velkominn í örugglega leiðinlegasta leik sem þú munt nokkurn tíman spila.")

gera = 0

while True:
    print("Y O W H A T S U P J I M B O")
    spilararSpurning = int(input("Hversu margir eru að spila?" ))
    Deal(spilararSpurning)
    print("Nú hefst leikurinn!")
    while True:
        numerADotiTilAdNotaTilTessAdBeraSamanVidOnnurDotHjaOdrumSpilurum = input("Hvað viltu gera? ")
        Turn(spilarar[gera], numerADotiTilAdNotaTilTessAdBeraSamanVidOnnurDotHjaOdrumSpilurum)
        print("")
