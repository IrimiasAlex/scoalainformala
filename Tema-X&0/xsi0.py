tabla = ['_', '_', '_',
         '_', '_', '_',
         '_', '_', '_']
jucator = 'X'
calculator = '0'
castigator = None
continuam_jocul = True


def afisare_tabla(tabla):
    # return f'{tabla[0]}   {tabla[1]}   {tabla[2]}\n\n{tabla[3]}   {tabla[4]}   {tabla[5]}\n\n{tabla[6]}   {tabla[7]}   {tabla[8]}'
    print(tabla[0] + "   " + tabla[1] + "   " + tabla[2])
    print("         ")
    print(tabla[3] + "   " + tabla[4] + "   " + tabla[5])
    print("         ")
    print(tabla[6] + "   " + tabla[7] + "   " + tabla[8])
    # return True


def alegere_jucator(tabla):
    alegere = int(input("Alege unde vrei sa pui X-ul: "))
    if tabla[alegere - 1] == '_':
        tabla[alegere - 1] = jucator
    else:
        print("Este deja ocupata :(, alege alta: ")


# TODO aici mai am de adaugat un while.

def castig_linie(tabla):
    global castigator
    if tabla[0] == tabla[1] == tabla[2] and tabla[0] != "_":
        castigator = tabla[0]
        return True
    elif tabla[3] == tabla[4] == tabla[5] and tabla[3] != "_":
        castigator = tabla[3]
        return True
    elif tabla[6] == tabla[7] == tabla[8] and tabla[6] != "_":
        castigator = tabla[6]
        return True


def castig_coloana(tabla):
    global castigator
    if tabla[0] == tabla[3] == tabla[6] and tabla[0] != "_":
        castigator = tabla[0]
        return True
    elif tabla[1] == tabla[4] == tabla[7] and tabla[1] != "_":
        castigator = tabla[1]
        return True
    elif tabla[2] == tabla[5] == tabla[8] and tabla[2] != "_":
        castigator = tabla[3]
        return True


def castig_diagonala(tabla):
    global castigator
    if tabla[0] == tabla[4] == tabla[8] and tabla[0] != "_":
        castigator = tabla[0]
        return True
    elif tabla[2] == tabla[4] == tabla[6] and tabla[4] != "_":
        castigator = tabla[2]
        return True


def ai_castigat(tabla):
    global continuam_jocul
    if castig_linie(tabla):
        afisare_tabla(tabla)
        print(f"Castigatorul este: {castigator}!")
        continuam_jocul = False

    elif castig_coloana(tabla):
        afisare_tabla(tabla)
        print(f"Castigatorul este: {castigator}!")
        continuam_jocul = False

    elif castig_diagonala(tabla):
        afisare_tabla(tabla)
        print(f"Castigatorul este: {castigator}!")
        continuam_jocul = False


def egalitate(tabla):
    global continuam_jocul
    if "_" not in tabla:
        afisare_tabla(tabla)
        print("Egalitate!")
        continuam_jocul = False


def schimba_jucatorul():
    global jucator
    if jucator == "X":
        jucator = "O"
    else:
        jucator = "X"


def calculator(tabla):
    while jucator == "O":
        if tabla[4] == '_':
            tabla[4] = '0'
            schimba_jucatorul()
        elif tabla[0] == '_':
            tabla[0] = '0'
            schimba_jucatorul()
        elif tabla[2] == '_':
            tabla[2] = '0'
            schimba_jucatorul()
        elif tabla[6] == '_':
            tabla[6] = '0'
            schimba_jucatorul()
        elif tabla[8] == '_':
            tabla[8] = '0'
            schimba_jucatorul()
        elif tabla[1] == '_':
            tabla[1] = '0'
            schimba_jucatorul()
        elif tabla[3] == '_':
            tabla[3] = '0'
            schimba_jucatorul()
        elif tabla[5] == '_':
            tabla[5] = '0'
            schimba_jucatorul()
        elif tabla[7] == '_':
            tabla[7] = '0'
            schimba_jucatorul()


while continuam_jocul:
    print(afisare_tabla(tabla))
    alegere_jucator(tabla)
    ai_castigat(tabla)
    egalitate(tabla)
    schimba_jucatorul()
    calculator(tabla)
    ai_castigat(tabla)
    egalitate(tabla)
