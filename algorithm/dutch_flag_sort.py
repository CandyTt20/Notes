def triplet_sort(arr, a, b, c):
    # a<b<c
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
        if arr[left] == a or arr[left] == c:
            left += 1
        if arr[right] == b or arr[right] == c:
            right -= 1
    return

def dutch_flag_sort(arr):
    # TODO: Write your code here
    triplet_sort(arr, 0, 1, 2)
    triplet_sort(arr, 0, 2, 1)
    triplet_sort(arr, 1, 2, 0)
    return 


a = [0, 1, 1, 2, 2, 0, 1, 2, 1]
print(a)
dutch_flag_sort(a)

print(a)
