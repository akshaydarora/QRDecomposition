import numpy as np
from numpy import linalg
from linear_systems.matrix import Matrix

class LeastSquares(Matrix): 

    def __init__(self,method_type,method_name,constraint_matrix,decomposed,rhs_matrix):

        Matrix.__init__(self,constraint_matrix)
        self.method_type=method_type
        self.method_name=method_name
        self.constraint_matrix=np.array(constraint_matrix)
        self.decomposed=decomposed
        self.rhs_matrix=np.array(rhs_matrix)


    def getLeastSquares(self):

        Q=self.decomposed["Q"]
        R=self.decomposed["R"]
        QTB=Q.T@self.rhs_matrix
        x_lcs=linalg.solve(R, QTB)
        return x_lcs
    

    def getLeastSquaresNorm(self,x_lcs):
        
        # Compute ||AX-B||
        x_lcs_norm=linalg.norm(self.constraint_matrix.dot(x_lcs)-self.rhs_matrix, 2)
        return x_lcs_norm