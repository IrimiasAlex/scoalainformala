# def adunare(n):
#     return n + n


lista_numere = [1, 2, 3, 4, 9]
lista_numere_2 = [5, 6, 7, 8]
# rezultat = map(adunare, lista_numere)   # aplica functia de adunare in toata lista!!!
# print(list(rezultat))    # REZULTATUL LUI MAP ESTE O LISTA DE ACEEA TREBUIE "LIST"

rezultat = map(lambda n, m: n + m, lista_numere, lista_numere_2)
# print(list(rezultat))


def adunare(lista_numere, lista_numere_2):
    lista_adunare = []
    for i in range(0, min([len(lista_numere), len(lista_numere_2)])):    #-ATENTIE AM PUS DE LA 0 - INDEX
        lista_adunare.append(lista_numere[i] + lista_numere_2[i])

        #CE ESTE MAI JOS PUTEM SCRIE MAI USOR CA SI SUS

    # for i, v in enumerate(lista_numere):
    #     for j, w in enumerate(lista_numere_2):
            # suma = lista_numere[i] + lista_numere_2[j]
            # suma = v + w
            # if i == j:
            #     lista_adunare.append(suma)
    return lista_adunare


print(adunare(lista_numere, lista_numere_2))