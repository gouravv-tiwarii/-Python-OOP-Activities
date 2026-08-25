from functools import lru_cache


def knapsack_top_down(values, weights, W):
    @lru_cache(maxsize=None)
    def solve(n, w):
        if n == 0 or w == 0:
            return 0
        if weights[n - 1] > w:
            return solve(n - 1, w)
        return max(
            solve(n - 1, w), values[n - 1] + solve(n - 1, w - weights[n - 1])
        )

    return solve(len(values), W)


values, weights, W = [60, 100, 120], [10, 20, 30], 50
print("Max Profit (Top-Down):", knapsack_top_down(values, weights, W))