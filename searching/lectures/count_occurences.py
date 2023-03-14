def first_occurence(l, x):
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


def last_occurence(l, x):
    """Last occurence of `x` within `l`.
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
            if mid == (len(l) - 1) or l[mid] != l[mid + 1]:
                return mid
            else:
                low = mid + 1
    return -1


def count_occurence(l, x):
    """Get count of occurence of `x` in `l`.
    """
    first = first_occurence(l, x)
    if first == -1:
        return 0
    else:
        return last_occurence(l, x) - first + 1


l = [10, 20, 20, 20, 30, 30]
x = 20
print(count_occurence(l, x))