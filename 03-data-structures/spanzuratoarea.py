#Reguli
#daca primul caracter si ultimul se repetau, caracterul trebuia afisat
# -restul erau ascunse
#7 sanse de a ghici cuvantul
#litera_cuvant = input('Alege o litera')
word = 'onomatopee'
lista_cuvant = []
for iterator in word:
    lista_cuvant.append('_')
    if iterator == word[0] or iterator == word[-1]:
        lista_cuvant[-1] = iterator
print(' '.join(lista_cuvant))
numar_de_incercari = 1
lista_litere_incercate = set()
while numar_de_incercari <= 7:
    litera = input('Alege o litera: ')
    if litera.lower() in word.lower():
        for index, valoare in enumerate(word):
            if valoare == litera:
                lista_cuvant[index] = litera
    else:
        if litera.lower() not in list(lista_litere_incercate):
            numar_de_incercari += 1
        lista_litere_incercate.add(litera.lower())
        print(f'Litera nu exista, deja ai incercat urmatoarele litere {",".join(lista_litere_incercate)}')
        print(f'Mai ai {7 - numar_de_incercari} incercari')
    if 9 - int(numar_de_incercari) == 0:
        print(f'Ai pierdut! Cuvantul era {word}')
    elif ''.join(lista_cuvant) == word:
        print('Ai castigat')
        break
    else:
        print(' '.join(lista_cuvant))

