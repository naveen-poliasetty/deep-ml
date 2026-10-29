import numpy as np

def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	matrix = np.array(matrix)
	det = np.linalg.det(matrix)
	trace = np.diag(matrix).sum()

	return det, trace