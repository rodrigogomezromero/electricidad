#!usr/bin/env python
# -*- coding: utf-8 -*-

x = [2, 2.2, 2.4, 2.6, 2.8]
y = [0.5103757, 0.5207893, 0.5104147, 0.4813306, 0.4359160]
#Arreglos para almacenar diferencias
a_1 = []
a_2 = []
a_3 = []
a_4 = []

#Calculo para la primer diferencia
for i in range(len(x)):
    j = i + 1
    if (j < len(x)):
        res = (y[j] - y[i]) / (x[j] - x[i])
        a_1.append(res)

for k in range(len(a_1)):
    j = k + 2
    l = k + 1
    if (j <= len(a_1)):
        res = (a_1[l] - a_1[k]) / (x[j] - x[k])
        a_2.append(res)
j = 0
l = 0
for k in range(len(a_2)):
    j = k + 3
    l = k + 1
    if (j <= len(a_2) + 1):
        res = (a_2[l] - a_2[k]) / (x[j] - x[k])
        a_3.append(res)

j = 0
l = 0
for k in range(len(a_3)):
    j = k + 4
    l = k + 1
    if (j <= len(a_3) + 2):
        res = (a_3[l] - a_3[k]) / (x[j] - x[k])
        a_4.append(res)
#GERENERAMOS EL ARREGLO DE LAS DIFERENCIAS  2.5 - Xo
px = 2.5
Xn = []
for i in x:
    Xn.append(px - i)
rest = 0
for i in range(len(a_1)):
    rest = Xn[i] * a_1[i] + rest

print (rest)
#Multiplicar  cada diferencia por la diferencia de las X
# a* (x-x[i])
