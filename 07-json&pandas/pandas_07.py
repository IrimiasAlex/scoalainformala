import pandas as pd


#pandas- librarie pe care o putem folosi pentru cititrea si parsarea de date+ statistica

# dictionar_date = {
#     "masini": ['Dacia', 'Volvo', 'Renault'],
#     "culoare": ['Rosu', 'Alb', 'Verde']
# }
#
# variabila = pd.DataFrame(dictionar_date)
# print(variabila)


# 0    Dacia    Rosu
# 1    Volvo     Alb
# 2  Renault   Verde



# masini = ['Dacia', 'Volvo', 'Renault']
# variabila = pd.Series(masini, index = ['x', 'y', 'z'])
# #din Series ne putem extrage mai usor datele
# print(variabila)

# x      Dacia
# y      Volvo
# z    Renault

# masini = {'x': 'Dacia', 'y': 'Volvo', 'z': 'Renault'}
# variabila = pd.Series(masini)
# print(variabila)


# x      Dacia
# y      Volvo
# z    Renault




# masini = {'x': 'Dacia', 'y': 'Volvo', 'z': 'Renault'}
# variabila = pd.Series(masini, index = ['y', 'z'])
# print(variabila)


# y      Volvo
# z    Renault

# SERIES - COLOANA , DATAFRAME - INTREG TABELUL !!!!!!!!!


# dictionar_date = {
#      "masini": ['Dacia', 'Volvo', 'Renault'],
#      "culoare": ['Rosu', 'Alb', 'Verde']
# }

# variabila = pd.DataFrame(dictionar_date)
# print(variabila.loc[0])

# masini     Dacia
# culoare     Rosu


# dictionar_date = {
#      "masini": ['Dacia', 'Volvo', 'Renault'],
#      "culoare": ['Rosu', 'Alb', 'Verde']
# }
# variabila = pd.DataFrame(dictionar_date)
# print(variabila.loc[[0, 1]])


#   masini culoare
# 0  Dacia    Rosu
# 1  Volvo     Alb



#
# dictionar_date = {
#      "masini": ['Dacia', 'Volvo', 'Renault'],
#      "culoare": ['Rosu', 'Alb', 'Verde']
# }
# variabila = pd.DataFrame(dictionar_date, index = ['producator1', 'producator2', 'producator3'])
# print(variabila)



#               masini culoare
# producator1    Dacia    Rosu
# producator2    Volvo     Alb
# producator3  Renault   Verde




# dictionar_date = {
#      "masini": ['Dacia', 'Volvo', 'Renault'],
#      "culoare": ['Rosu', 'Alb', 'Verde']
# }
# variabila = pd.DataFrame(dictionar_date, index = ['producator1', 'producator2', 'producator3'])
# print(variabila.loc[['producator1', 'producator2']])
#
#
#             masini culoare
# producator1  Dacia    Rosu
# producator2  Volvo     Alb


# data = {
#   "producator1" : {
#     "masini": "Dacia",
#     "culoare": "rosu"
#   },
#   "producator2" : {
#     "masini": "Volvo",
#     "culoare": "alb"
#   },
#   "producator3" : {
#     "masini": "Renault",
#     "culoare": "verde"
#   }
# }
#
# variabila1 = pd.read_json('data.json')
# print(variabila1)

#         producator1 producator2 producator3
# masini        Dacia       Volvo     Renault
# culoare        rosu         alb       verde


# data = {
#   "producator1" : {
#     "masini": "Dacia",
#     "culoare": "rosu"
#   },
#   "producator2" : {
#     "masini": "Volvo",
#     "culoare": "alb"
#   },
#   "producator3" : {
#     "masini": "Renault",
#     "culoare": "verde"
#   }
# }
# variabila1 = pd.DataFrame(data)
# fisier = variabila1.to_csv("data.csv")

#IMI SALVEAZA DATELE INTR-UN FISIER DE TIP CSV, SI IL POT DESCHIDE CU EXCEL
