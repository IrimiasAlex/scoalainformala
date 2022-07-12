import csv
import pandas as pd
from datetime import datetime
import json


dictionar_date = {
    "task": [],
    "data_limita": [],
    "persoana_responsabila": [],
    "categoria": []

}



meniu = [
    {
        "Listare_date.": 1,
        "Sortare." : 2,
        "Filtrare_date." : 3,
        "Adaugarea unui nou task in lista initiala." : 4,
        "Editarea detaliilor referitoare la task, data, persoana sau categorie." : 5,
        "Stergerea unui task din lista initiala." : 6,
        "Nimic." :7
    }
        ]

meniu_punctul_2 = [
    {
        "Sortare ascendenta task.": 1,
        "Sortare descendenta task." : 2,
        "Sortare ascendenta data." : 3,
        "Sortare descendenta data." : 4,
        "Sortare ascendenta persoana responsabila." : 5,
        "Sortare descendenta persoana responsabila." : 6,
        "Sortare ascendenta categorie." : 7,
        "Sortare descendenta categorie." : 8
    }
        ]

def adaugare_categorii(*args):                                          #export to txt
    with open("fisier_categorii.txt", "a") as file:
        file.write(ce_categorii + '\n')

lista_categorii = []
oprire = str(input("Doriti sa va opriti? da sau nu "))
global ce_categorii
while oprire == 'nu':
    ce_categorii = str(input("Categoria dorita este: "))
    adaugare_categorii(ce_categorii)
    lista_categorii.append(ce_categorii)
    oprire = str(input("Doriti sa va opriti? da sau nu "))
print('ok')

global task_1
def taskuri():
    task_1 = str(input("Task-ul dvs. este: "))
    dictionar_date['task'].append(task_1)                                     #adaugare task in dictionar

    data_limita=input("Data limita este: (DD/MM/YYYY) ")
    data=datetime.strptime(data_limita,"%d/%m/%Y").date()                   #alocare datetime unei variabile
    dictionar_date['data_limita'].append(data.strftime('%d/%B/%Y'))         #adaugare task in dictionar
# TODO de pus while in cazul in care nu se executa

    persoana_contact = str(input("Persoana dvs. de contact este: "))
    dictionar_date['persoana_responsabila'].append(persoana_contact)         #adaugare persoana responsabila in lista
    # TODO de pus while in cazul in care nu se executa

    categoria_1 = str(input('Din ce categorie face parte task-ul? '))
    while categoria_1 not in lista_categorii:                               #verificare daca categoriile concid cu cele de mai sus
        categoria_1 = str(input('Din ce categorie face parte task-ul? '))
    dictionar_date['categoria'].append(categoria_1)                          #adaugare categorie in lista
    print(dictionar_date)
    tabel = pd.DataFrame(dictionar_date)
    tabel.to_csv("fisier_taskuri.csv")                                       #export to csv
taskuri()

def introducere_taskuri(*args):
    intrebare = str(input('Mai ai de introdus task-uri? da sau nu '))
    while intrebare == 'da':
        taskuri()
        intrebare = str(input('Mai ai de introdus task-uri? da sau nu '))
    else:
        print('Acestea au fost')
introducere_taskuri()


afisare_meniu = json.dumps(meniu, indent = 1)                                               #la afisarea meniului asi vrea sa imi dispara paranteze....
afisare_meniu_punctul_2 = json.dumps(meniu_punctul_2, indent = 1)                           #la afisarea meniului asi vrea sa imi dispara paranteze....
def logica_meniu(*args):
    intreaba = str(input(f'{afisare_meniu}\nVrei sa alegi ceva din meniu? \n'))
    while intreaba in '1' or '2' or '3' or '4' or '5' or '6' or '7':
        if intreaba == '1':
            sortare = sorted(dictionar_date, key = lambda x: x[0])                                  #aici imi sorteaza lista de categorii de la inceput.Cred ca ar trebui cea cu taskuri..
            tabel = pd.DataFrame(sortare)
            tabel.to_csv("fisier_taskuri.csv")
            print(f'Lista sortata este:\n{sortare}')
            # TODO de adaugat o comanda sa imi adauge in fisier_categorii lista sortata
            break
        elif intreaba == '2':
            intreaba_2 = str(input(f'{afisare_meniu_punctul_2}\nCe alegeti din meniu?'))
            if intreaba_2 == '1':
                res = {'task': sorted(dictionar_date['task']) for key in sorted(dictionar_date)}
                tabel = pd.DataFrame(res)
                tabel.to_csv("fisier_taskuri.csv")
            elif intreaba_2 == '2':
                res = {'task': sorted(dictionar_date['task'], reverse = True) for key in sorted(dictionar_date)}
                tabel = pd.DataFrame(res)
                tabel.to_csv("fisier_taskuri.csv")
            elif intreaba_2 == '3':
                res = {'data_limita': sorted(dictionar_date['data_limita']) for key in sorted(dictionar_date)}
                tabel = pd.DataFrame(res)
                tabel.to_csv("fisier_taskuri.csv")
            elif intreaba_2 == '4':
                res = {'data_limita': sorted(dictionar_date['data_limita'], reverse = True) for key in sorted(dictionar_date)}
                tabel = pd.DataFrame(res)
                tabel.to_csv("fisier_taskuri.csv")
            elif intreaba_2 == '5':
                res = {'persoana_responsabila': sorted(dictionar_date["persoana_responsabila"]) for key in sorted(dictionar_date)}
                tabel = pd.DataFrame(res)
                tabel.to_csv("fisier_taskuri.csv")
            elif intreaba_2 == '6':
                res = {'persoana_responsabila': sorted(dictionar_date["persoana_responsabila"], reverse = True) for key in sorted(dictionar_date)}
                tabel = pd.DataFrame(res)
                tabel.to_csv("fisier_taskuri.csv")
            elif intreaba_2 == '7':
                res = {'categoria': sorted(dictionar_date['categoria']) for key in sorted(dictionar_date)}
                tabel = pd.DataFrame(res)
                tabel.to_csv("fisier_taskuri.csv")
            elif intreaba_2 == '8':
                res = {'categoria': sorted(dictionar_date['categoria'], reverse = True) for key in sorted(dictionar_date)}
                tabel = pd.DataFrame(res)
                tabel.to_csv("fisier_taskuri.csv")
        elif intreaba == '4':
            taskuri()
            introducere_taskuri()
            break
        elif intreaba == '6':
            task_sters = str(input('Ce task vrei sa stergi? '))
            if task_sters in taskuri():

                tabel = pd.DataFrame(dictionar_date)
                tabel.to_csv("fisier_taskuri.csv")
    else:
        return intreaba
logica_meniu()
