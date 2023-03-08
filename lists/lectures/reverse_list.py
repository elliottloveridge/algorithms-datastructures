def reverse_list(arr):
    return arr[::-1]


def reverse_list(arr):
    return arr.reverse()


def reverse_list(arr):
    s = 0
    e = len(arr) - 1
    while s < e:
        arr[s], arr[e] = arr[e], arr[s]
        s = s + 1
        e = e - 1
    
    return arr


print(reverse_list([1, 2, 3, 4]))