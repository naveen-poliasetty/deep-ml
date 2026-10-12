import numpy as np

def softmax(scores: list[float]) -> list[float]:
    scores = np.array(scores)
    scores -= np.max(scores)
    return np.exp(scores) / np.sum(np.exp(scores))