# Also known as counter clockwise rotation

# My solution
def left_rotation(arr):
    temp = [None] * len(arr)
    for i in range(0, len(arr)):
        if i == 0:
            temp[len(arr) - 1] = arr[i]
        else:
            temp[i - 1] = arr[i]
    
    return temp


# Example solution
def left_rotation(arr):
    n = len(arr)
    x = arr[0]

    for i in range(1, n):
        arr[i - 1] = arr[i]
    
    arr[n - 1] = x

    return arr


# Direct methods...

# Slicing
def left_rotation(arr):
    return arr[1:] + arr[:1]


# Pop
def left_rotation(arr):
    arr.append(arr.pop(0))
    return arr


print(left_rotation([1, 2, 3, 4]))