class MyFirstClass:  # tot timpul incepe cu litera mare #punem paranteze cand are mosteniri
    pass


my_first_object = MyFirstClass()  # primul nostru obiect este o instanta intr-o clasa


class Caine:  # definire clasa
    numar_picioare = 4  # ATRIBUT a clasei "caine" - declarat la nivel de clasa

    def __init__(self, name, age=3):  # constructor ! are rolul de a crea date
        # diferite # name si age - proprietati ale obiectului: le putem schimba oricand
        self.nume = name
        self.varsta = age

    def __str__(self):
        return f'{self.nume} - {self.varsta}'  # putem apela functia 'nume' DOAR daca am declarat-o de tipul SELF.NUME

    def change_name(self, name):
        self.nume = name


print(Caine.numar_picioare)  # doar asa putem apela functia din exteriorul unei clase
cainele_meu = Caine('Rex')  # construim OBIECT
print(cainele_meu.nume)
print(cainele_meu.change_name('Ben'))
print(cainele_meu.varsta)


class Calculator:

    def __init__(self, op1, op2, operation):
        self.operator1 = op1
        self.operator2 = op2
        self.operatie = operation

    def adunare(self):
        return self.operator1 + self.operator2

    def scadere(self):
        return self.operator1 - self.operator2

    def __str__(self):
        if self.operatie == '+':
            return f'{self.adunare()}'  # aici am folosit fstring pentru ca rezultatul trebuie sa fie STRING si eu INPUT !!!!
        elif self.operatie == '-':
            return f'{self.scadere()}'


obiect1 = Calculator(1, 2, '+')
obiect2 = Calculator(1, 2, '-')
print(obiect1, obiect2)
