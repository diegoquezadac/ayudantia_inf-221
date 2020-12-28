import numpy as np
def solve_knapsack(v,w,n,W):
    V = np.zeros((n, W))
    for i in range(1, n):
        for j in range(W):
            leave_val = V[i - 1][j]
            if( j >= w[i]):
                take_val = v[i] + V[i - 1][j - w[i]]
            else:
                take_val = - np.inf
            V[i][j] = max(leave_val, take_val)
    return V[n - 1][W - 1]

n = 4
W = 10
v = [10, 40, 30, 50]
w = [5, 4, 6, 3]
print(solve_knapsack(v,w,n,W))