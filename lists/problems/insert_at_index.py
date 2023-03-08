class Solution:

    def __init__(self):
        pass

    def insert_at_index(self, arr: list, index: int, element: int) -> None:
        """Insert `element` at a given `index` within an array, `arr`, shifting 
        elements to the right by one.

        Args:
            arr (list): an input array
            size_of_array (int): size of array, `arr`
            index (int): index for element insertion
            element (int): integer to insert in array, `arr`
        """
        arr.insert(index, element)

    def insert_at_index_slicing(self, arr: list, size_of_array: int,
                                index: int, element: int) -> None:
        """Custom insert at index module
        """
        # If index == end of arr
        if index == size_of_array - 1:
            arr.insert(size_of_array - 1, element)
        else:
            # Slice before/after index and store
            start, end = arr[:index], arr[index:-1]
            # Insert at end
            start.insert(index - 1, element)
            # Append after index slice
            start.extend(end)
            # Set arr to solution
            arr = start


def main():
    size_of_array = int(input())
    arr = [int(x) for x in input().strip().split()]
    arr.append(-1)
    index, element = map(int, input().strip().split())

    solution = Solution()
    solution.insert_at_index(arr, index, element)

    for i in range(size_of_array):
        print(arr[i], end=" ")
    print()


if __name__ == "__main__":
    main()
