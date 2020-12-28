import numpy as np

def generate_guess(n):
    guess = list(np.random.randint(0,10,n))
    #print(guess)
    return guess

def check_pass(guess, password):
    return guess == password

def guess_pass(n, password):
    guess = generate_guess(n)
    it_number = 1
    while(check_pass(guess, password) == False):
        guess = generate_guess(n)
        it_number = it_number + 1
    return guess, it_number

# frequentist analysis
n = 1000
iterations = 0
for i in range(n):
    password = guess_pass(3, [2,1,1])
    iterations = iterations + password[1]

print(iterations/n)