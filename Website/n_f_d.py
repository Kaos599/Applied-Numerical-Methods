import numpy as np

def coef(x, y):
    n = len(x)
    a = np.copy(y)
    for i in range(1, n):
        for j in range(0, n-i):
            a[j] = a[j+1] - a[j]
        if i < 4:
            a = np.append(a, 0)
    return a

def Eval(a, x, x_values, r, h, order):
    if order == 1:
        p = r
        p1 = p - 0.5
        p2 = p - 1
        if x in x_values:
            return (a[1] - 0.5 * a[2] + (1/3) * a[3] - (1/4) * a[4]) / h
        else:
            return (a[1] + p1 * a[2] + (6 * p2**2 - 6 * p2 + 2) / 12 * a[3]) / h
    elif order == 2:
        p = r
        p1 = p - 1
        if x in x_values:
            return (a[2] - a[3] + (11/12) * a[4]) / (h**2)
        else:
            return (a[2] + p1 * a[3] + (6 * p**2 - 18 * p + 11) / 12 * a[4]) / (h**2)
    elif order == 3:
        p = r
        if x in x_values:
            return (a[3] - (3/2) * a[4]) / (h**3)
        else:
            return (a[3] + (12 * p - 18) / 12 * a[4]) / (h**3)
    else:
        return 0

def newton_forward_difference(x_values, y_values, x_interpolate, order):
    a = coef(x_values, y_values)
    r = (x_interpolate - x_values[0]) / (x_values[1] - x_values[0])
    h = x_values[1] - x_values[0]
    y_interpolate = Eval(a, x_interpolate, x_values, r, h, order)
    return y_interpolate
