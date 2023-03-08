def is_list_sorted(arr):
    if len(arr) <= 1:
        return True
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False

    return True


def is_list_sorted(arr):
    l = sorted(arr)
    if arr == l:
        return True
    else:
        return False


print(is_list_sorted([1, 2, 3, 4]))
print(is_list_sorted([1, 3, 2, 4]))
