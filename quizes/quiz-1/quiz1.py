def newton_backward(f,f_prime, initial_guess, epsilon): 
	#print("Aprox: " + str(initial_guess) + " Backward error: " + str(abs(f(initial_guess))))
	if(abs(f(initial_guess)) > epsilon): # revisar backward error
		return (newton_backward(f, f_prime, initial_guess - (f(initial_guess) / f_prime(initial_guess)), epsilon))
	else:
		return (initial_guess, abs(f(initial_guess))) # retorna aproximación y backward error asociado

def bisection_forward(f,a,b,epsilon, root):
    it_number = 1
    while( abs(root - (a + b)/2) > epsilon): # revisar forward error
        c = (a + b)/2
        #print("Iteration number: " + str(it_number) + " Aprox: " + str(c) + " Forward error: " + str(abs(root - c)))
        if f(c) == 0: break
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
        it_number = it_number + 1
    #print("Aprox: " + str((a+b)/2) + " Forward error: " + str(abs(root - (a + b)/2)))
    return (a+b)/2, abs(root - (a+b)/2), it_number

def c(f, a, b):
    return a - f(a) * ((a-b) / (f(a) - f(b))  )

def regulafalsi_forward(f,a,b,epsilon, root):
    it_number = 1
    while( abs(root - c(f, a, b) ) > epsilon): # revisar forward error
        #print("Iteration number: " + str(it_number) + " Aprox: " + str(c) + " Forward error: " + str(abs(root - c)))
        if f(c(f, a, b)) == 0: break
        if f(a)*f(c(f, a ,b)) < 0:
            b = c(f, a ,b)
        else:
            a = c(f, a ,b)
        it_number = it_number + 1
    #print("Aprox: " + str((a+b)/2) + " Forward error: " + str(abs(root - (a + b)/2)))
    return c(f, a, b), abs(root -  c(f, a, b)), it_number

def f(x):
    return 54*x**6 + 45*x**5 - 102*x**4 - 69*x**3 + 35*x**2 + 16*x - 4

def f_prime(x):
    return 16 + 70*x - 207*x**2 - 408*x**3 + 225*x**4 + 324*x**5

# Pregunta 1
print("question 1")

epsilon_backward = 0.5 * (10 ** -13) 

initial_guesses = [-2, -1, 0, 0.8, 1]
approximate_roots = []

for initial_guess in initial_guesses:
    approximate_roots.append( newton_backward(f, f_prime, initial_guess, epsilon_backward)[0] )

print("initial guesses and approximate roots: ")
print(list(zip(initial_guesses, approximate_roots)))

# Pregunta 2
print("question 2")

roots = (-1.38129848204399, -2/3, 0.205182924689048, 0.5, 1.17611555735495)
multiple_roots = []
for root in roots:
    if ( abs(f_prime(root) - 0) < epsilon_backward):
        multiple_roots.append(root)

print("roots for which newton is linear")
print(multiple_roots)

# Pregunta 3
print("question 3")

epsilon_forward = 0.5 * (10 ** -10) # soluciones correctas en 10 cifras

intervals = [(-2, -1, roots[0]), (0, 0.4, roots[2]), (0.3, 0.6, roots[3]), (0.6, 1.5, roots[4])]
solutions_bisection = []
solutions_regulafalsi = []
for a,b,root in intervals:
    solutions_bisection.append(bisection_forward(f, a, b, epsilon_forward, root))
    solutions_regulafalsi.append(regulafalsi_forward(f, a, b, epsilon_forward, root))

print("comparison between bisection and regulafalsi (solution, associated error, it_numbers): ")
for j in range(len(intervals)):
    print(f"Bisección:  {solutions_bisection[j]}" )
    print(f"Regula falsi: {solutions_regulafalsi[j]}")
    print("**********")
