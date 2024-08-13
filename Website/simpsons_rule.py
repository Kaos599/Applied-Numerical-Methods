from tabulate import tabulate
import numpy as np
from scipy.integrate import simpson
from math import *

def simpsons_integration(expr, lower_limit, upper_limit, rule, choice, user_input):
    def f(x):
        return eval(expr)
    
    # Determine the step value h and ensure user_input is an integer
    if choice == "pairs":
        h = (upper_limit - lower_limit) / user_input
    elif choice == "h_value":
        h = user_input
        user_input = int((upper_limit - lower_limit) / h)
    
    # Ensure that user_input is an integer before passing to linspace
    user_input = int(user_input)
    x_values = np.linspace(lower_limit, upper_limit, user_input + 1)
    y_values = np.vectorize(f)(x_values)

    # Generate the table
    table_data = {"x": x_values, "y": y_values}
    df = tabulate(table_data, headers="keys", tablefmt="grid")

    # Calculate the integral using Simpson's rule
    if rule == "1/3":
        result = simpson(y_values, x=x_values, even='first')
    elif rule == "3/8":
        result = simpson(y_values, x=x_values, even='last')
    else:
        raise ValueError("Invalid Simpson's rule choice. Please choose '1/3' or '3/8'.")

    return df, result
