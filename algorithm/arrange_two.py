def arrange_two(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
        if arr[left] == 0:
            left += 1
        if arr[right] == 1:
            right -= 1

arr = [0, 1, 1, 1, 0, 0, 0]
print(arr)
arrange_two(arr)
print(arr)