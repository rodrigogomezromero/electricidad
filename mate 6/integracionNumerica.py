#!/usr/bin/env python
# -*- coding: utf-8 -*-

#importamos math
from math import *


def f(x, fun):
    return eval(fun)


#creamos la funcion
def integrateN():

    #pedimos al usuario los intervalos
    a = float(input('Ingrese el valor de A: '))
    b = float(input('Ingrese el valor de B: '))

    #Pedimos al usuario la funcion a integrar
    #f = "sin(x)"

    #Pedimos al usuario l valor de N
    n = float(input('Ingrese el valor de N: '))

    #Calculamos H
    h = (b - a) / n
    #realizamos la suma del primer y ultimo intervalo
    suma = (h / 2) * (sin(a) + sin(b))
    #Calculamos la suma de los demas intervalos
    for i in range(1, 5):
        xi = a + (i * h)
        suma = suma + (h * sin(xi))
    #Imprimos suma
    print (suma)

integrateN()