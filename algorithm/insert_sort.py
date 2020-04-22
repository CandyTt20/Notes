import random


def insert_sort(l):
    for i in range(1, len(l)):
        flag = l[i]
        p = list(range(0, i))[::-1]
        for j in p:

            if l[j] > flag:

                l[j], l[j + 1] = flag, l[j]

    return l


l = [random.randint(0, 20) for i in range(20)]
print(l)
print( insert_sort(l))
