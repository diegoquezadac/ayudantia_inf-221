# Diego Quezada
# Ayudantía 2
# Algoritmos y complejidad

import numpy as np

### PREGUNTA 1

def newton_backward(f,f_prime, initial_guess, epsilon): 
	print("Aprox: " + str(initial_guess) + " Backward error: " + str(abs(f(initial_guess))))
	if(abs(f(initial_guess)) > epsilon): # revisar backward error
		return (newton_backward(f, f_prime, initial_guess - (f(initial_guess) / f_prime(initial_guess)), epsilon))
	else:
		return initial_guess

def newton_forward(f,f_prime, initial_guess, epsilon, root): 
	print("Aprox: " + str(initial_guess) + " Forward error: " + str(abs(root- initial_guess)))
	if(abs(initial_guess - root) > epsilon): # revisar forward error (error absoluto)
		return newton_forward(f, f_prime, initial_guess - (f(initial_guess) / f_prime(initial_guess)), epsilon, root)
	else:
		return initial_guess

### PREGUNTA 2

def f(x):
	return np.log(x + 1) + x**2 - 3 # root 1.4504267650569250082 https://www.wolframalpha.com/input/?i=%5Clog%28x%2B1%29%2Bx%5E%7B2%7D-3

def f_prime(x):
	return 1/(x+ 1) + 2*x

### BISECCIÓN CON DISTINTOS CRITERIOS DE DETENCIÓN

def biseccion(f,a,b,epsilon):
    it_number = 1
    while( (b-a)/2 > epsilon): # revisar cota superior del forward error
        c = (a + b)/2
        print("Iteration number: " + str(it_number) + " Aprox: " + str(c) + " Backward error: " + str(abs(f(c))))
        if f(c) == 0: break
        if f(a)*f(c) < 0:
            b = c
        else:
        	a = c
        it_number = it_number + 1
    print("Aprox: " + str((a+b)/2) + " Backward error: " + str(abs(f((a+b)/2))))
    return (a+b)/2

def biseccion_backward(f,a,b,epsilon):
    it_number = 1
    while( abs(f((a + b) / 2)) > epsilon): # revisar backward error
        c = (a + b)/2
        print("Iteration number: " + str(it_number) + " Aprox: " + str(c) + " Backward error: " + str(abs(f(c))))
        if f(c) == 0: break
        if f(a)*f(c) < 0:
            b = c
        else:
        	a = c
        it_number = it_number + 1
    print("Aprox: " + str((a+b)/2) + " Backward error: " + str(abs(f((a+b)/2))))
    return (a+b)/2

def biseccion_forward(f,a,b,epsilon, root):
    it_number = 1
    while( abs(root - (a + b)/2) > epsilon): # revisar forward error
        c = (a + b)/2
        print("Iteration number: " + str(it_number) + " Aprox: " + str(c) + " Forward error: " + str(abs(root - c)))
        if f(c) == 0: break
        if f(a)*f(c) < 0:
            b = c
        else:
        	a = c
        it_number = it_number + 1
    print("Aprox: " + str((a+b)/2) + " Forward error: " + str(abs(root - (a + b)/2)))
    return (a+b)/2

### PREGUNTA 4
def g(x,y):
    return 21*(x**6) - 21*(x**4) + 21*(x**2) + y**3 + 21

def g_prime_y(y):
    return 3*(y**2)

def y(x):
    return np.cbrt(-(21*(x**6) - 21*(x**4) + 21*(x**2) + 21)) 

def newton_y(g, g_prime_y, y, x, initial_guess, epsilon):
    if(abs(initial_guess - y(x))  >= epsilon):
        new_y = initial_guess -( g(x, initial_guess)/g_prime_y(initial_guess) )
        return (newton_y (g, g_prime_y, y, x, new_y, epsilon))
    else: 
        return initial_guess

# set epsilon
epsilon = 0.5 *10**(-5) # 5 decimales correctos

### PREGUNTA 2
print("Biseccion method:")
print(biseccion(f, 0,5, epsilon))
print("Biseccion backward method:")
print(biseccion_backward(f, 0,5, epsilon))
print("Newton method:")
print(newton_forward(f, f_prime, 1, epsilon, 1.4504267650569250082)) 

### PREGUNTA 4
points = list()
initial_y = 1
epsilon = 0.0000000000001 # ajustamos epsilon
for x in np.arange(1,5,0.1):
    points.append( (x, newton_y(g, g_prime_y, y, x, initial_y, epsilon)) )
    initial_y  = points[-1][1]

### VERIFICACIÓN PREGUNTA 4
print("VERIFICACION")
for x,y in points:
    print( g(x,y) ) # deberian ser valores cercanos a 0