def kth_smallest_element(array, k):
    if len(array) < k:
        return None

    pivot = array[len(array) // 2]

    left = [x for x in array if x < pivot]
    right = [x for x in array if x > pivot]

    if len(left) == k - 1:
        return pivot

    if len(left) > k - 1:
        return kth_smallest_element(left, k)

    return kth_smallest_element(right, k - len(left) - 1)


if __name__ == "__main__":
    print(kth_smallest_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
    print(kth_smallest_element([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 5))
    print(kth_smallest_element([0, 3, 2, 1, 4], 2))
    print(kth_smallest_element([5, -7, 9, 45, -13, 28, 0, -15, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 5))
    print(kth_smallest_element([5, -7], 5))
