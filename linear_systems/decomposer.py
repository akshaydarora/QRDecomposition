from .utils.decompose_utils import Decomposer

def decompose(method_name,method_type,constraint_matrix):   

    decomposed_result={}
    dec=Decomposer(method_name = method_name,method_type=method_type, constraint_matrix= constraint_matrix)
    decomposed=dec.getDecomposeResult()  
    decomposed_result["Q"]=decomposed[0]
    decomposed_result["R"]=decomposed[1]
    
    return decomposed_result 

