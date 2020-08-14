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
            return (weight, other_weight)

    return None


if __name__ == "__main__":
    print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 32))
