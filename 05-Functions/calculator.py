# 2 variabile
# 1 operator
# 1 rezultat

def suma(a: int, b: int) -> int:
    return a + b

def diferenta(a: int, b: int) -> int:
    return a - b

def inmultire(a: int, b: int) -> int:
    return a * b

def impartire(a: int, b: int) -> float:
    if b == 0:
        while b == 0:
            b = int(input("Aloca o alta valoare pentru b: "))
    return a / b

def operator():
    op = input("Alege operatorul: ")
    if op not in ['*', '/', '+', '-']:
        while op not in ['*', '/', '+', '-']:
            op =  input("Alege operatorul")
    return op

def conversie(mesaj_input: str):
    nr1 = input(f"{mesaj_input}")
    while nr1.isdigit() is False:
        nr1 = input(f"{mesaj_input} ")
    return int(nr1)

    nr2 = input(f"{mesaj_input}")
    while nr2.isdigit() is False:
        nr2 = input(f"{mesaj_input} ")
    nr2 = int(nr2)



def calculator():
    # nr1 = input(f"{mesaj_input}")
    # while nr1.isdigit() is False:
    #     nr1 = input(f"{mesaj_input} ")
    # nr1 = int(nr1)
    nr1 = conversie("Primul numar: ")
    nr2 = conversie("Al 2-lea numar: ")
    # nr2 = int(input("Al 2-lea numar:"))
    # while nr2.isdigit() is False:
    #     nr2 = input("Al doilea numar: ")
    # nr2 = int(nr2)
    op = operator()
    if op == '+':
        rezultat = suma(nr1, nr2)
    elif op == '-':
        rezultat = diferenta(nr1, nr2)
    elif op == '*':
        rezultat = inmultire(nr1, nr2)
    else:
        rezultat = impartire(nr1, nr2)
    return rezultat
print(calculator())

