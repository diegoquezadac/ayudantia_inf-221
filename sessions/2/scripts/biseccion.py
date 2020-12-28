# BISECCIÓN CON DISTINTOS CRITERIOS DE DETENCIÓN

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
