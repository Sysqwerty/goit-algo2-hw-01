def min_max(array=[]):
    if len(array) == 0:
        return None

    if len(array) == 1:
        return array[0], array[0]

    mid = len(array) // 2
    left_min, left_max = min_max(array[:mid])
    right_min, right_max = min_max(array[mid:])

    return min(left_min, right_min), max(left_max, right_max)


if __name__ == "__main__":
    print(min_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(min_max([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(
        min_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    )
    print(min_max([5, -7, 9, 45, -13, 28, 0, -15, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]))
    print(min_max([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))
    print(min_max([]))
    print(min_max())
    print(min_max([1, 3, 2]))
