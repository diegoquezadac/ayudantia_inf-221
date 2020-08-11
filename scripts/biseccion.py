def biseccion(f,a,b,epsilon): # f es una función con un cero en [a,b]
    while((b-a)/2 > epsilon): # mientras esté cometiendo un error mayor a epsilon
        c = (a + b)/2 # punto medio de [a,b]
        if f(c) == 0: break 
        if f(a)*f(c) < 0: # si el cero está en [a,c]
            b = c # sigo trabajando en ese intervalo
        else:
        	a = c # de lo contrario está en [b,c], sigo trabajando por ahí.
            
    return (a+b)/2
