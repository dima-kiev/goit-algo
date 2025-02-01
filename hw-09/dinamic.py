def find_min_coins(amount, coins):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0

    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                if min_coins[i - coin] + 1 < min_coins[i]:
                    min_coins[i] = min_coins[i - coin] + 1
                    coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result
