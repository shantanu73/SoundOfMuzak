x = [1, 2, 3, 4, 5, 6]

arr1 = [7, 6, 5, 3, 1, 2, 4]
arr1 = [6, 5, 1, 2, 7, 4, 3]


def heapify(arr, n, i):
    # print("WUT")
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        # print("here-1")
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        # print("here-2")
        largest = r

    # Change root, if needed
    if largest != i:
        # print("here-XX")
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build a max-heap.
    print("Build a max-heap:-\n")
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        print(i)
        print(arr)

    # One by one extract elements
    print("\nDo the heap-sort:-\n")
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        print(arr)
        heapify(arr, i, 0)
        print(arr)
        print("\n")


heap_sort(arr1)
