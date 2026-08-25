import time


def lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Step 1: Create DP table of size (m+1) x (n+1)
    lcs_table = [[0] * (n + 1) for _ in range(m + 1)]

    # Step 2: Build the table in bottom-up manner
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcs_table[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])

    # Length of LCS is at lcs_table[m][n]
    lcs_length = lcs_table[m][n]

    # Step 3: Backtrack to find the actual LCS string
    lcs_chars = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_chars.append(X[i - 1])
            i -= 1
            j -= 1
        elif lcs_table[i - 1][j] > lcs_table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Reverse the collected characters to get original order
    lcs_string = "".join(reversed(lcs_chars))
    return lcs_length, lcs_string


# Driver Code
if __name__ == "__main__":
    X = input("Enter first string (S1): ").strip()
    Y = input("Enter second string (S2): ").strip()

    # Time measurement
    start_time = time.perf_counter()
    length, subsequence = lcs(X, Y)
    end_time = time.perf_counter()

    print(f"\nLength of LCS: {length}")
    print(f"Longest Common Subsequence: {subsequence}")
    print(f"Time Complexity : O(m * n)")
    print(f"Space Complexity: O(m * n)")
    print(f"Execution Time  : {(end_time - start_time) * 1000:.6f} ms")