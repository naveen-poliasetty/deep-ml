import numpy as np

def activation_derivatives(x: float) -> dict[str, float]:

	sigmoid = 1 / (1 + np.exp(-x))
	d_sigmoid = sigmoid * (1- sigmoid)

	tanh = np.tanh(x)
	tanh_derivative = 1 - tanh**2
	d_r = 1 if x > 0 else 0

	# Your code here
	return {
		"sigmoid":d_sigmoid,
		"tanh": tanh_derivative,
		"relu": d_r
	}