import heapq

def min_cost_to_connect_cables(lengths):
    heapq.heapify(lengths)  # Перетворюємо список довжин на купу
    total_cost = 0

    while len(lengths) > 1:
        first = heapq.heappop(lengths)  # Виймаємо найкоротший кабель
        second = heapq.heappop(lengths)  # Виймаємо наступний найкоротший кабель
        cost = first + second
        total_cost += cost
        heapq.heappush(lengths, cost)  # Додаємо об'єднаний кабель назад у купу

    return total_cost

# Приклад використання
cable_lengths = [4, 3, 2, 6]
total_cost = min_cost_to_connect_cables(cable_lengths)
print(total_cost)  
