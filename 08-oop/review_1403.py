class ClasaMea:

    gamma = 0             #variabila de clasa

    def __init__(self):   #constructor
        self.alpha = 1    #variabila de instance
        self.__delta = 3  #variabila de instanta privata

obj = ClasaMea()          #instantiere a clasei ClasaMea
obj.beta = 2              #variabila de instanta si poate exista doar in interiorul obj
print(obj.__dict__)       #
print(obj.alpha)
print(ClasaMea.gamma)
print(obj._ClasaMea__delta)

#rezultate:
# {'alpha': 1, '_ClasaMea__delta': 3, 'beta': 2}
# 1
# 0
# 3
