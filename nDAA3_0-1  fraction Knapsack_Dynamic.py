def fractional_knapsack(value, weight, capacity):
    items = sorted(zip(value, weight), key=lambda x: x[0] / x[1], reverse=True)
    total_value = 0
    for v, w in items:
        if capacity >= w:
            total_value += v
            capacity -= w
        else:
            total_value += v * (capacity / w)
            break
    return total_value

# Example usage
value = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50
print(fractional_knapsack(value, weight, capacity))
