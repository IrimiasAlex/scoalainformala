
cnp = []


def S(cnp):
    gen = int(cnp[0])
    if gen in [1, 2, 3, 4, 5, 6]:
        return True
    print('Ai gresit genul')
    return False


def LL(cnp):
    if int(cnp[3:5]) in range(1, 13):
        return True
    print('Ai gresit luna')
    return False


def ZZ(cnp):
    if int(cnp[5:7]) in range(1, 32):
        return True
    print('Ai gresit ziua')
    return False


def JJ(cnp):
    judet = list(range(1, 47)) + list(range(51, 53))
    if int(cnp[7:9]) in judet:
        return True
    print("Ai gresit Judetul")
    return False


def NNN(cnp):
    if int(cnp[9:12]) in range(1, 1000):
        return True
    print("Ai gresit NNN")
    return False

def C(cnp):
    cifra_de_control = int(cnp[-1])
    referinta = '279146358279'
    rezultat = 0
    for i, v in enumerate(referinta):
        rezultat += int(v) * int(cnp[i])
        rest = rezultat % 11
        if rest == 10:
            rest = 1
        else:
            rest = rest
        if cifra_de_control == rest:
            return True


def CNP():
    global cod_numeric_util
    cod_numeric_util = input("Introduceti-va CNP-ul dvs: ")
    while len(cod_numeric_util) != 13:
            print("CNP introdus gresit. Mai incercati.")
            cod_numeric_util = input("Cnp-ul dvs. este : ")
    if S(cod_numeric_util) and LL(cod_numeric_util) and ZZ(cod_numeric_util) and JJ(cod_numeric_util) and NNN(cod_numeric_util) and C(cod_numeric_util) :
        return 'E valid'
    return 'Nu e valid'

print(CNP())
