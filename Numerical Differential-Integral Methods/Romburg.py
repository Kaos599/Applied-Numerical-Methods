from tabulate import tabulate
import numpy as np
from scipy.integrate import romberg
from math import pi, e, log, sin, cos, tan # Import the constants and functions from math module

# Input the expression for the function to be integrated
expr = input("Enter the expression for f(x): ")

# Define the function to be integrated using eval
def f(x):
  return eval(expr)

# Input the lower and upper limits of integration
lower_limit = eval(input("Enter lower limit of integration: "))
upper_limit = eval(input("Enter upper limit of integration: "))

# Input the three values of h
h1 = float((upper_limit - lower_limit) / 2)
h2 = float(h1/2)
h3 = float(h2/2)

# Calculate the number of pairs for each h value
n1 = int((upper_limit - lower_limit) / h1)
n2 = int((upper_limit - lower_limit) / h2)
n3 = int((upper_limit - lower_limit) / h3)

# Generate the x and y values for each h value using np.linspace instead of np.arange
x_values1 = np.linspace(lower_limit, upper_limit, n1 + 1)
y_values1 = np.vectorize(f)(x_values1)
x_values2 = np.linspace(lower_limit, upper_limit, n2 + 1)
y_values2 = np.vectorize(f)(x_values2)
x_values3 = np.linspace(lower_limit, upper_limit, n3 + 1)
y_values3 = np.vectorize(f)(x_values3)

# Display the table for each h value using tabulate
def Table_maker(x_values, y_values):
 data1 = {}
 data1["x"] = x_values
 data1["y"] = ["0" if "e" in str(value) else value for value in y_values]
 print(tabulate(data1, headers="keys", tablefmt="grid"))

print("\nThe table for h = {}".format(h1))
Table_maker(x_values1, y_values1)
print("\nThe table for h = {}".format(h2))
Table_maker(x_values2, y_values2)
print("\nThe table for h = {}".format(h3))
Table_maker(x_values3, y_values3)

# Use romberg function to approximate the integral of the given function
result = romberg(f, lower_limit, upper_limit)

print("\nThe value of the integral using Romberg's method is: {}".format(result))
