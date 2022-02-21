
cnp = []
def S(cnp):
    gen = int(cnp[0])
    if gen in [1, 2, 3, 4, 5, 6]:
        return True
    return False


def LL(cnp):
    if int(cnp[3:5]) in range(1, 13):
        return True
    return False


def ZZ(cnp):
    if int(cnp[5:7]) in range(1, 32):
        return True
    return False


def JJ(cnp):
    if int(cnp[7:9]) in range(1, 53):
        return True
    return False


def NNN(cnp):
    if int(cnp[9:12]) in range(1, 999):
        return True
    return False


def C(cnp):
    if int(cnp[12]) in range(0, 10):
        return True
    return False


def CNP():
    cod_numeric_util = input("Introduceti-va CNP-ul dvs: ")
    while len(cod_numeric_util) != 13:
            print("CNP introdus gresit. Mai incercati.")
            cod_numeric_util = input("Cnp-ul dvs. este : ")
    if S(cod_numeric_util) is True and LL(cod_numeric_util) is True:
        return 'E valid'
    return 'Nu e valid'

print(CNP())