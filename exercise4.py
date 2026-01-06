import numpy as np
import math 
epsilon = 0.00001

epsilon_arr = []
# smallest number that can be added to 1.0 that results in something different from 1.0
while 1.0 + epsilon != 1.0:
	epsilon = epsilon/2.0
	epsilon_arr.append(epsilon)

print("smallest epsilon found is", epsilon)

# smallest number that cant be represented as a float64

a = 1.0
a_arr = []
while float(a) == a and not math.isinf(a):
	a *= 2
	a_arr.append(a)
	#print(a)
print("smallest number that cant be represented found", a_arr[-2])

# kinetic energy
# Issue seems to be that for my initial definition I was getting 
# a value of 0.0 for the red blood cell which has the smallest v and m 
# in this case gamma is approx 1 and so gamma - 1 gives EK = 0
# so if v is very small I should be using the newtonian version of EK


c = 299792458
def EK(m,v):
	gamma = 1/np.sqrt(1 - (v**2)/(c**2))
	beta = (v/c)**2
	if beta < 10**(-10):
		return 0.5*m* v**2
	else:
		return (gamma - 1.0)*m*c**2
print("baseball:", EK(150,40))
print("cosmic ray:", EK(1.67*10**(-27),(1-10**(-15))*c))
print("power walker:", EK(70,3))
print("red blood cell:", EK(0.1,1.0))
