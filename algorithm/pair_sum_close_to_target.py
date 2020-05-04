def pair_sum_close_to_target(arr, target_sum):
    left, right = 0, len(arr) - 1
    
    temp_min = abs(arr[left] + arr[right] - target_sum)
    result_list=[]
    while left<right:
        if abs(arr[left] + arr[right]-target_sum) <= temp_min:
            temp_min = abs(arr[left] + arr[right]-target_sum)
            result_list.append([arr[left],arr[right]])
        if arr[left] + arr[right] < target_sum:
            left += 1
        else:
            right -= 1
            
    return result_list        


arr = [ -2,0, 1,3]
print(pair_sum_close_to_target(arr, 1))
