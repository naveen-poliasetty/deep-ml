import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    rows = data.shape[0]

    gen = np.random.default_rng(seed)
    indices = gen.permutation(rows)

    data = data[indices]
    train_end = int(rows * train_frac)
    val_end = train_end + int(rows * validation_frac)

    train_split = data[:train_end]
    val_split = data[train_end:val_end]
    test_split = data[val_end:]
    
    return [train_split, val_split, test_split]