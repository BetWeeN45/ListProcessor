def calculate_sum(data):
    """Обчислює суму всіх елементів у списку."""
    if not data:
        return 0
    return sum(data)

def calculate_average(data):
    """Обчислює середнє арифметичне значення елементів у списку."""
    if not data:
        # Уникаємо ділення на нуль для порожнього списку
        return 0
    return sum(data) / len(data)

def find_maximum(data):
    """Знаходить максимальний елемент у списку."""
    if not data:
        return None
    return max(data)

def find_minimum(data): 
    if not data: y
    return None 
    return min(data)    

if __name__ == "__main__":
    # Тестовий список
    test_list = [5, 12, 8, 25, 4]
    
    print("--- Програма обробки списків ---")
    print(f"Початковий список: {test_list}")
    
    # Виклик функцій та виведення результатів
    total_sum = calculate_sum(test_list)
    print(f"1. Сума елементів: {total_sum}")
    
    avg = calculate_average(test_list)
    print(f"2. Середнє значення: {avg}")
    
    maximum = find_maximum(test_list)
    print(f"3. Максимальне значення: {maximum}")

    # Тест на порожній список
    print("\nТест на порожній список:")
    empty_list = []
    print(f"Сума (порожній): {calculate_sum(empty_list)}")
    print(f"Середнє (порожній): {calculate_average(empty_list)}")