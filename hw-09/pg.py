def knapSack(W, wt, val, n):
    K = [[0 for w in range(W + 1)] for i in range(n + 1)]
    print(len(K[0]))
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    print(K)
    return K[n][W]

value = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50
n = len(value)
print(knapSack(capacity, weight, value, n))  # 220
