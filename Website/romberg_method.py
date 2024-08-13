import numpy as np
import pandas as pd
import streamlit as st
from scipy.integrate import romberg
from math import pi, e, log, sin, cos, tan

def romberg_integration(expr, lower_limit, upper_limit):
    def f(x):
        return eval(expr)

    # Define step sizes
    h1 = (upper_limit - lower_limit) / 2
    h2 = h1 / 2
    h3 = h2 / 2

    # Number of intervals
    n1 = int((upper_limit - lower_limit) / h1)
    n2 = int((upper_limit - lower_limit) / h2)
    n3 = int((upper_limit - lower_limit) / h3)

    # Generate x and y values
    x_values1 = np.linspace(lower_limit, upper_limit, n1 + 1)
    y_values1 = np.vectorize(f)(x_values1)
    x_values2 = np.linspace(lower_limit, upper_limit, n2 + 1)
    y_values2 = np.vectorize(f)(x_values2)
    x_values3 = np.linspace(lower_limit, upper_limit, n3 + 1)
    y_values3 = np.vectorize(f)(x_values3)

    # Create dataframes for tables
    df1 = pd.DataFrame({"x": x_values1, "y": y_values1})
    df2 = pd.DataFrame({"x": x_values2, "y": y_values2})
    df3 = pd.DataFrame({"x": x_values3, "y": y_values3})

    # Calculate Romberg integral
    result = romberg(f, lower_limit, upper_limit)

    return df1, df2, df3, result
