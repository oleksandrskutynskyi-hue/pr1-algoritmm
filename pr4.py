
def print_1_to_n(n):
    if n < 1:
        return
    print_1_to_n(n - 1)
    print(n, end=" ")


def print_a_to_b(a, b):
    print(a, end=" ")
    if a == b:
        return
    if a < b:
        print_a_to_b(a + 1, b)
    else:
        print_a_to_b(a - 1, b)



def is_power_of_two(n):
    if n == 1:
        return "YES"
    if n < 1 or n % 2 != 0:
        return "NO"
    return is_power_of_two(n // 2)



def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)



def digits_right_to_left(n):
    print(n % 10, end=" ")
    if n // 10 > 0:
        digits_right_to_left(n // 10)


def digits_left_to_right(n):
    if n // 10 > 0:
        digits_left_to_right(n // 10)
    print(n % 10, end=" ")


if __name__ == "__main__":
    print("--- ПР 4: Рекурсія ---")

    print("\n1. Від 1 до 5:")
    print_1_to_n(5)
    print()

    print("\n2. Від 5 до 1:")
    print_a_to_b(5, 1)
    print()

    print(f"\n3. Степінь двійки для 8: {is_power_of_two(8)}")
    print(f"3. Степінь двійки для 3: {is_power_of_two(3)}")

    print(f"\n4. Сума цифр числа 179: {sum_of_digits(179)}")

    print("\n5. Цифри числа 179 справа наліво:")
    digits_right_to_left(179)
    print()

    print("\n6. Цифри числа 179 зліва направо:")
    digits_left_to_right(179)
    print()