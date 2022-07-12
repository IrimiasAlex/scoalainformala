print("Numele meu este Alexandru")
print(1, type(1))  # tipul int
print(1, type(1.1))  # tipul float
print(1j, type(1j))  # tipul complex
print(int(1.1))
print(float(1))
print(complex(1))
print(1 * 0)
print(5 / 2)  # impartire exacta
print(5 // 2)  # catul
print(5 % 2)  # restul
print(5 ** 2)  # ridicare la putere
print(5 == 2)  # operator de egalitate  --> returneaza un BOOLEAN( True sau False)
print(5 != 2)  # operator de diferentiere  --> returneaza un BOOLEAN( True sau False)
print(5 < 2)
print(5 >= 2)
print(5 > 2 or 3 > 4)  # --->Se opreste la TRUE
print(not (5 > 2 and 3 > 1))
print(7 is 7)  # --> True
print(7 is not 7)  # --> False
# variabile-
my_var, my_var_1 = 0, 1  # --> atribuire mai multe variabile
print(my_var, my_var_1)
my_var = 0  # --> incrementare prin adunare
my_var += 2
print(my_var)
my_var = 3  # --> asignare prin inmultire
my_var *= 2
print(my_var)
variabila = '''Ana are mere'''
print(variabila)

nume = "Irimias"
prenume = "Alexandru"
prezentare = "Numele meu este {} si prenumele este {}".format(nume, prenume)
print(prezentare)

nume = "Irimias"
prenume = "Alexandru"
prezentare = "Numele meu este {1} si prenumele este {0}".format(nume, prenume) #- -->Inverseaza
#"Numele meu este Alexandru si prenumele Irimias
print(prezentare)

prezentare = f"Numele meu este{nume} si prenumele meu este{prenume}"

nume = "Irimias"
prenume = "Alexandru"
varsta = 19
inaltime = 20.1
calcul = nume + str(varsta)
calcul1 = nume + prenume
print(calcul)
print(calcul1)
