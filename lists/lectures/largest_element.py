def largest_element_in_list(arr):

    if not arr:
        return None
    else:
        largest = -1
        for item in arr:
            if item > largest:
                largest = item

    return largest


print(largest_element_in_list([10, 20, 5, 50]))