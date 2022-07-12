# 1. Vehicul   - clasa mare - CLASA PRINCIPALA SAU SUPERCLASA
# 1.1 Vehicul de apa     SUBCLASA
# 1.2 Vehicul de aer
# 1.3 Vehicul de spatiu
# 1.4 Vehicul terestru
# 1.4.1 Vehicul de teren
# 1.4.2 Vehicul de curse
# 1.1 -> 1.4 SUBCLASA
# 1.4.1, 1.4.2 ->

# 2. Animale
# 2.1 Mamifere
# 2.1.1 Animale salbatice
# 2.1.2 Animale domestice
# 2.2 Reptile
# 2 pentru 2.1 si 2.2 este superclasa
# 2.1 si 2.2 pentru 2 sunt subclase
# 2.1.1 si 2.1.2 pentru 2.1 sunt subclase
# 2.1.1 si 2.1.2 pentru 2 sunt  TOT subclase !!!


# Max este un caine mare care doarme toata ziua.
# obiectul -> Max (substantiv)
# clasa -> caine (substantiv)
# proprietatea -> mare (adjectiv)
# activitatea -> doarme toata ziua (verb) -> metoda

# Un Logan verde merge incet.
# obiectul -> Logan
# clasa -> masina
# proprietatea -> verde
# activitatea -> merge incet

# Lenovo-ul gri se poate cumpara la un pret mai mic de pe un magazin online.
# obiectul -> Lenovo
# clasa -> calculator / laptop
# proprietatea -> gri
# activitatea -> se poate cumpara



# Sa se realizeze jocul X&0 intre 2 jucatori in care:
# primul jucator este mereu calculatorul
# exista reguli de joc pentru mutari
# obiectul -> calculatorul/ omul
# clasa -> Jocul
# proprietatea -> primul jucator este mereu calculatorul
# activitatea -> mutarile / calculul de scor al jocului



# class MyFirstClass:
#     pass
#
#
# object = MyFirstClass()

# stack = []
#
# def push(val):
#     stack.append(val)
#     return stack
#
# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val
#
# print(push(3))
# print(push(2))
# print(push(1))
#
# print(pop())
# print(pop())
# print(pop())

# class Stack:
#
#     def __init__(self):
#         self.__stack_list = []       # daca punem 2 x _ inainte-> INCAPSULARE (PRIVATA)
#
#     def push(self, val):
#         self.__stack_list.append(val)
#
#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
#
#     def __str__(self):
#         return f'Elementele sunt {self.__stack_list}'
#
# obiect_stiva = Stack()
# obiect_stiva.push(3)
# print(obiect_stiva)
# obiect_stiva.push(2)
# print(obiect_stiva)
# obiect_stiva.push(1)
# print(obiect_stiva)
# print(obiect_stiva.pop())
# print(obiect_stiva.pop())
# print(obiect_stiva.pop())


# class ClasaExemplu:
#
#     def __init__(self, val = 1):
#         self.first = val
#         self.second = 0
#
#     def set_second(self, val = 2):
#         self.second = val
#
#     def __str__(self):
#         return f'{self.first} {self.second}'
#
# obiect_1 = ClasaExemplu()
# obiect_2 = ClasaExemplu(2)
#
# print(obiect_1)
# print(obiect_2)


# class Caine:
#     numar_picioare = 4
#
#     def __init__(self, name, age=3):
#         self.nume = name
#         self.varsta = age
#         if self.varsta >= 4:
#             self.stare = 'batran'
#         else:
#             self.stare = 'tanar'
#
#     def __str__(self):
#         # return f'{self.nume} - {self.varsta}'
#         return f'{self.stare} - {self.varsta}'
#
#
#     def change_name(self, name):
#         self.nume = name
#
#
# obiect_1 = Caine('Rex', 3)
# print(obiect_1)
# print(obiect_1.__dict__)
# AFISEAZA : {'nume': 'Rex', 'varsta': 4}  ! PUTEM ALOCA UNEI VARIABILE DICTIONARUL RESPECTIV !

# print(obiect_1.numar_picioare)
# print(obiect_1.varsta)
# print(obiect_1.nume)

# validatorul CNP

# class Validator:
#
#     def __init__(self, cnp):
#         self.CNP = cnp
#
#     def lungime(self):
#         if len(self.CNP) != 13:
#             return False
#         return True
#
#     def __str__(self):
#         if self.lungime() is True:
#             return f'Cnp-ul {self.CNP} este valid'
#         return f'Cnp-ul {self.CNP} nu este valid '
#
# obiect_1 = Validator(input("Introdu CNP-ul: "))
# print(obiect_1)
# from collections import Counter
# lista_nume = ['Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria', 'Claudiu']
#a
# lista_nume.sort()
# print(lista_nume)
#b
# counter = lista_nume.count('Irina')
# print(counter)
#c
# cuvinte_de_numarat = (cuvantul for cuvantul in Counter(lista_nume).most_common())
# print(str(most_common))

# class Star:
#
#     def __init__(self, nume, galaxie):   # nume,galaxie-parametrii
#         self.name = nume
#         self.galaxy = galaxie
#
#     def __str__(self):
#         return f'{self.name} este in {self.galaxy}'
#
#
# soare = Star('Soare', 'Calea Lactee')
# print(soare)
# #rezultat : Soare este in Calea Lactee



vehicul
vehiculdeteren
vehiculdetractare

class Vehicul:
    pass

class Vehiculdeteren(Vehicul):
    pass

class Vehiculdetractare(Vehiculdeteren):
    pass

#parinti sunt Vehicul pentru Vehiculdeteren si Vehiculdetractare(indirect)
#parinti sunt Vehiculdeteren pentru Vehiculdetractare
#parintii sunt superclase pentru copii(superclass)
#copiii sunt VehiculTeren si VehiculTractare (indirect) pentru Vehicul
#copilul este Vehiculdetractare pentru Vehiculdeteren
#copiii se numesc subclase

# print("Vehicul Vehiculdeteren Vehiculdetractare")
# for cls1 in [Vehicul, Vehiculdeteren, Vehiculdetractare]:
#     for cls2 in [Vehicul, Vehiculdeteren, Vehiculdetractare]:
#         print(issubclass(cls1, cls2, end = '\t'))
#     print()

# vehicul1 = Vehicul()
# vehicul_teren = Vehiculdeteren()
# vehicul_tractare = Vehiculdetractare()
# print(isinstance(vehicul1, Vehiculdeteren))
#False pentru ca vehicul1 este superclasa si nu mosteneste pe nimeni

#Intrebare de interviu

# class Exemplu:
#     def __init__(self, val):
#         self.value = val
#
# obiect_1 = Exemplu(0)
# obiect_2 = Exemplu(2)
# obiect_3 = obiect_1
# obiect_3.value += 1
#
# print(obiect_1 is obiect_2)
# print(obiect_2 is obiect_3)
 #is verifica daca se pointeaza spre aceleasi obiect si == daca e egala valoarea

# string_1 = 'Maria are mere '
# string_2 = 'Maria are mere mari'
# string_1 += 'mari'
# print(string_1 == string_2, string_1 is string_2)
#DE EXERSAT!!!


# class SuperClass:
#
#     supVar = 1
#     variabila_clasa = 6
#
#     def __init__(self, nume):
#         self.name = nume
#         self.var_1 = 101
#
#     def __str__(self):
#         return f'Numele meu este {self.name}'
#
#
# class Clasa3(SuperClass):
#
#     variabila_clasa = 5
#
#     def __init__(self, nume):
#         super().__init__(self, nume)
#         self.name = nume
#         self.var_2 = 201
#
# class SubClass(Clasa3, SuperClass):
#
#     subVar = 2
#
#     def __init__(self, nume):
#         super().__init__(nume)   # INVOCA CONSTRUCTORUL SUPERCLASEI
#         self.var_3 = 301
#         # self.name = nume
#         # Super.__init__(self, nume)
#
#     # def __str__(self):
#     #     return f'Nume'
#
# obiect = SubClass('Alex')
# # print(obiect)
# # print(obiect.subVar)
# # print(obiect.supVar)
# print(obiect.var_3, obiect.var_2, obiect.var_1)
