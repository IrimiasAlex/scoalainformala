#PROIECT GRUPA
# import random
#
# def joc():
#
#     msg = " "
#
#     jucator = input("Your name is: ")
#
#     variante = ["foarfeca", "piatra", "hartie"]
#
#     alegere = input("Alege o varianta: ")
#
#     optiuni_calculator = random.choice(variante)
#
#     if alegere=="foarfeca" and optiuni_calculator=="foarfeca" or alegere=="piatra" and optiuni_calculator=="piatra" or alegere=="hartie" and optiuni_calculator=="hartie":
#         msg = "Remiza"
#
#     elif alegere=="foarfeca" and optiuni_calculator=="piatra":
#         msg="Piatra bate foarfeca, ai pierdut!"
#
#     elif alegere=="foarfeca" and optiuni_calculator=="hartie":
#         msg = f'Foarfeca taie hartia, ai castigat {jucator}!'
#
#     elif alegere=="piatra" and optiuni_calculator=="hartie":
#         msg = f'Hartia impacheteaza piatra, ai pierdut {jucator}!'
#
#     elif alegere=="hartie" and optiuni_calculator=="foarfeca":
#         msg = f'Foarfeca taie hartia, ai pierdut {jucator}!'
#
#     elif alegere=="hartie" and optiuni_calculator=="piatra":
#         msg = f'Hartia impacheteaza piatra, ai castigat {jucator}!'
#
#     elif alegere=="piatra" and optiuni_calculator=="foarfeca":
#         msg = f'Piatra bate foarfeca, ai pierdut, {jucator}!'
#
#     return optiuni_calculator,msg
#
# optiuni, mesaj = joc()
# print(f'Optiunea calculatorului a fost {optiuni}\n', mesaj)
#
# joc_nou = input("Vrei sa joci din nou? y/n")
#
# while joc_nou == "y":
#     optiuni, mesaj = joc()
#     print(f'Optiunea calculatorului a fost {optiuni}\n', mesaj)
#
#     joc_nou = input("Vrei sa joci din nou? y/n")



import random

piatra = 'piatra'
foarfeca = 'foarfeca'
hartie = 'hartie'
jucator = input("Numele tau este: ")
variante = [foarfeca, piatra, hartie]

varianta_jucator = int(input(f"Salut, {jucator}! Ce alegi? 0- foarfeca, 1- piatra, 2- hartie "))
while varianta_jucator in range(0,3):
    print('Alegerea ta este: ',variante[varianta_jucator])
    varianta_calculator = random.randint(0,2)
    print(f'Alegerea calculatorului: ', variante[varianta_calculator])

    if varianta_jucator < 0 and varianta_jucator > 2:
        print("Numar invalid")
    elif varianta_jucator == 0 and varianta_calculator == 1 or varianta_jucator == 1 and varianta_calculator == 2 or varianta_jucator == 2 and varianta_calculator == 0:
        print("Ai pierdut")
    elif varianta_jucator == varianta_calculator:
        print("Este egalitate")
    else:
        print("Ai castigat")
    break
else:
    print('Ai tastat gresit')
    jucator = input('Numele tau este: ')

