import numpy as np

#Implementing the bisection algorithm with a simple linear function

def f(x):
	return 3*x + 1

#end points

a = -1

b = 1
tol = 10**(-5)


while (b - a)/2 > tol:
	c = (a + b)/2
	if f(c) == 0:
		break
	elif  f(a)*f(c) < 0:
		b = c
	elif  f(b)*f(c) < 0:
          	a = c
	print(c)
print("root found", c)

#Implementing Newton Raphson algorithm for simple linear function

def derf(x):
	return 3 #in this simple linear case we can just define the der directly ig 

x1 = -1 

while abs(f(x1)) > tol:
	x1 = x1 - (f(x1)/derf(x1))

print("root found", x1)	
