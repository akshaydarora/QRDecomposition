from linear_systems.initializer import Initializer
from linear_systems.decomposer import decompose
from linear_systems.least_square import get_least_squares

if __name__=="__main__":

    #Initialize the Variables
    init=Initializer()
    constraint_matrix,rhs_matrix,method_config,input_config = init.initialize_vars()

    #Initialize the Methods
    method_type = input_config["method_type"]
    method_name = input_config["method_name"]

    # Decompose the Matrix A with the Decomposition Method   
    decomposed = decompose(method_name,method_type,constraint_matrix)
    # print("decomposed result using {0}:{1} method :{2}".format(method_name,method_type,decomposed))

    # Compute the Least Squares and Least Squares Norm
    least_squares, least_squares_norm = get_least_squares(method_type,method_name,
                                                          constraint_matrix,decomposed,rhs_matrix)
    print("least_squares_solution: {0} and least_squares_norm: {1}  using {2}:{3} method".format(least_squares,least_squares_norm,
                                                                                                 method_name,method_type))
    