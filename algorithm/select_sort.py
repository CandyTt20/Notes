import random


def select_sort(l):

    for k in range(len(l) - 1):
        for i in range(k, len(l)):
            if l[k] > l[i]:
                l[k], l[i] = l[i], l[k]
    return l


l = [random.randint(0, 20) for i in range(0, 50)]
print(l)
print(select_sort(l))
