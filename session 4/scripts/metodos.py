import numpy as np
import scipy.integrate as integrate

def rectangle_rule(f,a,b,n): # n + 1 puntos
    h = (b - a) / n
    suma_imagenes = 0
    x = a
    for i in range(0, n + 1): # i desde 0 hasta n
        suma_imagenes = suma_imagenes + f(x)
        x = x + h # siguiente x
    return h * suma_imagenes

def trapezoidal_rule(f,a,b,n): # n + 1 puntos
    h = (b - a) / n
    suma_imagenes = 0
    x = a
    for i in range(0, n + 1): # i desde 0 hasta n
        if (i == 0 or i == n): # f(a) y f(b)
            suma_imagenes = suma_imagenes + f(x)
        else: 
            suma_imagenes = suma_imagenes + 2 * f(x)
        x = x + h # siguiente x
    return (h/2) * suma_imagenes

def simpson_rule(f,a,b,n): # n + 1 puntos
    h = (b - a) / n 
    suma_imagenes = 0 
    x = a 
    for i in range(0, n + 1): # i desde 0 hasta n
        if (i == 0 or i == n): # f(a) y f(b)
            suma_imagenes = suma_imagenes + f(x)
        else: 
            if(i % 2 == 0):
                suma_imagenes = suma_imagenes + 2 * f(x)
            else:
                suma_imagenes = suma_imagenes + 4 * f(x)
        x = x + h # siguiente x
    return (h/3) * suma_imagenes

f,a,b,n = (np.exp, 1, 1.5, 100)
rectangle = rectangle_rule(f, a, b, n)
trapezoidal = trapezoidal_rule(f, a, b, n)
simpson = simpson_rule(f, a, b, n)
real_value = integrate.quad(f, a, b)[0] # retorna una tupla (value, error)

print("Rectangle rule error: " + str(abs(real_value - rectangle)))
print("Trapezoidal rule error: " + str(abs(real_value - trapezoidal)))
print("Simpson rule error: " + str(abs(real_value - simpson)))
