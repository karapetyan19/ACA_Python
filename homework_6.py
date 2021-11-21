
import numpy as np


class Matrix:
    def __init__(self, *args, **kwargs):
        """
        Takes 2 keyword arguments: filename or list. If filename is given
        read the matrix from file. Else, read it directly from list.
        """
        if 'filename' in kwargs:
            self.read_from_file(kwargs['filename'])
        elif 'list' in kwargs:
            self.read_as_list(kwargs['list'])

    def read_as_list(self, matrix_list):
        if len(matrix_list) == 0:
            self._matrix = []
            self._columns = 0
            self._rows = 0
            return

        columns_count_0 = len(matrix_list[0])
        if not all(len(row) == columns_count_0 for row in matrix_list):
            raise ValueError('Got incorrect matrix')

        self._matrix = matrix_list
        self._rows = len(self._matrix)
        self._columns = columns_count_0

    def read_from_file(self, filename):
        with open(filename, 'r') as f:
            rows = f.readlines()
        matrix_list = [[int(r) for r in row.split()] for row in rows]
        self.read_as_list(matrix_list)

    def __str__(self):
        s = '---------MATRIX---------\n'
        s += '\n'.join([str(row) for row in self._matrix])
        s += '\n'
        s += f'colums = {self.shape[0]}\nrows = {self.shape[1]}'
        s += '\n------------------------\n'
        return s

    def write_to_file(self, filename):
        """
        Write the matrix to the given filename.
        """
        rows = [" ".join([str(self._matrix[i][j]) for j in range(self._columns)]) for i in range(self._rows)]
        str_matrix = "\n".join(rows)
        with open(filename, 'w') as f:
          f.write(str_matrix)

    def traspose(self):
        """
        Transpose the matrix.
        """
        C = Matrix(list=[[self._matrix[j][i] for j in range(len(self._matrix))] for i in range(len(self._matrix[0]))])
        return  C 

    @property
    def shape(self):
        return self._columns, self._rows

    def __add__(self, other):
        """
        The `+` operator. Sum two matrices.
        """
        C = Matrix(list=[[0 for col in range(self._columns)] for row in range(self._rows)])
        for i in range(self._rows):
          for j in range(self._columns):
            C._matrix[i][j] = self._matrix[i][j] + other._matrix[i][j]
        return C

    def __mul__(self, other):
        """
        The `*` operator. Element-wise matrix multiplication.
        Columns and rows sizes of two matrices should be the same.
        If other is not a matrix (int, float) multiply all elements of the matrix to other.
        """
        if self._rows != other._rows and self._columns != other._columns:
          return False
        C = Matrix(list=[[0 for col in range(self._columns)] for row in range(self._rows)])
        for i in range(self._rows):
          for j in range(self._columns):
            C._matrix[i][j] = self._matrix[i][j] * other._matrix[i][j]
        return C

    def __matmul__(self, other):
        """
        The `@` operator. Mathematical matrix multiplication.
        The number of columns in the first matrix must be equal to the number of rows in the second matrix.
        """
        if self._columns != other._rows:
          return False

        C = Matrix(list=[[0 for col in range(other._columns)] for row in range(self._rows)])
        for i in range(C._rows):
          for j in range(C._columns):
            acc = 0
            for k in range(self._columns):
              acc += self._matrix[i][k] * other._matrix[k][j]
            C._matrix[i][j] = acc
        return C

    def __getitem__(self, key):
      if isinstance(key, tuple):
        i,j = key[:2]
        return self._matrix[i][j]

    def __setitem__(self, key, value):
      if isinstance(key, tuple):
        i,j = key[:2]
        self._matrix[i][j] = value
    
    @property
    def trace(self):
        """
        Find the trace of the matrix.
        """
        if self._rows != self._columns:
          return False
        return sum(self._matrix[i][i] for i in range(self._rows))

    @property
    def determinant(self):
        """
        Check if the matrix is square, find the determinant.
        """
        if self._rows != self._columns:
          return False

        return np.linalg.det(self._matrix)

