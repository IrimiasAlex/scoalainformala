#Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care reprezintă numere întregi sau reale.

#your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3).
def your_function(*args, **kwargs):
    return sum(args)

calcul = your_function(1, 5, -3, a= 'abc', b= [12, 56, 'cad'])
print(calcul)

#your_function() va returna 0.
def your_function2(*args):
    return sum(args)

calcul = your_function2()
print(calcul)

#your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4).
def your_function3 (*args, **kwargs ):
    return sum(args)

calcul = your_function3 (2, 4,  a= 'abc', param_1=2)
print(calcul)


#Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg, altfel returnează valoarea 0.
def este_int(n):
    try:
        int(n)
        print("Numarul", n , "este intreg")
    except ValueError:
        print(0)
este_int(4)