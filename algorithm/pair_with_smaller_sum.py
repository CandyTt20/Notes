def pair_with_smaller_sum(arr, target):
    count = 0
    arr.sort()

    for left in range(len(arr)-1):
        right = len(arr)-1
        while arr[left] + arr[right] >= target and right > left:
            right -= 1
        count += right - left
        
    return count

arr = [-1, 4, 2, 1, 3]
target = 100
print(pair_with_smaller_sum(arr, target))
