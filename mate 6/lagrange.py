#!/usr/bin/env python
# -*- coding: utf-8 -*-

r = eval(input("Ingresa el valor del grado r: "))
x = list(eval(input("Ingrese los valores de X separados por comas: ")))
y = list(eval(input('Ingrese los valores de Y separados por comas : ')))

#x = [2, 2.2, 2.4, 2.6, 2.8]
#y = [0.5103757, 0.5207893, 0.5104147, 0.4813306, 0.4359160]
X = float(eval(input(' Ingrese el valor de px: ')))

px = 0


#X = 2.5

for i in range(r + 1):
    l = y[i]
    for j in range(r + 1):
        if j != i:
            l = l * ((X - x[j]) / (x[i] - x[j]))
        px = px + l
print (px)