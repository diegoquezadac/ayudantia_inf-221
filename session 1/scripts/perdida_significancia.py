import numpy as np
import pandas as pd

def f(x):
    return (1 - np.cos(x))/(np.sin(x))**2 

def g(x):
    return 1/(1 + np.cos(x))

# Puntos a evaluar
points = [0.1, 0.01, 0.001, 0.0001, 1e-05, 1e-06, 1e-07, 1e-08, 1e-09, 1e-10]

# Generar imágenes para f y g 
d = dict()
for x in points:
    #print("x = " + str(x) + " f(x) = " + str(f(x)) + " g(x) = " + str(g(x)))
    d[x] = [f(x), g(x)]

data = pd.DataFrame(d, index = ["f(x)", "g(x)"])
print(data.T)