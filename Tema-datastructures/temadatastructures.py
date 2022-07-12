my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
my_list.sort()  #afișează lista inițială ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
print(my_list)

my_list.reverse()  #afișează lista inițială ordonată descendent (lista inițială trebuie păstrată în aceeași formă)
print(my_list)

my_sliced_even_list = my_list[::2]   #afișează o listă ce conține numerele pare din lista ordonată (folosind slice)
print(my_sliced_even_list)

my_sliced_odd_list = my_list[1::2]     #afișează o listă ce conține numerele impare din lista ordonată (folosind slice)
print(my_sliced_odd_list)

multiples_3 = my_list[1::3]       #afisează o listă ce conține numerele ce sunt multipli ai numărului 3 (folosind slice).
print(multiples_3)