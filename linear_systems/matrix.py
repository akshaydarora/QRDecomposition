import numpy as np

class Matrix(object):


    def __init__(self, matrix) -> None:
        # print(" Initialized a new instance of Matrix :A")
        self.matrix = np.array(matrix)
        self.metadata={
            "matrix_size":self.matrix.shape,
            "matrix_rows":self.matrix.shape[0],
            "matrix_cols":self.matrix.shape[1],
            "matrix_dim":self.matrix.ndim
        }

    def __repr__(self) -> str:
        return f"{type(self).__name__}(metadata={self.metadata})"