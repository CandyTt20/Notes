def pair_with_targetsum(arr, k):
    left, right = 0, len(arr) - 1
    results = []
    while left < right:
        if arr[left] + arr[right] < k:
            left += 1
        elif arr[left] + arr[right] > k:

            right -= 1
        else:
            results.append([left, right])
            left += 1
            right -= 1

    return results


def search_triplets(arr):
    triplets = []
    
    # TODO: Write your code here
    arr.sort()
    for index in range(len(arr)):
        temp = pair_with_targetsum(arr, -arr[index])
        for item in temp:
            if index > item[1]:
                triplets_set = [arr[item[0]], arr[item[1]], arr[index]]
                if triplets_set not in triplets:
                    triplets.append(triplets_set)
            elif index < item[0]:
                triplets_set = [arr[index],arr[item[0]], arr[item[1]]]
                if triplets_set not in triplets:
                    triplets.append(triplets_set)
            elif index<item[1] and index>item[0]:
                triplets_set = [arr[item[0]], arr[index], arr[item[1]]]
                if triplets_set not in triplets:
                    triplets.append(triplets_set)
    return triplets


arr = [-5, 2, -1, -2, 3]
print(search_triplets(arr))
