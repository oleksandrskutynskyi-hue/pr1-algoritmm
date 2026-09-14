import random


def generate_matrix(rows, cols, min_val, max_val):

    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]


def print_matrix(matrix):

    if not matrix:
        print("Матриця порожня.")
        return

    cols = len(matrix[0])


    header = "          " + "".join(f"стовпець {j + 1:<6}" for j in range(cols))
    print(header)
    print("-" * len(header))


    for i, row in enumerate(matrix):
        row_str = f"рядок {i + 1:<4} " + "".join(f"{val:<12}" for val in row)
        print(row_str)
    print()


def subtract_row_average(matrix):


    new_matrix = []
    for row in matrix:

        avg = sum(row) / len(row) if row else 0

        new_row = [round(val - avg, 2) for val in row]
        new_matrix.append(new_row)
    return new_matrix


if __name__ == "__main__":
    print("Початкова матриця:")

    my_matrix = generate_matrix(4, 3, -10, 10)
    print_matrix(my_matrix)

    print("Результат завдання 3 (Відняти середнє арифметичне рядка):")
    processed_matrix = subtract_row_average(my_matrix)
    print_matrix(processed_matrix)