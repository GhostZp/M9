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


auto = Auto("ABC-123", 142)

auto.accelerate(30)
auto.accelerate(70)
auto.accelerate(50)

print(f"{auto.nopeus}km/h.")

auto.accelerate(-200)

print(f"{auto.nopeus}km/h.")
