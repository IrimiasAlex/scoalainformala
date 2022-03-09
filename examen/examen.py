#1. Scrie un program care sa calculeze suma dintre trei numere. Daca valorilesunt egale, returnati de trei ori suma acestora.(1 punct)

def suma(a, b, c):
    sum = a + b + c
    if a == b == c:
        sum = sum * 3
    return sum

print(suma(a=int(input('Primul numar este: ')), b=int(input('Al 2-lea numar este: ')), c=int(input('Al 3-lea numar este: '))))


#2. Scrie un program care sa elimine si sa printeze numerele din 3 in 3 pana cand lista devine goala. (1 punct) Lista =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

Lista =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
def stergere():
    while len(Lista) > 0:
        print(Lista)
        Lista.remove(1)
        Lista.remove(4)
        Lista.remove(7)
        Lista.remove(10)
        Lista.remove(13)
        print(Lista)
        Lista.remove(2)
        Lista.remove(6)
        Lista.remove(11)
        print(Lista)
        Lista.remove(3)
        Lista.remove(9)
        print(Lista)
        Lista.remove(5)
        print(Lista)
        Lista.remove(8)
        print(Lista)
        Lista.remove(12)
        print(Lista)
stergere()


#3.Scrie un program care sa afiseze toate combinarile de 2 litere dintre valorile dictionarului de mai jos: dictionar = {"1": "abc","2": "s","3": "o","4": "n","5": "lm","6": "jk","7": "gi","8": "def","9": "abc"}
dictionar = {"1": "abc","2": "s","3": "o","4": "n","5": "lm","6": "jk","7": "gi","8": "def","9": "abc"}

# a = dictionar.values()
# b = dictionar.values()
# for i in a:
#     for j in b:
#         if len(i+j) == 2:
#             print(i+j)
def combinatii_litere(litere):
    combinatii = ['']
    for a in litere:
        lista_rezultat = []
        for i in combinatii:
            for j in dictionar[a]:
                lista_rezultat.append(i+j)
        combinatii = lista_rezultat
    return combinatii
k='19'
print(combinatii_litere(k))

