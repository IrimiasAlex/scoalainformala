if __name__ == 'main':
    print('Functionalitatea principala')

my_var = 5


def my_function():
    print('apeleaza functia')
    return f"Sunt o functie din {__name__}"


if __name__ == '__main__':
    print('Functionalitate principala')
    my_function()


def my_sum(a, b):
    return a + b


print(my_sum(1, 2))

my_list = [1, 2, 3]

if __name__ == '__main__':
    print("lista", my_list)
