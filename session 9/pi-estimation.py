import random
from math import pi
def dist_from_origin(x,y):
    return (x**2 + y**2)**2

def estimate_pi(n):
    inside = 0
    for i in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if dist_from_origin(x,y) <= 1:
            inside = inside + 1
    return 4*inside/n

n_values = [100, 1000, 10000, 100000, 1000000, 10000000]
print('Real value: ' + str(pi))
for n in n_values:
    print('n: ' + str(n) + ' estimation: ' + str(estimate_pi(n)))