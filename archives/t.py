def sum_5(l):
    i, j = 0, 4
    s = sum(l[0:5])/5
    sl = [s]
    while j < len(l)-1:
        j += 1
        # print(s,l[j],l[i],(l[j]-l[i])/5)
        
        s += (l[j] - l[i])/5
        i += 1
        sl.append(s)
    return sl


l = [1, 3, 2, 6, -1, 4, 1, 8, 2]
print(sum_5(l))
