#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import *
from sympy import diff


class NumericalMethods():
    """
    # Documentacíon para  NumericalMethods  clase para Obtener raices de
    # ecuaciondes de la forma: # F(x) = 0
    # Autor: Rodrigo Gómez Romero Mtc:10-11253
    # rodrigogomez05@gmail.com
    # Metodos : Biseccion, Newton , Fórmula general con soporte para
    # números complejos
    #

    """
    def __init__(self):

        msj = """
            # Class NumericalMethods
            # Version: 0.0.1
            # Author: Rodrigo Gomez Romero
            # http://www.rodrigogr.com/blog

            """
        print (msj)

    def caudratica(self, a, b, c):
        """
        # Metodo de Fórmula general
        # @parameters:  coeficientes a, b y c
        # @return:  result

        """
        #Calculamos el determinante
        det = (b ** 2) - (4 * a * c)
        #Evaluamos el determiante, si es menor a 0 usaremos complejos
        if det < 0:
            #multiplicamos por -1
            det = det * -1
            #Realizamos el calulo de la parte Imaginaria y la real
            det = sqrt(det) / (2 * a)
            result = float(-b) / (2 * a)

            #Creamos el numero complejo
            result = complex(result, det)
            #devolvemos el número complejo
            return result
        #Si no es complejo usamos la formula general
        else:
    #Calculamos el valor del primer resultado y el segundo
    #e imprimimos los valores

            result = float((-1 * b) + sqrt(det)) / (2 * a)
            result2 = float((-1 * b) - sqrt(det)) / (2 * a)
            return ("x1= %f; x2= %f") % (result, result2)

    def bisect(self, fx, a, b, e):
        """
        # Metodo de biseccion
        # Recibe: la funcion , el punto a , el punto b ,y la cota de ERROR
        # Retorna : n el numero de iteraciones y a ó b la raiz que va a con esa
        # cota de ERROR

        """
        n = 0
        fa = self.f(a, fx)

        if fa == 0.0:
            return (a, n)

        fb = self.f(b, fx)

        if fb == 0.0:
            return (b, n)

        while (abs(a - b) > e):

                c = 0.5 * (a + b)
                fc = self.f(c, fx)

                if fc == 0.0:
                    return(c, n)
                n = n + 1
                if fb * fc < 0.0:
                    a = c
                    fa = fc

                else:
                    b = c
                    fb = fc

        if fa < fb:
            return (a, n)

        else:
            return (b, n)

    def newton(self, x_0, fx, cota):

        """
        # Metodo de Newton
        # Recibe: la funcion , el punto inicial ,y la cota de ERROR
        # Retorna : x_1 la raiz que va a con esa cota de ERROR

        """
    #Variable que nos servira para almacenar el valor de las
    #aproximaciones anteriores.
        z = 0

        #Usando una libreria externa calculamos la derivada de la función.
        dfx = str(diff(fx))

        #Evaluamos si la deriva ni la funcion sean diferentes de cero.
        if self.f(x_0, dfx) != 0 and self.f(x_0, dfx) != 0:

            #empezamos a calular aproximaciones hasta que sea menor que la
            #cota de error
            while abs(x_0 - z) > cota:
                #Obtenemos el valor de nuestra aproximacion
                x_1 = x_0 - (self.f(x_0, fx) / self.f(x_0, dfx))
                #almacenamos el valor de la aproximacion aneterior
                z = x_0
                #almacenamos el valor de la aproximación actual
                x_0 = x_1
                #Retronamos el valor de la raíz
                return(x_1)
        else:
            #Si son iguales a cero  imprimimos un error
            raise "f(x) o df(x) igual  a cero Error "
            print("El valor inicial en f(x) y su derivada no pude ser 0")


    def secante(self, fx, a, b, cota):
        fx = fx
        dfx = str(diff(fx))
        x_0 = (a + b) * 0.5
        x_1 = x_0 - (self.f(x_0, fx) / self.f(x_0, dfx))
        error = cota
        x_2 = 0

        while (abs(self.f(x_2, fx)) < error):
            a = ((self.f(x_1, fx) * (x_0 - x_1)))
            b = (self.f(x_0, fx) - self.f(x_1, fx))
            x_2 = x_1 - (a / b)
            x_0 = x_1
            x_1 = x_2
        print (x_1)


    def punto_fijo(self, x_0, gx, error):
        x_1 = self.f(x_0, gx)
        y = 0
        while (abs(x_1 - y) > error):
            x_1 = self.f(x_0, gx)
            print (x_1)
            y = x_0
            x_0 = x_1
        return (x_1)

    #Método para evaluar funciones
    def f(self, x, fx):
            return eval(fx)

#ejemplo del uso del método de la secante
fx = "(x**2 / 4) - sin (x)"
a = 1
b = 2.5

cota = 0.0000001

c = NumericalMethods()
c.secante(fx, a, b, cota)
