def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}

    for (index, weight) in enumerate(weights):
        cache[weight] = index

    for cur_index, weight in enumerate(weights):
        other_weight = limit - weight
        if other_weight in cache:
            if cur_index > cache[other_weight]:
                return (cur_index, cache[other_weight])
            else:
                return (cache[other_weight], cur_index)
