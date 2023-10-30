class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

auto = Auto("ABC-123", 142)

print(f"{auto.rekisteritunnus:s}, {auto.huippunopeus}km/h, {auto.nopeus} {auto.matka}")
