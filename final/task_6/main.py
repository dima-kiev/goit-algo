def greedy_algorithm(items, budget):
    # Обчислюємо співвідношення калорій до вартості і сортуємо за спаданням
    item_ratios = [(name, item["calories"] / item["cost"], item["cost"], item["calories"]) for name, item in items.items()]
    item_ratios.sort(key=lambda x: x[1], reverse=True)

    total_cost = 0
    total_calories = 0
    selected_items = []

    for name, ratio, cost, calories in item_ratios:
        if total_cost + cost <= budget:
            selected_items.append(name)
            total_cost += cost
            total_calories += calories

    return selected_items, total_calories, total_cost

def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(item_names)
    dp = [0] * (budget + 1)  # dp[j] - максимальні калорії для бюджету j
    item_choice = [[False] * (budget + 1) for _ in range(n)]
 
    for i in range(n):
        cost = items[item_names[i]]["cost"]
        calories = items[item_names[i]]["calories"]
        for j in range(budget, cost - 1, -1):
            if dp[j - cost] + calories > dp[j]:
                dp[j] = dp[j - cost] + calories
                item_choice[i][j] = True

    # Знаходження вибраних страв
    selected_items = []
    w = budget
    for i in range(n - 1, -1, -1):
        if item_choice[i][w]:
            selected_items.append(item_names[i])
            w -= items[item_names[i]]["cost"]
    
    total_cost = budget - w  # витрачений бюджет

    return selected_items, dp[budget], total_cost

def main():
    # Приклад використання
    items = {
        "pizza": {"cost": 50, "calories": 300}, # 6 калорій за один долар
        "hamburger": {"cost": 40, "calories": 250}, # 6.25 калорій за один долар
        "hot-dog": {"cost": 30, "calories": 200}, # 6.667 калорій за один долар
        "pepsi": {"cost": 10, "calories": 100}, # 10 калорій за один долар
        "cola": {"cost": 15, "calories": 220}, # 14.67 калорій за один долар
        "potato": {"cost": 25, "calories": 350} # 14 калорій за один долар
    }

    budget = 100
 
    selected_items, total_calories, total_cost = greedy_algorithm(items, budget)
    print(f"Жадібний алгоритм - Вибранні страви: {selected_items}")
    print(f"Загальні калорії: {total_calories}")
    print(f"Загальна вартість: {total_cost}")
 
    selected_items, total_calories, total_cost = dynamic_programming(items, budget)
    print(f"Динамічне програмування - Вибранні страви: {selected_items}")
    print(f"Загальні калорії: {total_calories}")
    print(f"Загальна вартість: {total_cost}")

if __name__ == "__main__":
    main()