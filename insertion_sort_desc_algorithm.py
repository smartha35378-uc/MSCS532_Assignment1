def insertion_sort_desc(arr):
    # This Algorithm 3 4Sorts arr in monotonically decreasing order
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1

        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i -= 1

        arr[i + 1] = key
    return arr


if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    data = list(map(int, user_input.split()))

    print("Original Array:", data)
    insertion_sort_desc(data)
    print("Sorted Array(decreasing):", data)
