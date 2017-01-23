#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import math
x0 = float(input("Introduce el valor de X0: "))
y0 = float(input("Introduce el valor de Y0: "))
eror = float(input("Introduce el error: "))

xn = "x0 + ((-2*y0 * ((2*(x0**2)) - 3.0/2)) / (8*x0*y0))"
yn = "y0 + ((-2*x0 * ((2*(y0**2)) - 1.0/2)) / (8*x0*y0))"

#Le damos un valor inicial a x1 y y1.
x1 = 0.0
y1 = 0.0
#Asignamos los valores de x0 y y0 a z0 y z1 para la condicion de parada.
z0 = x0
z1 = y0
#Condicion que se ejecutara mientras la magnitud sea mayor al error 
while float(math.sqrt(((x1 - z0)**2) + ((y1 - z1)**2))) > eror:

	#Evaluamos las funciones.
	x1 = float(eval(xn))
	y1 = float(eval(yn))
	#Guardamos los valores de x0 y y0 en z0 y z1.
	z0 = x0
	z1 = y0
	#guardamos los valores de x1 y y1 en las variables x0 y y0.
	x0 = x1
	y0 = y1
#imprimimos el resultado.
print "x1: %2.11f" %(x0)
print "y1: %2.11f" %(y0)
