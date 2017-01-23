#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import math


class Electricidad(object):
	"""docstring for Electricidad"""
	def __init__(self):
		self.E = 8.854e12
		self.PI = math.pi
		self.K = 9e9
	

	def coulomb(self):
		q_uno = float(raw_input("Ingrese el valor de la carga uno ( ejemplo 6e-4):"))
		q_dos = float(raw_input("Ingrese el valor de la carga dos ( ejemplo 6e-4):"))
		d = float(raw_input("Ingrese la distancia que hay entre las cargas (ejemplo: 5.55 o 10.0): "))
		
		f =	self.K * (q_uno * q_dos) / (d ** 2)
		return (f)


	def coulomb_v(self):
		
		q_uno =	float(raw_input("Ingrese el valor de la carga uno ( ejemplo 6e-4): "))
		v_uno =	list(str(raw_input("Ingrese la posicion de Q1 (separados por comas)"))

		#Volvemos enteros los indices de nuestro vector
		v_uno = self.vector_to_int(v_uno)

		q_dos =	float(raw_input("Ingrese el valor de la carga dos ( ejemplo 6e-4): "))
		v_dos =	list(str(raw_input("Ingrese la posicion de Q2 (ejemplo 154): ")).split(" "))

		#Convertimos los indices a int
		v_dos = self.vector_to_int(v_dos)

		# Vecotor posicion
		v_p = self.vector_pos(v_uno,v_dos)

		# Magnitud de Vector posicion
		M = self.magnitud_v(v_p)

		#Calculo de la fuerza
		f = (q_uno*q_dos)/(4*self.PI*self.E*(M**3))
		

		#Lista que almacena el vector resultante
		res = []

		#Multiplicamos la fuerza por cada componente de nuestro vector posicion
		for x in v_p:

			x = x * f
			res.append(x)

		#Imprimimos el vector de la fuerza resultante
		return res


	def campo_e_origin(self):

		q = float(raw_input("Ingrese el valor de la carga (ejemplo 100e-6): "))
		v_uno =	list(str(raw_input("Ingrese la posicion de Q1 (ejemplo 1 5 4):")).split(" "))
		v_uno = self.vector_to_int(v_uno)
 
		#obtenemos la magnitud del vector
		M = self.magnitud_v(v_uno)
		E = (q) / (4 * self.PI * self.E * (M ** 3))
		res = []

		#Multiplicamos la fuerza por cada componente de nuestro vector posicion
		for x in v_uno:

			x = x * E
			res.append(x)

		#Imprimimos el vector de la fuerza resultante
		return res


	def vector_pos(self, v_uno, v_dos):

		v_p = [v_uno[0] - v_dos[0], v_uno[1] - v_dos[1], v_uno[2] - v_dos[2]]
		return v_p


	def magnitud_v(self, v_p):

		M = math.sqrt((v_p[0] ** 2) + (v_p[1] ** 2) + (v_p[2] ** 2))
		return M


	def vector_to_int(self,v):
		v[0] = int(v[0])
		v[1] = int(v[1])
		v[2] = int(v[2])

		return v
	


c = Electricidad()
print c.campo_e_origin()
