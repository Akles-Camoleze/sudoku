import string
import sys
import argparse


def read_file(file_name: string) -> list:
    try:
        with open(file_name, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f'{file} not found.')


def create_matrix(lines: list) -> list:
    m = []
    for ln in lines:
        elements = ln.strip()
        if elements:
            elements = elements.split()
            cast_line = [int(element) for element in elements]
            m.append(cast_line)
    return m


def sudoku(matrix: list):
    def solver(m: list, row: int, col: int):
        if row == 9:
            return True

        if col == 9:
            return solver(m, row + 1, 0)

        if m[row][col] == 0:
            sub_m = define_sub_matrix(m, row, col)
            sub_valids = designate_valid(sub_m)

            for i in range(len(sub_valids)):
                if insert(m, row, col, sub_valids[i]) and solver(m, row, col + 1):
                    return True
                m[row][col] = 0
            return False

        return solver(m, row, col + 1)

    return solver(matrix, 0, 0)


def insert(m: list, row: int, col: int, element: int) -> bool:
    for i in range(9):
        if m[row][i] == element or m[i][col] == element:
            return False

    m[row][col] = element

    return True


def define_sub_matrix(m: list, row: int, col: int) -> list:
    row, col = row // 3 * 3, col // 3 * 3
    return [sub_m[col:col + 3] for sub_m in m[row:row + 3]]


def designate_valid(m: list) -> list:
    numbers: list = [_ for _ in range(1, 10)]
    flattened_m = [item for sublist in m for item in sublist]
    result = [item for item in numbers if item not in flattened_m]
    return result


def show_result(m: list):
    for i in range(9):
        for j in range(9):
            print(m[i][j], end=' ')
        print()


def compare_solution(m1: list, m2: list) -> bool:
    if len(m1) != len(m2):
        return False

    for i in range(len(m1)):
        if m1[i] != m2[i]:
            return False

    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sodoku Solver')
    parser.add_argument('--file', '-f', type=str, help='Nome do arquivo de entrada')
    parser.add_argument('--solution', '-s', type=str, help='Nome do arquivo de solução')
    args = parser.parse_args()

    def main():
        if args.file:
            matrix: list = create_matrix(read_file(args.file))

            if not sudoku(matrix):
                raise Exception('Impossible sudoku.')
            show_result(matrix)

            if args.solution:
                matrix_s: list = create_matrix(read_file(args.solution))
                print(f'Solutions equals is: ${compare_solution(matrix, matrix_s)}')

            return

        print('No input file specified. Use --file or -f to provide the file name.')

    main()
