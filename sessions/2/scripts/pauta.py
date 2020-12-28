# Diego Quezada
# Ayudantía 2
# Algoritmos y complejidad

import numpy as np

### FUNCIONES PREGUNTA 1

def newton_backward(f,f_prime, initial_guess, epsilon): 
	print("Aprox: " + str(initial_guess) + " Backward error: " + str(abs(f(initial_guess))))
	if(abs(f(initial_guess)) > epsilon): # Revisar backward error
		return (newton_backward(f, f_prime, initial_guess - (f(initial_guess) / f_prime(initial_guess)), epsilon))
	else:
		return initial_guess

def newton_forward(f,f_prime, initial_guess, epsilon, root): 
	print("Aprox: " + str(initial_guess) + " Forward error: " + str(abs(root- initial_guess)))
	if(abs(initial_guess - root) > epsilon): # Revisar forward error (error absoluto)
		return newton_forward(f, f_prime, initial_guess - (f(initial_guess) / f_prime(initial_guess)), epsilon, root)
	else:
		return initial_guess

### FUNCIONES PREGUNTA 2

def f(x):
	return np.log(x + 1) + x**2 - 3 # root 1.4504267650569250082 https://www.wolframalpha.com/input/?i=%5Clog%28x%2B1%29%2Bx%5E%7B2%7D-3

def f_prime(x):
	return 1/(x+ 1) + 2*x

### FUNCIONES PREGUNTA 4

def g(x,y):
    return 21*(x**6) - 21*(x**4) + 21*(x**2) + y**3 + 21

def g_prime_y(y):
    return 3*(y**2)

def y(x):
    return np.cbrt(-(21*(x**6) - 21*(x**4) + 21*(x**2) + 21)) 

def newton_y(g, g_prime_y, y, x, initial_guess, epsilon):
    if(abs(initial_guess - y(x))  >= epsilon): # revisar forward error
        new_y = initial_guess -( g(x, initial_guess)/g_prime_y(initial_guess) )
        return newton_y (g, g_prime_y, y, x, new_y, epsilon)
    else: 
        return initial_guess

### FUNCION PREGUNTA 5

def secant_backward(f, x1, x2, epsilon):
    print("Aprox: " + str(x2) + " Backward error: " + str(abs(f(x2))))
    if (abs(f(x2)) <= epsilon): # revisar backward error
        return x2
    else:
        return secant_backward(f, x2, x2 - f(x2) * (x2-x1)/(f(x2) - f(x1)), epsilon)

# Establecer cotas para los errores
epsilon_backward = 10 ** (-10)
epsilon_forward = 0.5 *10**(-5) # 5 decimales correctos

### PREGUNTA 2
print("Pregunta 2")
print("Newton Backward")
aprox_root = newton_backward(f, f_prime, 1, epsilon_backward) # Deberia ser similar a 1.4504267650569250082
print("Newton Forward:")
print(newton_forward(f, f_prime, 1, epsilon_forward, aprox_root)) 

### PREGUNTA 4
points = list()
initial_y = 1
epsilon = 0.0000000000001 # ajustamos epsilon
for x in np.arange(1,5,0.1):
    points.append( (x, newton_y(g, g_prime_y, y, x, initial_y, epsilon)) )
    initial_y  = points[-1][1]

# VERIFICACION PREGUNTA 4
print("Verificacion Pregunta 4")
for x,y in points:
    print( g(x,y) ) # Deberian ser valores cercanos a 0

### PREGUNTA 5
print("Pregunta 5")
x1 = 100
x2 = x1- (f(x1) / f_prime(x1)) # g(x) de newton
print("Newton Backward")
newton_backward(f, f_prime, x1, epsilon_backward)
print("Secant Backward")
secant_backward(f,x1,x2,epsilon_backward)