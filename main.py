import string
import argparse

from Sudoku import Sudoku


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


def init_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Sodoku Solver')
    parser.add_argument('--file', '-f', type=str, help='Nome do arquivo de entrada')
    parser.add_argument('--solution', '-s', type=str, help='Nome do arquivo de solução')
    return parser.parse_args()


if __name__ == "__main__":
    args = init_args()


    def main():
        if args.file:
            matrix: list = create_matrix(read_file(args.file))
            sudoku: Sudoku = Sudoku(matrix)

            sudoku.solve()
            print(sudoku)

            if args.solution:
                matrix_s: list = create_matrix(read_file(args.solution))
                sudoku_s: Sudoku = Sudoku(matrix_s)
                print(f'Solutions equals is: {sudoku_s.compare(sudoku)}')
            return

        print('No input file specified. Use --file or -f to provide the file name.')

    main()
