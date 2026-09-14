import random

def generate_array(length, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(length)]


def print_array(arr):
    elements = [f"[cell - {i},value - {val}]" for i, val in enumerate(arr)]
    print("{" + ",".join(elements) + "}")


def bubble_sort(arr, ascending=True):
    n = len(arr)
    # Робимо копію масиву, щоб не змінювати оригінальний, якщо це потрібно
    sorted_arr = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            condition = (sorted_arr[j] > sorted_arr[j + 1]) if ascending else (sorted_arr[j] < sorted_arr[j + 1])
            if condition:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    return sorted_arr

def insertion_sort(arr, ascending=True):
    sorted_arr = arr.copy()
    for i in range(1, len(sorted_arr)):
        key = sorted_arr[i]
        j = i - 1
        while j >= 0 and ((sorted_arr[j] > key) if ascending else (sorted_arr[j] < key)):
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        sorted_arr[j + 1] = key
    return sorted_arr

def selection_sort(arr, ascending=True):
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    for i in range(n):
        extreme_idx = i
        for j in range(i + 1, n):
            condition = (sorted_arr[j] < sorted_arr[extreme_idx]) if ascending else (
                        sorted_arr[j] > sorted_arr[extreme_idx])
            if condition:
                extreme_idx = j
        sorted_arr[i], sorted_arr[extreme_idx] = sorted_arr[extreme_idx], sorted_arr[i]
    return sorted_arr



if __name__ == "__main__":

    original = generate_array(5, -10, 10)

    print("Початковий масив:")
    print_array(original)

    print("\nBubble Sort (Прямий порядок - True):")
    print_array(bubble_sort(original, True))

    print("\nBubble Sort (Зворотний порядок - False):")
    print_array(bubble_sort(original, False))

    print("\nInsertion Sort (Прямий порядок - True):")
    print_array(insertion_sort(original, True))

    print("\nSelection Sort (Зворотний порядок - False):")
    print_array(selection_sort(original, False))