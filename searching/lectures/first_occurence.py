def binary_search(l, x):
    """First occurence of `x` within `l`.
    """
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] < x:
            # Set new lower bound
            low = mid + 1
        elif l[mid] > x:
            # Set new upper bound
            high = mid - 1
        elif l[mid] == x:
            if mid == 0 or l[mid] != l[mid - 1]:
                return mid
            else:
                high = mid - 1
    return -1


arr = [10, 10, 20, 20, 50, 60, 70, 80, 90, 100]
x = 20
val = binary_search(arr, x)
print(val)