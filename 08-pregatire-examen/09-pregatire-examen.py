# def string_initial(*args):
#     text = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced.".split(' ')
#     text[1] = 'Conquistador'
#     text[4] = 'King'
#     text[8] = 'Palace'
#     return ' '.join(text)
# print(string_initial())

# lista_nume = ['Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria', 'Claudiu']

#a.Sortati lista dupa nume.
# lista_nume.sort()
# print(str(lista_nume))
#b.Determinati numarul de aparitii al fiecarui nume

# dictionar_nume = {}
# def numar_aparitii(*args):
#     for i in lista_nume:
#         dictionar_nume[i] = lista_nume.count(i)
#     return dictionar_nume
# print(numar_aparitii())


#c.Listati numele care apare de cele mai multe ori in lista initiala.

# def nume_maxim():
#     global max_value
#     for i in lista_nume:
#         dictionar_nume[i] = lista_nume.count(i)
#         all_values = dictionar_nume.values()
#         max_value = max(all_values)
#     return max_value
# print(nume_maxim())
#
#
# def max_occurrences(nums):
#     max_val = 0
#     result = lista_nume[0]
#     for i in lista_nume:
#         occu = nums.count(i)
#         if occu > max_val:
#             max_val = occu
#             result = i
#     return result
# print(f'{max_occurrences(lista_nume)} de {} ori')


# Sa se verifice daca doua stringuri sunt anagrame
# def verificare_anagrama(intrebare_1, intrebare_2):
#     if sorted(intrebare_1) == sorted(intrebare_2):
#         print('Sunt anagrame')
#     else:
#         print('Nu sunt anagrame')
# verificare_anagrama(intrebare_1 = str(input('Primul cuvant este: ')), intrebare_2 = str(input('Al 2-lea cuvant este: ')))


#  Sa se elimine toate duplicatele dintr-o lista
# def verificare():
#     lista = []
#     intrebare = input('Ce elemente vrei sa pui?\n')
#     lista.extend(intrebare.split())
#     print(f'Elementele listei tale sunt : {lista}')
#
#     noua_lista = []
#     for i in lista:
#         if i not in noua_lista:
#             noua_lista.append(i)
#     print(f'Elementele noii liste sunt : {noua_lista}')
# verificare()



