from .utils.least_square_utils import LeastSquares

def get_least_squares(method_name,method_type,constraint_matrix,decomposed,rhs_matrix):   
    ls=LeastSquares(method_name = method_name,method_type=method_type,
                     constraint_matrix=constraint_matrix,decomposed=decomposed,rhs_matrix=rhs_matrix)
    least_squares=ls.getLeastSquares() 
    least_squares_norm=ls.getLeastSquaresNorm(least_squares) 
    return least_squares,least_squares_norm
