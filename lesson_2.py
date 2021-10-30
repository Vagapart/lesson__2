# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 20:03:00 2021

@author: ИнтелАв
"""

s = "cool.exe"

print(s[-3:])

v = [x+1 for x in range(0, 101, 10)]

text1 = "land привет здрасте"
v1 = text1.split()

text2 = " ".join(v1)

СколькоТочек = text1.count("т")

#Задание 1

newList = ["привет", "1", "element 3"]

#Задание 2

AnyList = []
elem = ""
while elem != "end":
    elem = input("Введите элемент №{0} (для окончания ввода введите 'end'): ".format(len(AnyList)+1))
    if elem != "end":
        AnyList.append(elem)
        
for i in range(1, len(AnyList), 2):
    AnyList[i-1], AnyList[i] = AnyList[i], AnyList[i-1]
    

#Задание 3
#через список
Zima = [12, 1, 2]
vesna = [3, 4, 5]
leto = [6, 7, 8]
osen = [9, 10, 11]
elem = int(input("Введите номер месяца: "))
if elem in Zima:
    print("Это зима")
if elem in vesna:
    print("Это весна")
if elem in leto:
    print("Это лето")
if elem in osen:
    print("Это осень")


#через dict
DictOfMonth = dict({1: "Зима", 2: "Зима", 3: "Весна",  4: "Весна",  5: "Весна",  6: "Лето",  7: "Лето",  8: "Лето",  9: "Осень", 10: "Осень", 11: "Осень",  12: "Осень"})
elem = int(input("Введите номер месяца: "))
print(DictOfMonth[i])

#Задание 4
text1 = input("Введите текст: ")
NewList = text1.split()
for i in range(0, len(NewList)):
    print("{0}. {1}".format(i+1, NewList[i]))
    
#Задание 5
my_list = [7, 5, 3, 3, 2]

elem = ""
while elem != "end":
    elem = input("Введите элемент (для окончания ввода введите 'end'): ")
    if elem != "end":
        my_list.append(int(elem))
    my_list.sort(reverse = True)

#Задание 6
names = ["название", "цена", "количесто", "ед."]
print(names[1])
count = int(input("Введите количество требуемых кортежей: "))
data1 = []

for i in range(0, count):
    dict1 = dict()
    for t in range(0, len(names)):
        dict1[str(names[t])] = input("Введите {0} в кортеж {1}: ".format(names[t], i+1))
    data1.append((i+1, dict1))
 
slovar = dict()
for t in range(0, len(names)):
    newList1 = []
    for i in range(0, len(data1)):
        if not data1[i][1][names[t]] in newList1:
            newList1.append(data1[i][1][names[t]])    
    slovar[names[t]] = newList1
   

