# 1) se cere realizarea unei functii get_year_data() care sa
# contina 2 param: Setul de date si anul pentru care se doreste
# preluarea datelor
# get_year_data(dataset, "2019") returneaza
# {'2019': [('Romania', 84), ('Germany', 95), ..., ('Latvia',
# 85)]}
# 2) se cere realizarea unei functii get_country_data(dataset,
# "Romania"), care sa contina 2 param. datasetul si tara pentru
# care se doreste primirea datelor.
# ex: get_country_data(dataset, "Romania") returneaza
# {'Romania': [('2019', 84), ('2018', 86), ..., ('2011', 72)]}
# 3) de asemenea, se cere realizarea unei functii
# perform_average(country_data['Romania']) care sa returneze
# media per tara, ex perform_average(country_data['Romania'])
# returneaza 79.4

from exercitiul_2_import import dataset
import pandas as pd
import csv


def get_year_data(set_date, an):
    result = {an: []}
    # b = [item['coverage'] for key, value in set_date.items() for item in set_date[key] if item['year'] == str(an)]
    # res = {key: b for key, value in set_date.items()}
    # result[an].append(res)
    for key, value in set_date.items():
        for item in set_date[key]:
            if item['year'] == str(an):
                res = {key: item['coverage'] for key, value in set_date.items()}
                result[an].append(res)
    return result


df = pd.DataFrame(get_year_data(dataset,
                                '2019'))  # imi apar ambele tari la rezultat: {'2019': [{'Romania': 84, 'Austria': 84}, {'Romania': 90, 'Austria': 90}]}
df.to_csv('exercitiul_2.csv', index=False, mode='a', )


def get_country_data(set_date, tara):
    result = {tara: []}
    a = [d.get('year') for country, sublists in set_date.items() if country == tara for d in sublists]
    b = [e.get('coverage') for country, sublists in set_date.items() if country == tara for e in sublists]
    c = list(zip(a, b))
    result[tara].append(c)
    return result


df1 = pd.DataFrame(get_country_data(dataset, 'Romania'))
df1.to_csv('exercitiul_2.csv', index=False, mode='a', )


def perform_average(country_data):
    country_data = [e.get('coverage') for country, sublists in dataset.items() if country == country_data for e in
                    sublists]
    # return f'Media este : {round(sum(country_data) / len(country_data), 2)}'
    return str(round(sum(country_data) / len(country_data), 2))

print(perform_average(country_data='Bulgaria'))
print(type(perform_average(country_data='Bulgaria')))
df2 = pd.DataFrame(perform_average(country_data='Bulgaria'))
df2.to_csv('exercitiul_2.csv', index=False, mode='a', )
