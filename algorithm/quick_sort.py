def quick_sort(l, low_index, high_index):
    # if low_index > high_index:
    #     return
    if low_index >= high_index:
        return
    mid_val = l[low_index]
    low = low_index
    high = high_index

    while low < high:
        while low < high and mid_val <= l[high]:
            high -= 1
        l[low] = l[high]

        while low < high and mid_val > l[low]:
            low += 1
        l[high] = l[low]
    l[low] = mid_val

    quick_sort(l, 0, low-1)
    quick_sort(l, low+1, high_index)


l = [4, 5, 2, 7, 3]
quick_sort(l, 0, 4)
print(l)
