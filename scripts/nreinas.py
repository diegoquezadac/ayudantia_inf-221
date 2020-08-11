### Problema de las N Reinas
### Diego Quezada - Ayudante Algoritmos y Complejidad
### Para ver el código en acción setee el valor de n a gusto, luego ejecute via consola como "python3 nreinas.py"

# 4 reinas -> 2 soluciones
# 8 reinas -> 12 soluciones

# Definir problema (Sea paciente para n > 11
n = 8
solucion = [-1 for i in range(n)]

def valido(etapa): # verifica si un estado (un nodo en el árbol de búsqueda) es válido o no.
    for i in range(0,etapa): # verificar que columnas anteriores no entren en conflicto.
        misma_fila = solucion[i] == solucion[etapa] # analizar si reina "i" y "etapa" está en la misma fila
        misma_diagonal = (abs(solucion[i] - solucion[etapa]) == abs(i - etapa)) # analizar si reina "i" y "etapa" está en la misma columna
        if(misma_fila or misma_diagonal): 
            return False
    return True

def reinas(etapa): # etapa indica en que columna estoy trabajando.
    if etapa > n: # no se encontró solución, se debe volver a un nodo anterior.
        return False
    exito = False
    solucion[etapa] = -1
    while((solucion[etapa] < n - 1) and not(exito)):
        print(solucion) # permite visualizar el trabajo del algoritmo
        solucion[etapa] = solucion[etapa] + 1 # probamos nueva configuración
        if (valido(etapa)): # verificar solución parcial
            if (etapa != n-1): # verificar condicion de término
                exito = reinas(etapa + 1) # faltan posicionar reinas. Se ramifica el árbol de búsqueda.
            else:
            	# para mostrar una solucion, setear exito en True.
            	# para mostrar todas las solucioens, setear exito en False y realizar append a soluciones.
                soluciones.append(list(solucion))
                #exito = True # tablero completo, se acaba la ejecución.
                exito = False # encontré una solución, pero seteo en False para seguir buscando otras.
    return exito

# lista para almacenar soluciones (listas)
soluciones = []

# ejecución
print(reinas(0)) # Debe ser 0 siempre

# output 
print("Se han encontrado " + str(len(soluciones)) + " soluciones para " + str(n) + " reinas" )

#print(soluciones)
