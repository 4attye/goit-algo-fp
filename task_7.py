import random
import matplotlib.pyplot as plt


# Метод Монте-Карло 
def monte_carlo(num_rolls):
    # Ініціалізуємо словник для зберігання кількості випадків для кожної суми
    counts = {total: 0 for total in range(2, 13)}

    # Виконуємо кидки кубиків
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        counts[total] += 1

    # Обчислюємо ймовірності для кожної суми
    probs = {total: count / num_rolls for total, count in counts.items()}
    return probs

# Функція побудови графіку ймовірностей
def visualization_probs(monte_carlo_probs, analytical_probs):
    sums = list(monte_carlo_probs.keys())
    mc_values = [monte_carlo_probs[s] for s in sums]
    an_values = [analytical_probs[s] for s in sums]

    plt.figure(figsize=(10,6))
    plt.bar([s - 0.2 for s in sums], [m*100 for m in mc_values], width=0.4, label='Монте-Карло', color='skyblue')
    plt.bar([s + 0.2 for s in sums], [a*100 for a in an_values], width=0.4, label='Аналітична', color='salmon')
    plt.xticks(sums)
    plt.xlabel('Сума на кубиках')
    plt.ylabel('Ймовірність %')
    plt.title('Ймовірність сум при киданні двох кубиків')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    num_rolls = 10000

    monte_carlo_probs = monte_carlo(num_rolls)
    analytical_probs = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
    7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

    print(f"{"Сума":^4} | {"Монте-Карло":^16} | {"Аналітична":^16} | {"Різниця":^16}")
    print("-"*61)
    for total in range(2, 13):
        print(f"{total:^4} | {monte_carlo_probs[total]*100:^15.2f}% | {analytical_probs[total]*100:^15.2f}% | {abs(monte_carlo_probs[total] - analytical_probs[total])*100:^15.2f}%")

    visualization_probs(monte_carlo_probs, analytical_probs)