items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(budget, items):
    # Сортуємо страви за співвідношенням калорій/вартості за спадання
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    chosen = {}
    total_cost = 0
    total_calories = 0
    
    for name, data in sorted_items:
        if total_cost + data['cost'] <= budget:
            chosen[name] = 1
            total_cost += data['cost']
            total_calories += data['calories']
    
    return chosen, total_cost, total_calories

def dynamic_programming(budget, items):
    names = list(items.keys())
    costs = [items[name]['cost'] for name in names]
    calories = [items[name]['calories'] for name in names]
    n = len(items)
    
    # dp[i][w] = максимальна калорійність при використанні перших i страв і бюджеті w
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(budget + 1):
            cost = costs[i-1]
            cal = calories[i-1]
            if cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - cost] + cal)
            else:
                dp[i][w] = dp[i-1][w]
    
    # Відновлення вибраних страв
    w = budget
    chosen = {}
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            name = names[i-1]
            chosen[name] = 1
            w -= costs[i-1]
    
    total_cost = sum(items[name]['cost'] for name in chosen)
    total_calories = dp[n][budget]
    
    return chosen, total_cost, total_calories


if __name__ == "__main__":
    # Приклад використання:
    budget = 100

    greedy_result = greedy_algorithm(budget, items)
    dp_result = dynamic_programming(budget, items)

    # Виведення результату жадібного алгоритму
    print("Жадібний алгоритм:")
    print(f"Обрані страви: {greedy_result[0]}")
    print(f"Загальна вартість: {greedy_result[1]}")
    print(f"Загальна калорійність: {greedy_result[2]}")

    # Виведення результату динамічного програмування
    print("\nДинамічне програмування:")
    print(f"Обрані страви: {dp_result[0]}")
    print(f"Загальна вартість: {dp_result[1]}")
    print(f"Загальна калорійність: {dp_result[2]}")