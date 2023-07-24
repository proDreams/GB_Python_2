class Matrix:
    def __init__(self, matrix):
        """
        Конструктор класса
        :param matrix: Двумерный список
        """
        self.matrix = matrix

    def print_matrix(self):
        """Выводим матрицу на экран"""
        for row in self.matrix:
            print(*row)

    def __eq__(self, other):
        """
        Сравнение матриц путём сравнения количества строк и размеров столбцов
        :param other: Объект класса Matrix
        :return: Boolean True/False
        """
        if len(self.matrix) != len(other.matrix):
            return False
        for row in range(len(self.matrix)):
            if len(self.matrix[row]) != len(other.matrix[row]):
                return False
        return True

    def __add__(self, other):
        """
        Складывание матриц путём поэлементного сложения.
        Складывать матрицы можно только если количество рядов и столбцов совпадает.
        :param other: Объект класса Matrix
        :return: Новый объект класса Matrix, в случае равенства входных матриц или поднимает ошибку ValueError.
        """
        if self.matrix == other.matrix:
            new_matrix = []
            for row in range(len(self.matrix)):
                new_matrix.append([*map(lambda x: sum(x), zip(self.matrix[row], other.matrix[row]))])
            return Matrix(new_matrix)
        raise ValueError("Матрица неправильного размера")

    def __mul__(self, other):
        """
        Умножение матриц путём поэлементного умножения.
        Умножать матрицы можно только когда количество столбцов первой матрицы совпадает с количеством строк во второй.
        :param other: Объект класса Matrix
        :return: Новый объект класса Matrix, в случае равенства входных матриц или поднимает ошибку ValueError.
        """
        if len(self.matrix[0]) == len(other.matrix):
            new_matrix = [[0 for _ in range(len(other.matrix[0]))] for _ in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    for k in range(len(self.matrix[0])):
                        new_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(new_matrix)
        raise ValueError("Матрица неправильного размера")

    def __pow__(self, power):
        matrix: list = self.matrix.copy()

        for _ in range(power - 1):
            temp = [[0 for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    for k in range(len(self.matrix[0])):
                        temp[i][j] += self.matrix[i][k] * self.matrix[k][j]
            matrix = temp.copy()
        return Matrix(matrix)
