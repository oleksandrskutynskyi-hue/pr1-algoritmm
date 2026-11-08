import time
import random



def generate_random_data(size):
    return [random.randint(-10000, 10000) for _ in range(size)]


def method_1_sort(arr):
    data = arr.copy()

    if len(data) <= 10000:
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] < key:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
    else:
        data.sort(reverse=True)
    return data[5]  # 6-й за величиною елемент (індекс 5)



def method_2_top_6_array(arr):

    top6 = sorted(arr[:6], reverse=True)

    for num in arr[6:]:
        if num > top6[-1]:

            for i in range(5):
                if num > top6[i]:
                    top6.insert(i, num)
                    top6.pop()
                    break
    return top6[5]


def method_3_find_max_6_times(arr):
    data = arr.copy()
    sixth_max = None
    for _ in range(6):
        max_val = max(data)
        sixth_max = max_val
        # Замінюємо знайдене максимальне значення на -10 001 (менше за найменше можливе)
        max_idx = data.index(max_val)
        data[max_idx] = -10001
    return sixth_max



def measure_execution_time(method, data):
    start_time = time.perf_counter()
    method(data)
    end_time = time.perf_counter()
    return (end_time - start_time) * 1000


def main():
    sizes = [10_000, 100_000, 1_000_000, 10_000_000, 100_000_000]
    methods = [
        ("Спосіб 1 (Сортування)", method_1_sort),
        ("Спосіб 2 (Масив top-6)", method_2_top_6_array),
        ("Спосіб 3 (Пошук max x6)", method_3_find_max_6_times)
    ]

    print(
        f"{'Розмір вхідних даних':<22} | {'Спосіб 1 (Сортування)':<25} | {'Спосіб 2 (Масив)':<25} | {'Спосіб 3 (Максимальні)':<25}")
    print("-" * 105)

    for size in sizes:

        datasets = [generate_random_data(size) for _ in range(3)]

        row_results = []
        for name, method in methods:
            times = []
            for run_idx in range(3):
                t = measure_execution_time(method, datasets[run_idx])
                times.append(round(t, 2))

            avg_time = round(sum(times) / len(times), 2)
            runs_str = " ".join(str(int(t)) for t in times)
            row_results.append(f"{avg_time}({runs_str})")

        print(f"{size:<22} | {row_results[0]:<25} | {row_results[1]:<25} | {row_results[2]:<25}")


if __name__ == "__main__":
    main()