def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    x = x0
    for i in range(steps):
        x = x - lr * (2 * a * x + b) #trzeba pochodna sobie wziac, ogolnie to ciekawe jak mialbym to policzyc
    return float(x)