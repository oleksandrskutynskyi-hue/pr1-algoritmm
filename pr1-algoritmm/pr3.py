import random


def generate_array(length, min_val, max_val):

    return [random.randint(min_val, max_val) for _ in range(length)]


def print_custom_format(arr):

    formatted_elements = [f"[cell - {i},value - {val}]" for i, val in enumerate(arr)]
    print("{" + ",".join(formatted_elements) + "}")


def bubble_sort(arr, ascending=True):

    n = len(arr)
    res = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if ascending:
                if res[j] > res[j + 1]:
                    res[j], res[j + 1] = res[j + 1], res[j]
            else:
                if res[j] < res[j + 1]:
                    res[j], res[j + 1] = res[j + 1], res[j]
    return res


def insertion_sort(arr, ascending=True):

    res = arr.copy()
    for i in range(1, len(res)):
        key = res[i]
        j = i - 1
        if ascending:
            while j >= 0 and res[j] > key:
                res[j + 1] = res[j]
                j -= 1
        else:
            while j >= 0 and res[j] < key:
                res[j + 1] = res[j]
                j -= 1
        res[j + 1] = key
    return res


def selection_sort(arr, ascending=True):

    n = len(arr)
    res = arr.copy()
    for i in range(n):
        min_max_idx = i
        for j in range(i + 1, n):
            if ascending:
                if res[j] < res[min_max_idx]:
                    min_max_idx = j
            else:
                if res[j] > res[min_max_idx]:
                    min_max_idx = j
        res[i], res[min_max_idx] = res[min_max_idx], res[i]
    return res


if __name__ == "__main__":
    print("--- ПР 3: Прості алгоритми сортування ---")

    original_arr = generate_array(5, -10, 10)
    print("\nПочатковий масив:")
    print_custom_format(original_arr)

    print("\nBubble Sort (Прямий порядок - True):")
    print_custom_format(bubble_sort(original_arr, True))

    print("\nBubble Sort (Зворотний порядок - False):")
    print_custom_format(bubble_sort(original_arr, False))

    print("\nInsertion Sort (Прямий порядок - True):")
    print_custom_format(insertion_sort(original_arr, True))

    print("\nSelection Sort (Зворотний порядок - False):")
    print_custom_format(selection_sort(original_arr, False))