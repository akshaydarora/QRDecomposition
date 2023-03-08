import numpy as np
from numpy import linalg
from linear_systems.matrix import Matrix

class Decomposer(Matrix):

    def __init__(self,method_name,method_type,constraint_matrix)-> None:
        
        Matrix.__init__(self,constraint_matrix)
        self.method_name=method_name
        self.method=method_type
        self.n=self.metadata["matrix_rows"]
        self.m=self.metadata["matrix_cols"]
        self.constraint_matrix=np.array(constraint_matrix)
        self.rank=linalg.matrix_rank(constraint_matrix)

    def getDecomposeResult(self):
        # Gram-Schmidt Method
        if self.rank<self.m:
            raise Exception("rank is smaller than columns")
        Q= np.zeros((self.n,self.m))
        for i, col in enumerate(self.constraint_matrix.T):
            Q[:,i]=col
            for prev in Q.T[:i]:
                Q[:,i]-=(prev@col)/(prev@prev)*prev
        Q=Q/(linalg.norm(Q,axis=0))
        R=Q.T@self.constraint_matrix

        return Q,R
    
            