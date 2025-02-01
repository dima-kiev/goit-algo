import random
import pandas as pd

def simulate_dice_rolls(num_rolls):
    sums = [0] * 11  # Для зберігання кількості разів, коли кожна сума (від 2 до 12) з'являється
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        sums[total - 2] += 1  # Оновлюємо кількість випадків для суми `total`
    
    probabilities = [count / num_rolls * 100 for count in sums]  # У відсотках
    return probabilities

def compare_with_analytical(probabilities):
    # Аналітичні ймовірності
    analytical_probabilities = [
        1/36 * 100, 2/36 * 100, 3/36 * 100, 4/36 * 100, 5/36 * 100, 6/36 * 100, 
        5/36 * 100, 4/36 * 100, 3/36 * 100, 2/36 * 100, 1/36 * 100
    ]
    sums = list(range(2, 13))
    
    # Створення DataFrame для таблиці
    df = pd.DataFrame({
        'Сума': sums,
        'Ймовірність (Монте-Карло) (%)': probabilities,
        'Ймовірність (Аналітична) (%)': analytical_probabilities
    })

    # Виведення таблиці
    print(df.to_markdown(index=False))

def main():
    num_rolls = 100000  # Велика кількість ітерацій для точності
    probabilities = simulate_dice_rolls(num_rolls)
    
    print("Ймовірності кожної суми (Метод Монте-Карло):")
    compare_with_analytical(probabilities)

if __name__ == "__main__":
    main()