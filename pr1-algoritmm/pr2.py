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


# Завдання 1: Відняти від елементів кожного рядка матриці середнє арифметичне цього рядка
def subtract_row_average(matrix):
    new_matrix = []
    for row in matrix:
        avg = sum(row) / len(row) if row else 0
        new_row = [round(val - avg, 2) for val in row]
        new_matrix.append(new_row)
    return new_matrix


def cyclic_shift(matrix, k_right, k_up):
    if not matrix or not matrix[0]:
        return matrix

    rows = len(matrix)
    cols = len(matrix[0])


    res = [[0 * cols for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):

            new_i = (i - k_up) % rows
            new_j = (j + k_right) % cols



            pass


    k_right = k_right % cols
    k_up = k_up % rows

    shifted = [row[:] for row in matrix]


    for i in range(rows):
        shifted[i] = shifted[i][-k_right:] + shifted[i][:-k_right]


    shifted = shifted[k_up:] + shifted[:k_up]

    return shifted

def rotate_matrix_90(matrix):
    if not matrix or not matrix[0]:
        return
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()


if __name__ == "__main__":
    print("--- ПР 2: Багатовимірні масиви ---")


    matrix = generate_matrix(3, 3, -5, 15)
    print("Початкова матриця:")
    print_matrix(matrix)

    print("1. Відняти середнє арифметичне рядка:")
    avg_matrix = subtract_row_average(matrix)
    print_matrix(avg_matrix)

    print("4. Обертання матриці на 90 градусів (in-place):")
    rotate_matrix_90(matrix)
    print_matrix(matrix)