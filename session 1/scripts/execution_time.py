import time
import numpy as np

def find_max_array(numbers): # Algoritmo Theta(n)
    max = numbers[0]
    for number in numbers[1:]:
        if (number >= max):
            max = number
    return max

def find_max_matrix(numbers): # Algoritmo Theta(n^2)
    max = numbers[0][0]
    for i in range(numbers.shape[0]):
        for j in range(numbers.shape[1]):
            if (numbers[i][j] >= max):
                max = numbers[i][j]
    return max

def check_time(f, array, n, estimacion = None):
    tic = time.clock() 
    value = f(array) # solo es importante calcularlo para tomar el tiempo, no usaremos el valor obtenido
    toc = time.clock() 
    time_segs = toc - tic # tiempo en segundos que tomó la computación de f(array)
    if(estimacion == None):
        print("n: " + str(n) + " time: " + str(time_segs))
    else:
        print("n: " + str(n) + " time: " + str(time_segs) + " estimacion: " + str(estimacion))
    
    return time_segs


#### FIND_MAX_ARRAY ####
print("Análisis Theta(n)")

n_test_1 = 10000000
# Veamos cuánto se demora find_max_array con un arreglo de n_test_1 elementos
time_1 = check_time(find_max_array, np.random.rand(n_test_1), n_test_1)

n_test_2 = 100000
# Puedo tener una estimación de time_2 basada en los datos n_test_1 y time_1
estimacion_time_2 = (n_test_2 * time_1) / n_test_1 # Esto es regla de 3 pura y dura...

# Calculemos el valor real
time_2 = check_time(find_max_array, np.random.rand(n_test_2), n_test_2, estimacion_time_2)


#### FIND_MAX_MATRIX ####
print("Análisis Theta(n^2)")

n_test_3 = 100
# Veamos cuánto se demora find_max_matrix con una matriz de n_test_3 elementos
time_3 = check_time(find_max_matrix, np.random.rand(n_test_3,n_test_3), n_test_3)

# Si su computador es lo suficientemente potente, podría setear n_test_4 = 10000. En mi computador se demora 35 segundos app
n_test_4 = 10000

# Puedo tener una estimación de time_4 basada en el resultado del cálculo para n_test_3
estimacion_time_4 = ((n_test_4**2) * time_3) / (n_test_3**2) # Esto es regla de 3 pura y dura...

# Calculemos el valor real
time_4 = check_time(find_max_matrix, np.random.rand(n_test_4,n_test_4), n_test_4, estimacion_time_4)
