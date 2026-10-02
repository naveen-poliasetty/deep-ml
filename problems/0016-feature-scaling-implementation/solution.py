import numpy as np
def feature_scaling(x: np.ndarray) -> (np.ndarray, np.ndarray):
	#standarization
	x_mean = np.mean(x, axis=0)
	x_std = np.std(x, axis=0)

	x_min = np.min(x, axis=0)
	x_max = np.max(x, axis=0)

	standardized_data = (x - x_mean) / x_std
	# Min max feature_scaling
	normalized_data = (x - x_min) / (x_max - x_min)
	return (standardized_data, normalized_data)