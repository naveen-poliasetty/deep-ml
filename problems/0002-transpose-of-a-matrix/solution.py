import numpy as np
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    arr = np.array(a)
    return arr.T
    