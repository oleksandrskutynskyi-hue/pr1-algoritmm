import random



def generate_array(length, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(length)]



def print_array(arr):
    formatted_elements = [f"[елемент_{i + 1}_значення_{val}]" for i, val in enumerate(arr)]
    print(",\n".join(formatted_elements))



def even_count_and_sum_in_range(arr, min_range, max_range):
    count = 0
    total_sum = 0
    for val in arr:
        if min_range <= val <= max_range and val % 2 == 0:
            count += 1
            total_sum += val
    return count, total_sum



def mean_and_greater_count(arr):
    if not arr:
        return 0, 0
    mean = sum(arr) / len(arr)
    count = sum(1 for val in arr if val > mean)
    return mean, count



def pairwise_sum(arr1, arr2):
    return [a + b for a, b in zip(arr1, arr2)]



def concatenate_arrays(arr1, arr2):
    return arr1 + arr2



def swap_min_max(arr):
    if not arr:
        return arr
    min_val = min(arr)
    max_val = max(arr)
    min_idx = arr.index(min_val)
    max_idx = arr.index(max_val)

    arr[min_idx], arr[max_idx] = arr[max_idx], arr[min_idx]
    return arr



def split_positive_negative(arr):
    positives = [val for val in arr if val > 0]
    negatives = [val for val in arr if val < 0]
    return positives, negatives



def remove_duplicates_min_max(arr):
    if not arr:
        return arr
    min_val = min(arr)
    max_val = max(arr)


    filtered = []
    min_seen = False
    max_seen = False
    for val in arr:
        if val == min_val:
            if not min_seen:
                filtered.append(val)
                min_seen = True
        elif val == max_val:
            if not max_seen:
                filtered.append(val)
                max_seen = True
        else:
            filtered.append(val)
    return filtered



def elements_between_means(arr1, arr2):
    if not arr1 or not arr2:
        return []
    mean1 = sum(arr1) / len(arr1)
    mean2 = sum(arr2) / len(arr2)

    lower = min(mean1, mean2)
    upper = max(mean1, mean2)

    combined = arr1 + arr2
    return [val for val in combined if lower <= val <= upper]



if __name__ == "__main__":
    print("Генерація та виведення масиву:")
    my_array = generate_array(5, -10, 10)
    print_array(my_array)

    print(f"\n1. Парні в діапазоні [-5, 5]: {even_count_and_sum_in_range(my_array, -5, 5)}")

    mean, greater = mean_and_greater_count(my_array)
    print(f"2. Середнє арифметичне: {mean}, Кількість більших: {greater}")

    arr_a = [1, 2, 3]
    arr_b = [4, 5, 6]
    print(f"3. Попарна сума: {pairwise_sum(arr_a, arr_b)}")
    print(f"4. Конкатенація: {concatenate_arrays(arr_a, [7, 8])}")

    print(f"5. Поміняти мін та макс: {swap_min_max(my_array.copy())}")

    pos, neg = split_positive_negative(my_array)
    print(f"6. Додатні: {pos}, Від'ємні: {neg}")