def print_1_to_n(n):
    if n < 1:
        return
    print_1_to_n(n - 1)
    print(n, end=" ")

def print_ab(a, b):
    print(a, end=" ")
    if a == b:
        return
    if a < b:
        print_ab(a + 1, b)
    else:
        print_ab(a - 1, b)

def is_power_of_two(n):
    if n == 1:
        return True
    if n < 1 or n % 2 != 0:
        return False
    return is_power_of_two(n // 2)

def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

def print_digits_right_to_left(n):
    print(n % 10, end=" ")
    if n // 10 > 0:
        print_digits_right_to_left(n // 10)

def print_digits_left_to_right(n):
    if n // 10 > 0:
        print_digits_left_to_right(n // 10)
    print(n % 10, end=" ")