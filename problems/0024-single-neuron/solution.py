import math
import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	probabilities = []
	for feature in features:
		z = sum(x*w for x, w in zip(feature, weights)) + bias

		probability = 1 / (1 + np.exp(-z))
		probabilities.append(probability)

	mse = sum((prob - actual)**2 for prob, actual in zip(probabilities, labels)) / len(labels)
	probabilities = [round(p, 4) for p in probabilities]
	mse = round(mse, 4)

	return probabilities, mse

