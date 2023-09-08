class Sudoku:
    __matrix: list
    __numbers: list

    def __init__(self, matrix: list):
        self.__matrix = matrix
        self.__numbers = [_ for _ in range(1, 10)]

    def __str__(self):
        x = ""
        for i in range(9):
            for j in range(9):
                x += str(self.__matrix[i][j]) + ' '
            x += '\n'
        return x

    def __define_sub_matrix(self, row: int, col: int) -> list:
        row, col = row // 3 * 3, col // 3 * 3
        return [sub_m[col:col + 3] for sub_m in self.__matrix[row:row + 3]]

    def __designate_valid(self, m: list) -> list:
        flattened_m = [item for sublist in m for item in sublist]
        return [item for item in self.__numbers if item not in flattened_m]

    def __solver(self, row: int, col: int):
        if row == 9:
            return True

        if col == 9:
            return self.__solver(row + 1, 0)

        if self.__matrix[row][col] == 0:
            sub_m = self.__define_sub_matrix(row, col)
            sub_valids = self.__designate_valid(sub_m)

            for i in range(len(sub_valids)):
                if self.insert(row, col, sub_valids[i]) and self.__solver(row, col + 1):
                    return True
                self.__matrix[row][col] = 0
            return False

        return self.__solver(row, col + 1)

    def solve(self):
        if not self.__solver(0, 0):
            raise Exception('Impossible to solve')

    def insert(self, row: int, col: int, element: int) -> bool:
        for i in range(9):
            if self.__matrix[row][i] == element or self.__matrix[i][col] == element:
                return False

        self.__matrix[row][col] = element

        return True

    def get_matrix(self):
        return self.__matrix

    def compare(self, sudoku_s: any) -> bool:
        matrix_s = sudoku_s
        if isinstance(matrix_s, Sudoku):
            matrix_s = sudoku_s.get_matrix()

        if len(self.__matrix) != len(matrix_s):
            return False

        for i in range(len(self.__matrix)):
            if self.__matrix[i] != matrix_s[i]:
                return False

        return True
