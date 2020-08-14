def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}

    for (index, weight) in enumerate(weights):
        cache[weight] = index

    for weight in weights:
        other_weight = limit - weight
        if other_weight in cache:
            if cache[weight] > cache[other_weight]:
                return (cache[weight], cache[other_weight])
            elif cache[weight] < cache[other_weight]:
                return (cache[other_weight], cache[weight])

    return None


if __name__ == "__main__":
    print(get_indices_of_item_weights([9], 1, 9))
    print(get_indices_of_item_weights([4, 4], 2, 8))
    print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
