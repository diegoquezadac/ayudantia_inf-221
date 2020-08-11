def biseccion(f,a,b,epsilon):
    while( (b-a)/2 > epsilon):
        c = (a + b)/2
        if f(c) == 0: break
        if f(a)*f(c) < 0:
            b = c
        else:
        	a = c
    return (a+b)/2