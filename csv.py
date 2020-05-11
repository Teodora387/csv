import re
import csv
class Car():
    def __init__(self, marca, an, pret):
        self.marca=marca
        self.an=an
        self.pret=pret
    def __str__(self):
        return "marca: {}, an: {}, pret:{}".format(self.marca, self.an, self.pret)
    def __repr__(self):
        return "marca: {}, an: {}, pret:{}".format(self.marca, self.an, self.pret)

car1 = Car('peugeot', '2015', '50000 lei')
car2 = Car('BMW', '2019', '50000 euro')
car3 = Car('audi', '2002', '2000 euro')
car4 = Car('dacia', '1910', '500 lei')
cars=[car1, car2, car3, car4]
#print('cars: ', cars)
with open('CheapCars.csv', 'w') as f:
   writer=csv.writer(f)
   for car in cars:
       hold=re.findall('[0-9]', car.pret)
       val=re.findall('[a-z]', car.pret)
       price=''
       valuta=''
       for i in hold:
           price+=1
       for i in val:
           valuta+=i
       if (int(price)<5000 and valuta=='lei') or (int(price)<300 and valuta=='euro'):
           writer.writerow([car.marca, car.an, car,pret])