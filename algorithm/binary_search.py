def find(l, flag):
    low = 0
    high = len(l) - 1

    while low <= high:
        mid = (low + high) // 2
        if flag < l[mid]:
            high = mid-1

        elif flag > l[mid]:
            low = mid+1

        else:
            return mid


def find2(l, flag):
    if len(l) == 0:
        return
    mid = len(l) // 2
    if flag > l[mid]:
        find2(l[mid + 1:], flag)
    elif flag < l[mid]:
        find2(l[0:mid], flag)
    else:
        return mid
    return False


l = [5, 17, 19, 20]
print(find2(l, 1))
