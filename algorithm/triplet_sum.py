def pair_sum_close_to_target(arr, init, target_sum):
    left, right = init, len(arr) - 1

    temp_min = abs(arr[left] + arr[right] - target_sum)
    result_list = []
    while left < right:
        if abs(arr[left] + arr[right]-target_sum) <= temp_min:
            temp_min = abs(arr[left] + arr[right]-target_sum)
            result_list.append([arr[left], arr[right]])
        if arr[left] + arr[right] < target_sum:
            left += 1
        else:
            right -= 1

    return result_list


def triplet_sum_close_to_target(arr, target_sum):
    # TODO: Write your code here
    result_list = []
    i=0
    while i <len(arr)-1:
        temp_list = pair_sum_close_to_target(arr, i+1, target_sum - arr[i])
        for item in temp_list:
            result_list.append([arr[i], item[0], item[1]])
        i += 1
        
    return result_list


arr = [-2, 0, 1, 3]
print(triplet_sum_close_to_target(arr, 1))
