#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Importamos math
from math import *


#Definimos la funcion
#@ n: numero de x
#@ a y b los intervalos de la integral
#@ f: La funcion a integrar
def simpson38(n, a, b, f):
    #calculamos h
    h = (b - a) / n
    #Inicializamos nuestra varible donde se almacenara las sumas
    suma = 0.0
    #hacemos un ciclo para ir sumando las areas
    for i in range(1, n):
        #calculamos la x
        x = a + i * h
        # si es multiplo de 3 se multiplica por 6/8
        if(i % 3 == 0):
            suma = suma + ((6.0 / 8) * (h) * fx(x, f))
        #en caso contrario se multiplica por 9/8
        else:
            suma = suma + ((9.0 / 8) * (h) * fx(x, f))
    #sumamos los el primer elemento y el ultimo
    suma = suma + ((3.0 / 8) * h * (fx(a, f) + fx(b, f)))

    #Retornamos el el valor de suma
    return (suma)


#Funcion que nos ayuda a evaluar las funciones
def fx(x, f):
    return eval(f)

#valores de ejemplo para la funcion sin(x) con intervalos de
n = 4
a = 0.0
b = 0.8
f = '0.2 + (25*x) - 200*(x**2)+ 675*(x**3) - 900*(x**4) + 400*(x**5)'

print(simpson38(n, a, b, f))