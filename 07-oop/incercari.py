# #am ajuns la exercitii_decoratori
# from operator import itemgetter
#
#
# class Catalog_de_prajituri:
#
#     lista_prajituri = []
#
#     def __init__(self, nume, pret, gramaj):
#         self.name = str(nume)
#         self.price = int(pret)
#         self.weight = int(gramaj)
#         self.lista_prajituri.append([self.name, self.price, self.weight])
#
#     def afisare_lista(self):
#         print(self.lista_prajituri)
#
#     @staticmethod
#     def sortare_gramaj():
#         sortata_gramaj = sorted(Catalog_de_prajituri.lista_prajituri, key=itemgetter(2))
#         return f'Lista sortata dupa gramaj este: {sortata_gramaj}'
#
#     def sortare_pret():
#         sortata_pret = sorted(Catalog_de_prajituri.lista_prajituri, key=itemgetter(1))
#         return f'Lista sortata dupa pret este : {sortata_pret}'
#
#
# class Tort(Catalog_de_prajituri):
#
#     def __init__(self, nume, pret, gramaj, etajat=False, glazura='ciocolata'):
#         super().__init__(nume, gramaj, pret)
#         self.etajat = etajat
#         self.glazura = glazura
#
#
#     def __str__(self):
#         return f'Etajarea este {self.etajat}, iar glazura este {self.glazura}'
#
# obiect = Catalog_de_prajituri('Broscuta', 15, 150)
# obiect1 = Catalog_de_prajituri('Spumoasa', 30, 100)
# obiect2 = Catalog_de_prajituri('Ecler', 17, 125)
#
# tort = Tort(nume='A', pret=70, gramaj=150, etajat=True, glazura='Martipan')
# tort1 = Tort(nume='B', pret=80, gramaj=100, etajat=False, glazura='Portocale')
#
#
# print(obiect.afisare_lista())
# print(Catalog_de_prajituri.sortare_gramaj())
# print(Catalog_de_prajituri.sortare_pret())
# print(tort)
# print(tort1)

