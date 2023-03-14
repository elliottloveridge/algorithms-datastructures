def binary_search(arr, n, x):
    """My solution for binary search (does not return position)
    """
    # Get midpoint of arr
    mid = n // 2
    # Split arr into left and right
    l, r = arr[:mid], arr[mid:]
    # Update arr as l/r of original arr
    arr = r if l[-1] < x else l
    # Get new len of arr
    n = len(arr)

    # If x value found
    if n == 1:
        if x == arr[0]:
            return arr[0]
        else:
            return -1
    else:
        binary_search(arr, n, x)


def binary_search(l, x, low, high):
    """Recursive binary search implementation.
    """
    if low > high:
        return -1
    
    mid = (low + high) // 2
    if l[mid] == x:
        return mid
    elif l[mid] > x:
        return binary_search(l, x, low, mid -1)
    else:
        return binary_search(l, x, mid + 1, high)


def binary_search(l, x):
    """Iterative binary search implementation.
    """
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == x:
            return mid
        elif l[mid] < x:
            # Set new lower bound
            low = mid + 1
        else:
            # Set new upper bound
            high = mid - 1

    return -1


arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n = 10
x = 80
val = binary_search(arr, n, x)
print(val)