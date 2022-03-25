#PROBLEMA 1
def vocale():

    count = 0
    vocale = ('aeiou')
    sir = str(input('Introdu numarul de caractere: '))
    while len(sir) <= 10:
        for i in sir:
            if i in vocale:
                count += 1
        print(f'Ai {count} vocale in sir')
        break
    else:
        print('Prea multe caractere')
vocale()

#PROBLEMA 2

def impartire(a, b, c):
    try:
        impartire = a / b / c
        if a == b == c:
            impartire = impartire * 3
            return impartire
    except ZeroDivisionError:
        return 0

print(impartire(a=int(input('Primul numar este: ')), b=int(input('Al 2-lea numar este: ')), c=int(input('Al 3-lea numar este: '))))

#PROBLEMA 3

def sir_de_numere():
    n = [1, 2, 3, 4, 5, 6, 7]
    for i in n:
        if i % 2 == 0:
            n.insert(i, i*2)
            return n
print(sir_de_numere())
#Nu am reusit sa fac un while pentru a nu intra in return n cum gaseste un nr par......