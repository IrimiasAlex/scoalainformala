import datetime


class Validator:

    def __init__(self, cnp):
        self.CNP = cnp

    def lungime(self):
        if len(self.CNP) != 13:
            return False
        return True

    def sex(self):
        if self.CNP[0] != "0":
            return True
        return False

    def data(self):
        data = slice(1, 7, 1)
        data_n = self.CNP[data]
        date = data_n
        try:
            datetime.datetime.strptime(date, "%y%m%d")
            return True
        except ValueError:
            return False

    def judet(self):
        judet = int(self.CNP[7:9])
        if judet not in range(1, 47) and (51, 53):
            return False
        return True

    def nnn(self):
        nnn_verificat = int(self.CNP[9:12])
        if nnn_verificat in range(1, 1000):
            return True
        return False

    def caractere_cnp(self):
        if self.CNP.isdigit():
            return True
        return False

    def c(self):
        nr_control = (2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9)
        val = sum(a * int(b) for a, b in zip(nr_control, self.CNP)) % 11
        return '1' if val == 10 else str(val)

    def __str__(self):
        if self.lungime() is True and self.sex() is True and self.data() is True and self.judet() is True and self.caractere_cnp() is True and self.nnn() is True and self.c() == self.CNP[12]:
            return f"Cnp-ul  {self.CNP} este valid"
        return f"Cnp-ul  {self.CNP} nu este valid"


obiect_1 = Validator(input("Introduceti CNP-ul :"))
print(obiect_1)

