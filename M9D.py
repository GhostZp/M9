import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def accelerate(self, nopeuden_muutos):
        self.nopeuden_muutos = nopeuden_muutos
        self.nopeus += nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, hour_count):
        self.hour_count = hour_count
        self.matka += (self.nopeus * hour_count)

autot = []
maali = False
for i in range(1, 11):
    huippu_nopeus = random.randint(100,200)
    auto = Auto(f"ABC-{i}", huippu_nopeus)
    autot.append(auto)

while maali != True:
    for auto in autot:
        auto.accelerate(random.randint(-10, 15))
        auto.kulje(1)
        if auto.matka >= 10000:
            maali = True

for auto in autot:
    print(f"""
    =============================================
    | Rekisteritunnus: {auto.rekisteritunnus}
    | Nopeus: {auto.nopeus} km/h
    | Huippunopeus:{auto.huippunopeus} km/h 
    | Matka: {auto.matka} km
    =============================================
    """)