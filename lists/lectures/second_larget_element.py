# Naive solution
def second_largest_element_naive(arr):
    if len(arr) <= 1:
        return None
    else:
        largest = arr[0]
        second = None
        for i in range(1, len(arr)):
            if arr[i] > largest:
                largest = arr[i]
        for i in range(1, len(arr)):
            if arr[i] < largest:
                if second == None:
                    second = arr[i]
                else:
                    second = max(second, arr[i])
    
    return second


# Efficient solution
def second_largest_element_fast(arr):
    lar = arr[0]
    slar = None
    if len(arr) <= 1:
        return None
    
    for i in arr[1:]:
        if i > lar:
            slar = lar
            lar = i
        elif i != lar:
            if slar == None or slar < i:
                slar = i
    
    return slar


print(second_largest_element_fast([1, 2, 3, 4, 5]))
print(second_largest_element_fast([1, 2, 3, 4, 4]))
print(second_largest_element_fast([20, 20, 20]))