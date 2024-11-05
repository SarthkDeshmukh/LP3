def knapsack_dp(value, weight, capacity):
    n = len(value)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weight[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight[i - 1]] + value[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Example usage
value = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50
print(knapsack_dp(value, weight, capacity))
