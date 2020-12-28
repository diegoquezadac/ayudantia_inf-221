import random

def fisher_shuffle(A):

    # for each element of A
    for i in range(len(A)): 

        # select a random index of A[:i + 1]
        j = random.randint(0, i) 

        # swap element number i with element number j
        temp = A[i]
        A[i] = A[j]
        A[j] = temp

def naive_shuffle(A):

    # for each element of A
    for i in range(len(A)):

        # select a random index of A
        rand_index = random.randint(0, len(A) - 1)

        # swap element number i with element number random_index
        temp = A[i]
        A[i] = A[rand_index]
        A[rand_index] = temp


lista = [1,2,3,4]
fisher_shuffle(lista)
print(lista)