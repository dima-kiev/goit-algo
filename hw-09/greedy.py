def find_coins_greedy(amount, coins):
    result = {}
    for coin in sorted(coins, reverse=True):
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            result[coin] = count
    return result
