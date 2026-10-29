import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    if norm_type == "frobenius":
        return np.linalg.norm(arr, ord='fro')
    arr = np.ravel((arr))
    if norm_type == 'linf':
        return np.linalg.norm(arr, ord=np.inf)
    elif norm_type == 'l1':
        return np.linalg.norm(arr, ord=1)
    else:
        return np.linalg.norm(arr, ord=2)