# my_lambda = lambda x, y: x + y
# #denumire_functie = lambda param1, param2: corp_functie
# my_sum = my_lambda(2, 3)
# print(my_sum)
 # putem scrie lambda ca si o functie---deci teoretic am scris "my_lambda = lambda x, y: x+ y" in loc de "def my_lambda(x, y): return x+y"
#
# def my_lambda(x, y):
#     return x + y

# diferenta = lambda x, y, z: z - y
# dif = diferenta(4, 3, 5)
# print(dif)

players = [
    {
        "first_name": "Ion",
        "last_name": 'Gheorghe',
        "varsta": 12
    },
    {
        "first_name": "Andreea",
        "last_name": "Popa",
        "varsta": 35
    },
    {
        "first_name": "Isabela",
        "last_name": "Enache",
        "varsta": 25
    }
]

jucatori_sortati = sorted(players, key=lambda jucator: jucator["last_name"])
print(jucatori_sortati)