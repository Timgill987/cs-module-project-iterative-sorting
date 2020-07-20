def linear_search(arr, target):
    # Your code here
    for j in range(0, len(arr)):
        if arr[j] == target:
            return j
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    l = 0
    h = len(arr) - 1

    while l <= h:
        m = (l + h) // 2
        g = arr[m]
        if g == target:
            return m
        if g > target:
            h = m - 1
        else:
            l = m + 1

    return -1  # not found
