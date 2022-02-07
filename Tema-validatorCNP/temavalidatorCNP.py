import random
cod_numeric = []

def S():
    gen = str(input('Sunteti de sex masculin sau feminin? ')).lower()
    while gen not in ['masculin', 'feminin']:
        print('Ati tastat gresit')
        gen = str(input('Sunteti de sex masculin sau feminin? ')).lower()
    if gen == 'masculin':
        cod_numeric.insert(0, str(1))
    elif gen == 'feminin':
        cod_numeric.insert(0, str(2))
S()


def AA():
    an_nastere = input('Anul dumneavoastra de nastere este: ')  # aici nu am stiut sa gandesc un while prin care ma intoarce la input in cazul unei tastari gresite.
    if an_nastere:
        an_nastere = an_nastere[2:]
        cod_numeric.insert(1, str(an_nastere))

AA()


def LL():
    luna_nasterii = {"ianuarie": "01", 'februarie': "02", 'martie': "03", 'aprilie': "04", 'mai': "05", 'iunie': "06",
                     'iulie': "07", 'august': "08", 'septembrie': "09", 'octombrie': "10", 'noiembrie': "11",
                     'decembrie': "12"}
    luna = input("Luna in care v-ati nascut este: ").lower()
    while luna not in luna_nasterii:
        print('Ati tastat gresit')
        luna = input("Luna in care v-ati nascut este: ").lower()
    if luna in luna_nasterii:
        luna = luna_nasterii.get(luna)
        cod_numeric.insert(2, luna)
LL()


def ZZ():
    ziua_nasterii = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
                     '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    ziua = input("Ziua lunii in care v-ati nascut este: ")
    while ziua not in ziua_nasterii:
        print('Ati tastat gresit- ex. ziua 9 este 09')
        ziua = input("Ziua lunii in care v-ati nascut este: ").lower()
    if ziua in ziua_nasterii:
        cod_numeric.insert(3, ziua)
ZZ()


def JJ():
    cod_judet = {'alba': "01", "arad": "02", "arges": "03", "bacau": "04", "bihor": "05", "bistrita-Nasaud": "06",
                 "botosani": "07", "brasov": "08", "braila": "09", "buzau": "10", "caras-severin": "11", "cluj": "12",
                 "constanta": "13", "covasna": "14", "dambovita": "15", "dolj": "16", "galati": "17", "gorj": "18",
                 "harghita": "19", "hunedoara": "20", "ialomita": "21", "iasi": "22", "ilfov": "23", "maramures": "24",
                 "mehedinti": "25", "mures": "26", "neamt": "27", "olt": "28", "prahova": "29", "satu Mare": "30",
                 "salaj": "31", "sibiu": "32", "suceava": "33", "teleorman": "34", "timis": "35", "tulcea": "36",
                 "vaslui": "37", "valcea": "38", "vrancea": "39", "bucuresti": "40", "bucuresti s.1": "41",
                 "bucuresti s.2": "42", "bucuresti s.3": "43", "bucuresti s.4": "44", "bucuresti s.5": "45",
                 "bucuresti s.6": "46", "calarasi": "51", "giurgiu": "52"}
    judet = input("Scrieti aici judetul in care v-ati nascut: ").lower()
    while judet not in cod_judet:
        print("Ati tastat gresit")
        judet = input("Scrieti aici judetul in care v-ati nascut: ").lower()
    if judet in cod_judet:
        judet = cod_judet.get(judet)
        cod_numeric.insert(4, judet)
JJ()


def NNN():
    numar_random = random.randint(1, 999)    # aici nu am facut impartirea numerelor pe judete. Pentru Alba - numerele de la 001 - 019, la Arad 020 - 039 etc
    numar_random = f'{numar_random:03}'
    cod_numeric.insert(5, numar_random)
NNN()


def C():
    codul_dvs = input("Introduceti-va  primele 12 cifre ale CNP-ul dvs separate prin spatii :")
    lista_utilizator = codul_dvs.split()
    while len(lista_utilizator) != 12:
        print("Ati tastat gresit.")
        codul_dvs = input("Introduceti-va  primele 12 cifre ale CNP-ul dvs separate prin spatii: ")
        lista_utilizator = codul_dvs.split()
    for i in range(len(lista_utilizator)):
        lista_utilizator[i] = int(lista_utilizator[i])
    noua_lista = int(
        2 * lista_utilizator[0] + 7 * lista_utilizator[1] + 9 * lista_utilizator[2] + 1 * lista_utilizator[3] +
        4 * lista_utilizator[4] + 6 * lista_utilizator[5] + 3 * lista_utilizator[6] + 5 * lista_utilizator[7] +
        8 * lista_utilizator[8] + 2 * lista_utilizator[9] + 7 * lista_utilizator[10] + 9 * lista_utilizator[11]) % 11
    print(f'Cifra dvs. de control este: {noua_lista}')  #---> aici imi afiseaza cfra de control ( ultima din CNP)
    cod_numeric.insert(6, str(noua_lista))
C()

def CNP():
    mesaj = input("Introduceti-va CNP-ul dvs separat de spatii: ")
    cod_numeric_util = mesaj.split()
    while len(cod_numeric_util) != 13:
            print("CNP introdus gresit. Mai incercati.")
            mesaj = input("Cnp-ul dvs. este : ")
            cod_numeric_util = mesaj.split()
    if cod_numeric[0] == cod_numeric_util[0] and cod_numeric[1] == cod_numeric_util[1] + cod_numeric_util[2] and \
            cod_numeric[2] == cod_numeric_util[3] + cod_numeric_util[4] and cod_numeric[3] == cod_numeric_util[5] + \
            cod_numeric_util[6] and cod_numeric[4] == cod_numeric_util[7] + cod_numeric_util[8] and cod_numeric[6] == \
            cod_numeric_util[12]:
        print('CNP Valid')
    else:
        print('CNP invalid')

CNP()
print('Cnp-ul dvs este: ', ''.join(map(str,cod_numeric))) # afiseaza CNP-ul, in afara de NNN care sunt cele 3 numere random