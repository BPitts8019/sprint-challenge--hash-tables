def intersection(arrays):
    """
    YOUR CODE HERE
    """
    num_arrays = len(arrays)
    numbers_table = {}
    result = []

    for array in arrays:
        for num in array:
            if num not in numbers_table:
                numbers_table[num] = 1
            else:
                numbers_table[num] += 1

    for (num, num_appearances) in numbers_table.items():
        if num_appearances == num_arrays:
            result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
