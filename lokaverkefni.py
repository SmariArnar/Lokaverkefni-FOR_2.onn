class Kind:
    def __init__(self, nafn, tyngd, mjokl, ull, fjoldiafkvaema, laeri, frjosemi, bakvodvi, malir, papi, madre):
        self.nafn = nafn
        self.tyngd = tyngd
        self.mjokl = mjokl
        self.ull = ull
        self.afkvaemi = fjoldiafkvaema
        self.laeri = laeri
        self.frjosemi = frjosemi
        self.bakvodvi = bakvodvi
        self.malir = malir
        self.papi = papi
        self.madre = madre
listi = []
with open("new1.txt","r", encoding="utf-8") as open_file:
    for i in open_file.readlines():
        a = i.split(",")
        listi.append(Kind(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10]))
    for i in listi:
        print(i.nafn,end=" ")
        print(i.tyngd)