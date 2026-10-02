import numpy as np

def standard_scaler(X_train: np.ndarray, X_test: np.ndarray) -> np.ndarray:
    x_mean = np.mean(X_train, axis=0)
    x_std = np.std(X_train, axis=0)
    x_std = np.where(x_std == 0, 1, x_std)

    X_test_scaled = (X_test - x_mean) / x_std

    """
    Fit a standard scaler on X_train and transform X_test.
    Returns the standardized X_test as a numpy array.
    """
    return X_test_scaled
