import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	scores = np.array(scores)
	result = scores - np.log(np.sum(np.exp(scores)))
	return result