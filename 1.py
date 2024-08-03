import heapq

# Основне завдання: Пірамідальне сортування
def heap_sort(arr):
    # Створюємо купу з масиву
    heapq.heapify(arr)
    
    # Витягуємо елементи з купи і формуємо відсортований масив
    sorted_list = [heapq.heappop(arr) for _ in range(len(arr))]
    
    return sorted_list

# Приклад використання пірамідального сортування
array = [5, 2, 9, 1, 5, 6]
sorted_array = heap_sort(array)
print("Відсортований масив:", sorted_array)

# Додаткове завдання: Злиття k відсортованих списків
def merge_k_lists(lists):
    # Створюємо купу
    min_heap = []
    
    # Ініціалізуємо купу з перших елементів кожного списку
    for i, lst in enumerate(lists):
        if lst:  # Перевіряємо, чи список не порожній
            heapq.heappush(min_heap, (lst[0], i, 0))
    
    merged_list = []
    
    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        merged_list.append(value)
        
        # Якщо у списку є ще елементи, додаємо наступний елемент в купу
        if element_index + 1 < len(lists[list_index]):
            next_value = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))
    
    return merged_list

# Приклад використання злиття k відсортованих списків
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
