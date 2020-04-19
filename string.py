s = ''


def substr(s, l):
    li = []
    N = len(s)
    if l != 0:    
        for i in range(N-l+1):
            li.append(s[i:i + l])
    

    return li


def overlap(l):

    isTrue = False
    for i in l:
        if len(set(i)) == len(i):
            isTrue = True
            break
    return isTrue


def main(s):
    str_len = len(s)
    ring = sorted(list(range(0,str_len+1)),reverse=True)
    
    answer = 0
    for i in ring:
        if overlap(substr(s, i)):
            answer = i
            break
    return answer

print(main(s))
