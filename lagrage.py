import math

r = input("Ingresa el valor del grado r: ")

x = [2, 2.2, 2.4, 2.6, 2.8]
y= [0.5103757, 0.5207893, 0.5104147, 0.4813306, 0.4359160]

px = 0

xx = 2.5

for i in xrange(r+1):
	l = y[i]
	for j in xrange(r+1):
		if j != i:
			l = l * ((xx - x[j]) / (x[i] - x[j]))
	px = px + l
print px