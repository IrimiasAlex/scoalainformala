# 1. Problema 1
# Creati o clasa ce va reprezenta un catalog:
# • La initializare trebuie sa oferim doi parametrii de intrare nume si prenume Metoda de
# initializare creaza un atribut numit materii de tip dictionar nepopulat, dar si un atribut numit
# absente initializat la 0.
# • Avem o metoda care afiseaza absente implementat cu __str__
# • Avem o metoda care incrementeaza cu 1 nr. de absente
# • Avem o metoda care sterge un nr. (exclusiv un numar - verifica) de absente dat (pentru
# cazurile in care avem o scutire medical) fara a deveni negativ
# Creati a doua clasa numita Extensie1 care sa mosteneasca prima clasa. Clasa materii sa
# aiba 3 metode:
# - Prima metoda permite adaugarea prin doi parametrii de intrare a unui sir de
# caractere reprezentand materia si o lista reprezentand notele. Acesti parametrii de
# intrare sunt utilizati pentru a adauga o intrare in dictionarul atribut materii al obiectului
# current. Cheia este materia (sirul de caractere) si lista reprezinta value.
# - A doua metoda permite afisarea tuturor materilor unui student.
# - A treia metoda permite afisarea materiilor si media aritmetica a fiecarei liste asociate
# pentru fiecare materie in parte. Verificati daca in lista sunt elemente de tip numar si
# ignorati alte valori.
# Verificari:
# • Creati 1 student numit Ion Roata
# • Modificati argumentul absente sa fie incrementat de 3 ori prin metoda creata
# • Stergeti doua absente prin metoda specificata
# • Creati al doilea student numit George Cerc
# • Modificati argumentul absente sa fie incrementat de 4 ori prin metoda creata
# • Stergeti doua absente prin metoda specificata
# • Afisati absentele fiecarui student
# • Adaugati materia ”Python” impreuna cu o lista formata din 3 numere intre 1-10 pentru
# fiecare student
# • Adaugati materia ”Matematica” la al doilea student numit George Cerc si “Romana” pentru
# studentul numit Ion Roata impreuna cu o lista formata din 3 numere intre 1-10 pentru fiecare
# student
# • Verificati ce materii are fiecare student prin metoda ce permite afisarea tuturor materilor
# unui student.
# • Verificati ce materii si ce note mediate au studentii.
class Catalog:

    def __init__(self, nume, prenume):
        self.name = nume
        self.firstname = prenume
        self.materii = {}
        self.absente = 0

    def incrementare_abs(self, nr_abs):
        self.absente += nr_abs

    def delete_abs(self, nr_abs):
        if self.absente >= nr_abs:
            self.absente -= nr_abs

    def __str__(self):
        return f'Elevul {self.name} {self.firstname} are {self.absente} absente'


class Extensie1(Catalog):

    def __init__(self, nume, prenume):
        super().__init__(nume, prenume)
        self.note_finale = {}

    def metoda_1(self, materie, note):
        self.materii.update({materie: note})

    def metoda_2(self):
        return f"Materiile elevului {self.name} {self.firstname} sunt: {', '.join(list(self.materii.keys()))}"

    def metoda_3(self):
        note_finale = {}
        for i, j in self.materii.items():
            if all(isinstance(x, int) for x in j):
                media = sum(j) / len(j)
                note_finale.update({i: media})
        return f'Notele finale ale studentului {self.name} {self.firstname} sunt: {("%s" % note_finale).replace("{", "").replace("}", "")}'


student = Catalog('Ion', 'Roata')
student.incrementare_abs(3)
student.delete_abs(2)

student1 = Extensie1('Ion', 'Roata')
student1.metoda_1('Python', [4, 5, 6])
student1.metoda_1('Romana', [1, 9, 10])

student2 = Catalog('George', 'Cerc')
student2.incrementare_abs(4)
student2.delete_abs(2)

student3 = Extensie1('George', 'Cerc')
student3.metoda_1('Python', [7, 8, 9])
student3.metoda_1('Matematica', [2, 8, 5])

print(student)
print(student1.metoda_2())
print(student1.metoda_3())

print(student2)
print(student3.metoda_2())
print(student3.metoda_3())

# PROBLEMA-URMATOARE :
# Creati 3 clase ce vor reprezenta un catalog de prajituri.
# • Creati o clasa ce va reprezenta un catalog de prajituri.
# La crearea unui obiect al acestei clase va solicita trei argumente reprezentand nume (sir de
# caractere), preț (integer) si gramaj (integer) cu care va crea trei atribute. Fiecare obiect creat
# va fi adaugat intr-o lista mentinuta de o variabila a clasei.
# Clasa trebuie sa detina o metoda care sa poate afisa toate prăjituri sortand în funcție de
# gramaj afisand gramajul, numele și pretul Clasa trebuie sa detina o metoda care sa poate
# afisa toate prăjituri în funcție de pret afisand gramajul, numele și prețul
# • Creati a doua clasa care mosteneste prima clasa care se va numi tort.
# Aceasta clasa va avea o atribut numit etajat care default sa devina False și alt atribut care
# se numește glazura (sir de caractere) ce este default „ciocolata”. Aceste atribute trebuiesc
# implementate printr-o metoda de setare cu parametrii de intrare. O alta metoda permite
# citirea acestora.
# • Creati a treia clasa care mosteneste prima clasa care se va numi fursec. Aceasta va
# mosteni intocmai prima clasa fara a modifica/ adauga nimic.
# Creati 3 obiecte ale clasei tort si trei obiecte ale clasei fursec.
# Afisati prajiturie dupa gramaj.
# Afisati prajiturie dupa pret.
# Folositi pentru un obiect de tip tort modificarea atributelor etajat in True si glazura in “cacao”,
# apoi pentru acest obiect folositi metoda de afisare a atributelor glazura si etajat.
# De asemenea, folositi metoda de setare/afisare si pentru un alt obiect de tip tort

from operator import itemgetter


class Catalog_prajituri:
    lista = []

    def __init__(self, nume='Chec', pret=14, gramaj=150):
        self.nume = str(nume)
        self.pret = int(pret)
        self.gramaj = int(gramaj)
        self.lista.append([self.nume, self.pret, self.gramaj])

    def afisare_lista(self):
        print(self.lista)

    @staticmethod
    def sortare_gramaj():
        sortata_gramaj = sorted(Catalog_prajituri.lista, key=itemgetter(2))
        return f'Prajiturile sortate dupa gramaj sunt: {sortata_gramaj}'

    @staticmethod
    def sortare_pret():
        sortata_pret = sorted(Catalog_prajituri.lista, key=itemgetter(1))
        return f'Prajiturile sortate dupa pret sunt: {sortata_pret}'


class Tort(Catalog_prajituri):
    def __init__(self, nume, gramaj, pret, etajat=False, glazura='ciocolata'):
        super().__init__(nume, gramaj, pret)
        self.etajat = etajat
        self.glazura = glazura

    def __str__(self):
        return f'Etajarea este {self.etajat}, iar glazura este {self.glazura}'


class Fursec(Catalog_prajituri):
    pass


obiect1 = Catalog_prajituri('Broscuta', 9, 150)
obiect2 = Catalog_prajituri('Cremes', 7, 100)
obiect3 = Catalog_prajituri('Tiramisu', 12, 125)
# Catalog_prajituri.afisare_lista(obiect1 and obiect2 and obiect3)
tort1 = Tort(nume='A', gramaj=112, pret=150, etajat=True, glazura='cacao')
tort2 = Tort(nume='D', gramaj=55, pret=45, etajat=True, glazura='cacao')
tort3 = Tort(nume='B', gramaj=1150, pret=350, etajat=True, glazura='cacao')

fursec = Fursec()

print(Catalog_prajituri.sortare_gramaj())
print(Catalog_prajituri.sortare_pret())
print(Catalog_prajituri.lista)

print(tort1.glazura)
print(tort1.gramaj)
print(tort1.nume)
print(tort1)


# PROBLEMA-URMATOARE:
# Creati 3 clase ce vor reprezenta un catalog auto:
# • Clasa1 • La initializare trebuie sa oferim doi parametrii de intrare marca si tip • Are o
# metoda ce accepta parametrul de intrare culoare. De asemenea o metoda numita
# AfisareCuloare pentru afisarea culorii. Folositi metoda pentru afisare.
# • Clasa2 : • Mosteneste Clasa1 si avem o metoda care adauga argumentul scaune_incalzite
# ca parametru de intrare
# • Clasa3 : • Mosteneste Clasa1 si avem o metoda care adauga argumentul
# Blocuri_Optice_LED ca parametru de intrare

# • Creati un obiect al Clasei 2 (marca = ARO,Tip = M461) si folositi metoda de creare argum
# DA. scaune_incalzite cu valoarea Nu;
# Creati argumentul culoare cu valoarea rosu
# • Creati un obiect al Clasei 3 (marca = Dacia, Tip = 1310) si folositi metoda de creare argum.
# Blocuri_Optice_LED cu valoarea Nu; Creati argumentul culoare cu valoarea negru
# • Afisati pe rand argumentele culoare, Blocuri_Optice_LED, scaune_incalzite marca si tip a
# obiectelor create

class CatalogAuto:
    def __init__(self, marca, tip):
        self.marca = marca
        self.tip = tip

    def schimb_culoare(self, culoare):
        self.culoare = culoare  # self.culoare il putem folosi si in alte metode ( gen str)

    def __str__(self):
        return f'Culoarea este : {self.culoare}'


class ScauneIncalzite(CatalogAuto):

    def __init__(self, scaune_incalzite, marca, tip):
        super(ScauneIncalzite, self).__init__(marca, tip)
        self.scaune_incalzite = scaune_incalzite

    def __str__(self):
        return f'Marca este : {self.marca}, tipul este {self.tip}, scaune incalzite :{self.scaune_incalzite}'


class BlocuriOpticeLED(CatalogAuto):

    def __init__(self, blocuri_optice_led, marca, tip):
        super().__init__(marca, tip)
        self.blocuri_optice_led = blocuri_optice_led

    def __str__(self):
        return f'Marca este : {self.marca}, tipul este: {self.tip}, Blocuri optice: {self.blocuri_optice_led}'


obj = ScauneIncalzite(marca='ARO', tip=461, scaune_incalzite='NU')
print(obj)
obj.schimb_culoare('rosu')
print(obj.culoare)
obj2 = BlocuriOpticeLED(marca='Dacia', tip=1310, blocuri_optice_led='Nu')
print(obj2)
obj2.schimb_culoare('Negru')
print(obj2.culoare)
print(obj2.culoare, obj2.blocuri_optice_led, obj2.marca, obj2.tip)
print(obj.culoare, obj.scaune_incalzite, obj.marca, obj.tip)


# PROBLEMA-URMATOARE
# Creati o clasa care sa calculeze si sa returneze operatia matematica de mai jos pentru
# 4 numere: [a(b+3)/c]*d.
# Clasa trebuie sa aiba 2 metode: prima metoda este metoda speciala init.
# Iar cea dea doua metoda este metoda speciala str.
# Va rog sa aplicati cel putin doua exemple (doua obiecte).
# Metoda init trebuie sa foloseasca parametrii default a=1,b=2,c=3,d=4 si trebuie sa suprime
# orice eroare.
# La aparitia unei erori trebuie sa afiseze textul: <>
# Folositi clasa in trei exemple:
# • cu patru parametrii numerici diferiti de cei default
# • cu 3 parametrii non-numerici
# • cu 2 parametrii numerici

class Calcul:

    def __init__(self, a=1, b=2, c=3, d=4):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def verificare(self):
        self.e = f'Nu sunt cifre'
        if str(self.a).isnumeric() and str(self.b).isnumeric() and str(self.c).isnumeric() and str(self.d).isnumeric():
            self.e = (self.a * (self.b + 3) / self.c) * self.d
        return self.e

    def __str__(self):
        return f'Rezultatul este : {self.verificare()}'


obiect = Calcul()
print(obiect)
obiect4 = Calcul(5, 6, 7, 8)
print(obiect4)
obiect5 = Calcul('x', 'y', 'z', 2)
print(obiect5)
obiect6 = Calcul(9, 2)
print(obiect6)


# PROBLEMA URMATOARE:
# Creati o clasa care se numeste lista_CD_DVD.
# La crearea unui obiect ale acestei clase va solicita doua argumente reprezentand titlu si
# continut cu care va crea doua atribute.
# Fiecare obiect creat va fi adaugat intr-o lista din namespace-ul global Clasa are o
# metoda care cauta si gaseste pe baza textului dat ca argument un obiect, afisiand titlu
# si continutul. Se va folosi lista de obiecte pentru a cauta.
# La afisarea obiectului returnati utilizand metoda __str__ titlul obiectului.
# Aplicati clasa pentru 3 exemple apoi folositi cautarea pe un caz pozitiv si unul
# negativ. Printati cele 3 obiecte.

class Lista_CD_DVD:
    lista = []

    def __init__(self, titlu, continut):
        self.titlu = titlu
        self.continut = continut
        self.lista.append([self.titlu, self.continut])

    @staticmethod
    def cautare(argument):
        msg = 'Obiectul nu a fost gasit'
        for i in Lista_CD_DVD.lista:
            if argument in i[0] or argument in i[1]:
                msg = f'Obiectul cautat este Titlu: {i[0]} , iar Continut: {i[1]}'
        return msg

    def __str__(self):
        return f'Titlul obiectului este: {self.titlu}'


obiect7 = Lista_CD_DVD(titlu='Grand Theft Auto', continut='Game')
obiect8 = Lista_CD_DVD(titlu='Avatar', continut="Film pe care nu l-am vazut")
obiect9 = Lista_CD_DVD(titlu='Bitdefender', continut='Antivirus')
print(obiect9)
print(Lista_CD_DVD.cautare('virus'))
print(Lista_CD_DVD.cautare('NFS'))

# PROBLEMA URMATOARE
# Creati un program ce are o clasa numita util. Clasa are o variabila a clasei de tip lista
# populata automat in constructor(__init__) cu obiectul.
# Creati a doua clasa numita izatori care primeste in constructor doua argumente numite
# user si passw, formand cu ajutorul acestora doua atribute cu acelasi nume.
# Creati a treia clasa numita utilizatori care sa mosteneasca clasele util și izatori fără a
# pierde din functionalitatea claselor mostenite.
# De asemenea, aceasta clasa are o metoda privata numita parole care sa returneze un
# set cu toate parolele și o metoda privata numita useri care sa returneze un set cu toți
# userii. Se va folosi variabila clasei de tip lista care are toate obiectele pentru căutare.
# Interpretorul trebuie sa ridice o eroare setata de voi în cazul în care este apelat
# obiectul prin len(). Setati 3 obiecte și testați functionalitatea.

# class Util:
#     lista_obj = []
#     def __init__(self):
#         self.lista_obj.append(self)
#
#     def __str__(self):
#         return f"{self.lista_obj}"
#
# class Izatori():
#     def __init__(self, user, passw):
#         self.user = user
#         self.passw = passw
#
# class Utilizatori(Util, Izatori):
#     set_parole = set()
#     set_useri = set()
#
#     def __init__(self, user, passw):
#         Util.__init__(self)
#         Izatori.__init__(self, user, passw)
#
#     @staticmethod
#     def parole():
#         for i in Utilizatori.lista_obj:
#             Utilizatori.set_parole.add(i.passw)
#         return f"Lista de parole este: {Utilizatori.set_parole}"
#
# om_bun = Utilizatori("pisici", "catei")
# om_bun2 = Utilizatori("pisicile", "cateii")
# om_bun4 = Utilizatori("dinozauri", "balauri")
#
# print(Utilizatori.lista_obj)
# print(om_bun.user)
#
# print(Utilizatori.__dict__)

# print(Util.__parole())
# REZOLVARE-ALEXANDRA
