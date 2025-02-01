import time
import pandas as pd

from greedy import find_coins_greedy
from dinamic import find_min_coins


def measure_time(func, amount, coins):
    start_time = time.time()
    result = func(amount, coins)
    end_time = time.time()
    return end_time - start_time, result


def main():
    coins = [50, 25, 10, 5, 2, 1]

    amount = 113
    print("Greedy Algorithm:", find_coins_greedy(amount, coins))
    print("Dynamic Programming:", find_min_coins(amount, coins))
    print("-" * 50)

    amounts = [138, 1038, 10038, 100038]
    results = {
        "Amount": [],
        "Greedy Time": [],
        "DP Time": [],
        "Greedy Result": [],
        "DP Result": []
    }
    for amount in amounts:
        greedy_time, greedy_result = measure_time(find_coins_greedy, amount, coins)
        dp_time, dp_result = measure_time(find_min_coins, amount, coins)
        results["Amount"].append(amount)
        results["Greedy Time"].append(greedy_time)
        results["DP Time"].append(dp_time)
        results["Greedy Result"].append(greedy_result)
        results["DP Result"].append(dp_result)

    df = pd.DataFrame(results)
    print(df.to_markdown(index=False))


if __name__ == "__main__":
    main()
