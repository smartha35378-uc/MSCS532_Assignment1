def insertion_sort_desc(arr):
    # This Algorithm Sorts given arr in monotonically decreasing order (largest to smallest)
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1

        # Move elements that are smaller than key to one position ahead
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i -= 1

        arr[i + 1] = key
    return arr


if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]
    print("Original Array:", data)
    insertion_sort_desc(data)
    print("Sorted Array(decreasing):", data)
