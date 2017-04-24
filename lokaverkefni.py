class Kind:
    def __self__(self, _nafn, _tyngd, _mjokl, _ull, _fjoldiafkvaema, _laeri, _frjosemi, _bakvodvi, _malir, _papi, _madre):
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

listi1 = []
listi2 = []

skra = []
hermadur = Kind
print (hermadur)
with open("new1.txt", "r", encoding="utf-8") as f:
    for i in f.readlines():
        a = i.split(",")
        print(a)
        print(i)
        skra.append(hermadur(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10]))

print(skra[3].mjokl)
print("Velkominn í örugglega leiðinlegasta leik sem þú munt nokkurn tíman spila.")
