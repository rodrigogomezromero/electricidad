import math
a = input("ingresa el valor de a:\n")
b = input("ingresa el valor de b:\n")
c = input("ingresa el valor de c:\n")
#Calculamos el determinate
det = (b**2)-(4*a*c)
#Evaluamos el determiante, si es menor a 0 usaremos complejos
if det < 0:
	#multiplicamos por -1 
	det = det*-1
	det = math.sqrt(det)/(2*a)
	result = float(-b)/(2*a)
	
	#Creamos el numero complejo
	result = complex(result,det)
	print result
	

#Si no es complejo usamos la formula general
else:
	#Calculamos el valor del primer resultado y el segundo e imprimimos los valores7

	result  =float(((-1*b)+math.sqrt(det))/2*a) 
	result2 = float(((-1*b)-math.sqrt(det))/2*a) 
	print("x1= %f; x2= %f")%(result,result2)

