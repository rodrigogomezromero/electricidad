#!/usr/bin/env python
# -*- coding: utf-8 -*-


#author Rodrigo Gómez Romero
#license GPL v3

from math import log


intervalo = []
print "Ingrese funcion"
funcion     = raw_input()
funcion     = funcion.replace("^", "**")
print "Ingrese intervalo en la forma a,b"
input       = raw_input()
intervalo   = input.split(",")
print "Ingrese convergencia. Ejemplo 0.001"
convergencia = raw_input()

def bisect(f, a, b, e):
    n   = 0
    fa  = f(a)
    if fa == 0.0: return (a, n)
    fb  = f(b)
    if fb   == 0.0: return (b, n)

    while (abs(a-b) > e):
        c   = 0.5*(a+b)
        fc  = f(c)

        if fc == 0.0: return (c, n)
        n   = n + 1
        if fb*fc < 0.0:
            a   = c
            fa  = fc

        else:
            b   = c
            fb  = fc

    if fa < fb:
        return (a, n)
    else:
        return (b, n)

# prueba
# lo siguiente es usando programacion funcional
def f(x): return eval(funcion)
x= bisect(f, float(intervalo[0]), float(intervalo[1]), float(convergencia))
print "Raiz en",
x[0], "en la iteracion", x[1]