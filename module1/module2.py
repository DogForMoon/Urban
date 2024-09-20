from random import seed

def matrix(n, m, value):
    a = list()
    for _ in range(n):
        a.append([value]*m)
    return a


result1 = matrix(2, 2, 0)
print(result1)

