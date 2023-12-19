# personal_assistant/sorter.py

class Sorter:
    @staticmethod
    def sort_list(lst, reverse=False):
        # Сортування списку
        return sorted(lst, reverse=reverse)

# Перевірка роботи модуля при його виклику напряму
if __name__ == "__main__":
    data_to_sort = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    
    sorter = Sorter()
    
    # Сортування за зростанням
    sorted_data = sorter.sort_list(data_to_sort)
    print(f"Sorted (ascending): {sorted_data}")
    
    # Сортування за спаданням
    sorted_data_reverse = sorter.sort_list(data_to_sort, reverse=True)
    print(f"Sorted (descending): {sorted_data_reverse}")