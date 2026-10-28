import random



def generate_array(length, min_val, max_val):

    return [random.randint(min_val, max_val) for _ in range(length)]



def count_and_sum_even_in_range(arr, start_idx, end_idx):

    start_idx = max(0, start_idx)
    end_idx = min(len(arr) - 1, end_idx)

    even_count = 0
    even_sum = 0

    for i in range(start_idx, end_idx + 1):
        if arr[i] % 2 == 0:
            even_count += 1
            even_sum += arr[i]

    return even_count, even_sum



def elements_greater_than_average(arr):
    if not arr:
        return 0, 0
    avg = sum(arr) / len(arr)
    count = sum(1 for x in arr if x > avg)
    return avg, count



def sum_two_arrays(arr1, arr2):
    return [a + b for a, b in zip(arr1, arr2)]



def concatenate_arrays(arr1, arr2):
    return arr1 + arr2



def swap_min_max(arr):
    if not arr:
        return arr
    res = arr.copy()
    min_val = min(res)
    max_val = max(res)
    min_idx = res.index(min_val)
    max_idx = res.index(max_val)

    res[min_idx], res[max_idx] = res[max_idx], res[min_idx]
    return res


if __name__ == "__main__":
    print("--- ПР 1: Масиви ---")
    my_arr = generate_array(8, -10, 10)
    print(f"Згенерований масив: {my_arr}")

    cnt, sm = count_and_sum_even_in_range(my_arr, 1, 5)
    print(f"1. Парні елементи (індекси 1..5): кількість = {cnt}, сума = {sm}")

    avg, greater_cnt = elements_greater_than_average(my_arr)
    print(f"2. Середнє арифметичне: {avg:.2f}, більших за нього: {greater_cnt}")

    arr_a = [1, 2, 3]
    arr_b = [4, 5, 6]
    print(f"3. Попарна сума: {sum_two_arrays(arr_a, arr_b)}")
    print(f"4. Конкатенація: {concatenate_arrays(arr_a, [7, 8])}")
    print(f"5. Поміняти мін/макс: {swap_min_max(my_arr)}")