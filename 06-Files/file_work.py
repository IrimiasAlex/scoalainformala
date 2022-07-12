import pandas as pd

with open("fisier.txt", "w") as file:
    file.write("Buna seara")  # imi creeaza fisier nou

file = open("fisier.txt", "w")
file.write("Buna")
file.close()
file = open("fisier.txt", "w")
try:
    file.write("Buna ziua")
except Exception:
    pass
finally:
    file.close()

with open("fisier1.txt", "w") as file:
    file.write("Buna seara")

with open("fisier2.txt", "a") as file:
    file.write("Buna dimineata1")

with open("fisier2.txt", "r") as file:
    for line in file.readlines():
        print("line", line)

with open("fisier2.txt", "r") as file:
    for line in list(file):
        print('line', line)

df = pd.read_csv('EXEMPLU.csv')
print(df)
