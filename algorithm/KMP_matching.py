def gen_next(p):
    i, j = -1, 0
    next = [-1] * len(p)

    while j <= len(p)-2:
        if i == -1 or p[i] == p[j]:
            i += 1
            j += 1
            next[j] = i
        else:
            i = next[i]
    return next


# print(gen_next('abbcabcaabbcaa'))




def KMP_matching(t, p):
    next = gen_next(p)
    i, j = 0, 0
    while i<len(p) and j<len(t):
        if i==-1 or p[i] == t[j]:
            i += 1
            j += 1
        else:
            i = next[i]
    if i > len(p) - 1:
        return j - i
    else:
        return -1

t = 'ababcabcacbab'
p = 'abcac'
print(KMP_matching(t,p))