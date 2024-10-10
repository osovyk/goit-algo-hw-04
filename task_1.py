import timeit
import random

# Функція для генерації випадкового списку
def generate_random_list(size):
    return [random.randint(0, 10000) for _ in range(size)]

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Реалізація Timsort (вбудована функція Python)
def timsort(arr):
    return sorted(arr)

# Функція для вимірювання часу виконання
def measure_time(sort_func, data):
    start_time = timeit.default_timer()
    sort_func(data)
    return timeit.default_timer() - start_time


def main():
    # Генерація даних
    sizes = [1000, 10000, 100000]
    results = {}

    for size in sizes:
        random_list = generate_random_list(size)
        results[size] = {
            "Сортування вставками": measure_time(insertion_sort, random_list.copy()),
            "Сортування злиттям": measure_time(merge_sort, random_list.copy()),
            "Timsort": measure_time(timsort, random_list.copy())
        }

    # Виведення результатів
    for size in sizes:
        print(f"Розмір: {size}")
        for sort_type, time_taken in results[size].items():
            print(f"{sort_type}: {time_taken:.6f} секунд")
        print()

if __name__ == "__main__":
    main()
