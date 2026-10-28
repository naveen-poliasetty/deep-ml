import numpy as np

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    matrix = np.array(matrix)
    try: 
        inv = np.linalg.inv(matrix)
    except np.linalg.LinAlgError:
        return None
    return inv