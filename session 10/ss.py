def trim(l, delta):
    l_prime = [l[0]]
    last = l[0]
    for i in range(1, len(l)):
        if (last < (1 - delta) * l[i]):
            l_prime.append(l[i])
            last = l[i]
    return l_prime

def subset_sum(l, suma):
    s = set([0])
    for i in range(0, len(l)):
        s = s | set(map(lambda x: x + l[i], s))
        s = set(filter(lambda x: x <= suma, s))
    return max(s)

def app_subset_sum(l, suma, epsilon):
    s = set([0])
    delta = epsilon/len(l)
    for i in range(0, len(l)):
        s = s | set(map(lambda x: x + l[i], s))
        aux = list(s)
        aux.sort()
        s = set(trim(aux, delta))
        s = set(filter(lambda x: x <= suma, s))
    return max(s)

#print(subset_sum([6,4,1], 8))
#print(subset_sum([1, 1.01, 4, 6, 6.2],8))

print(subset_sum([101,104,102,201], 308))
print(app_subset_sum([101, 104,102,201], 308, 0.20))