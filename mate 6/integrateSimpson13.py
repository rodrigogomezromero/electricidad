#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Importamos math
from math import *

def simpson13(n, a, b, f):
    #calculamos h
    h = (b - a) / float(n)
    #h = 0.2
    #Inicializamos nuestra varible donde se almacenara las sumas
    suma = 0.0
    #hacemos un ciclo para ir sumando las areas
    for i in range(1, n):
        #calculamos la x
        #x = a - h + (2 * h * i)
        x = a + i * h
        print "Valor de x = %f" % (x)
        # si es par se multiplica por 4
        if(i % 2 == 0):
            suma = suma + 2 * fx(x, f)
            print "f(x)  = %f" % (fx(x, f))
        #en caso contrario se multiplica por 2
        else:
            suma = suma + 4 * fx(x, f)
            print "f(x)  = %f" % (fx(x, f))

    #sumamos los el primer elemento y el ultimo
    suma = suma + fx(a, f) + fx(b, f)
    #Multiplicamos por h/3
    rest = suma * (h / 3)
    #Retornamos el resultado
    return (rest)


#Funcion que nos ayuda a evaluar las funciones
def fx(x, f):
    return eval(f)

#valores de ejemplo para la funcion sin(x) con intervalos de
n = 4
a = 0.0
b = 0.8
f = '0.2 + (25*x) - 200*(x**2)+ 675*(x**3) - 900*(x**4) + 400*(x**5)'
print(simpson13(n, a, b, f))
