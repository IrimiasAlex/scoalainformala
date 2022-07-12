import csv

lista_masini = []

masina = [
    {
        "id": [],
        "brand": [],
        "model": [],
        "hp" : [],
        "price" : []
    }
]

def citire_din_csv():
    with open('input.csv' , 'r') as csv_file:
        cititorcsv = csv.reader