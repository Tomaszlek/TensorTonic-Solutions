import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    N = len(y_pred) #zakladam, że beda rownej dlugosci y_pred i y_true

    y_pred = np.array(y_pred, dtype = float)
    y_true = np.array(y_true, dtype = float)

    MSE = 0
    for i in range(N):
        MSE += (y_pred[i] - y_true[i]) ** 2
        
    MSE = MSE * (1/N)
    
    return MSE
