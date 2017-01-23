#!/usr/bin/env python
# -*- coding: utf-8 -*-


def euler(x0, xn, y0, n, fx):
    #Calculamos H la distancia entre los intervalos

    h = (xn - x0) / n
    yj = y0
    xj = x0

    #Recorremos para calcular las aproximaciones
    for i in range(n):
        xi = xj + (i * h)
        #ff = fx(xj, fx)
        yi = yj + eval(fx) * h
        yj = yi
        xj = xi
        print (str(xj) + " " + str(yj))
    print("La aproximación es : %f") % (yi)


#Funcion que nos ayuda a evaluar las funciones
def fx(x, f):
    return eval(f)

x0 = 0.0
xn = 2.0
y0 = 2.0
n = 10
fx = 'yj - (xj ** 2) + 1'

euler(x0, xn, y0, n, fx)
