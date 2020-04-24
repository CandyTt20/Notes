def merge_sort(l):
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    left_list = merge_sort(l[0:mid])
    right_list = merge_sort(l[mid:])

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left_list) and right_index < len(right_list):

        if left_list[left_index] <= right_list[right_index]:
            result.append(left_list[left_index])
            left_index += 1
        else:
            result.append(right_list[right_index])
            right_index += 1
    result += left_list[left_index:]
    result += right_list[right_index:]
    return result


l = [3, 5, 2, 7, 8, 4, 9]
print(merge_sort(l))
