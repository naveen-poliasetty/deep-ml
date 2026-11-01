
import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	vectors = np.array(vectors)
	covar = np.cov(vectors, rowvar=True)
	return covar