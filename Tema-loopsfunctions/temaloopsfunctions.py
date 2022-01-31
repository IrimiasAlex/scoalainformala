# EXERCITIUL 1 Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care reprezintă
# numere întregi sau reale.

#your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3).

def your_function(*args, **kwargs):
    print (sum(args))

your_function(1, 5, -3, a= 'abc', b= [12, 56, 'cad'])


# your_function() va returna 0

def your_function2( *args ):
    print (sum(args))

your_function2()


# your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4).

def your_function3 (*args, **kwargs):
    print (sum(args))

your_function3 (2, 4,  a= 'abc', param_1=2)


#EXERCITIUL 2: Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
#suma tuturor numerelor de la [0, n]
def my_sum(n):
    if n == 0:
        return 0
    return n + my_sum(n-1)
print(my_sum(9))

#suma numerelor pare de la [0, n]
def my_sum_even(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            total += i
    print("Suma numerelor pare de la 0 la ", n, "este :", total)
my_sum_even(12)

#suma numerelor impare de la [0. n]
def my_sum_odd(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            total += i
    print("Suma numerelor impare de la 0 la ", n, "este :", total)
my_sum_odd(10)

#Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg, altfel returnează
#valoarea 0.

def este_int(n):
    try:
        int(n)
        print("Numarul", n, "este intreg")
    except ValueError:
        print(0)
este_int('abc')

