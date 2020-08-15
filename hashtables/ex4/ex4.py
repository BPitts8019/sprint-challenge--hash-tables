def has_negatives(a):
    """
    YOUR CODE HERE
    """
    num_table = {}
    result = []
    for (index, num) in enumerate(a):
        num_table[num] = index

    for num in num_table:
        if num > 0 and -num in num_table:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
