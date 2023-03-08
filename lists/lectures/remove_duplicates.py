def remove_duplicates(arr):
    arr.sort()
    l = [None] * (len(arr))
    l[0] = arr[0]
    res = 1
    for i in range(1, len(arr)):
        if l[res - 1] != arr[i]:
            l[res] = arr[i]
            res += 1
    return l


print(remove_duplicates([1, 2, 2, 3, 4]))