class Telefon:
    counter = 0

    def __init__(self, numar):
        self.numar = numar
        Telefon.counter += 1

    def apelare(self, numar):
        mesaj = f'Apelati {numar} utilizand propriul numar de telefon'
        return mesaj

class TelefonFix(Telefon):

    last_sn = 0

    def __init__(self, numar):
        super().__init__(numar)
        TelefonFix.last_sn += 1
        self.SN = f'Telefon fix - {TelefonFix.last_sn}'

class TelefonMobil(Telefon):

    last_sn = 0

    def __init__(self, numar):
        super().__init__(numar)
        TelefonMobil.last_sn += 1
        self.SN = f'Telefon mobil - {TelefonMobil.last_sn}'

print(f' Numarul total de dispozitive este {Telefon.counter}')
fix_1 = TelefonFix('0264 265 602')
fix_2 = TelefonFix('0264 265 832')
mobil = TelefonMobil('0745 77 21 89')
print(f' Numarul total de dispozitive fixe este {TelefonFix.last_sn}')
print(f' Numarul total de dispozitive mobile este {TelefonMobil.last_sn}')
print(f' Numarul total de dispozitive este {Telefon.counter}')
