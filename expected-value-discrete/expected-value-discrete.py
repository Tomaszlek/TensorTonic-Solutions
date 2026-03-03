import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    sum = 0
    sum_p = 0
        
    for i in range(len(x)):
        sum += x[i] * p[i]
        sum_p += p[i]
        
    if int(sum_p) != 1:
        raise ValueError('Suma prawdopodobienstw nie wynosi 1, co jest bledem')

    return sum
