from tabulate import tabulate
import numpy as np
from scipy.integrate import trapezoid

# Input the expression for the function to be integrated
expr = input("Enter the expression for f(x): ")

# Define the function to be integrated using eval
def f(x):
  return eval(expr)

# Input the lower and upper limits of integration
lower_limit = float(input("Enter lower limit of integration: "))
upper_limit = float(input("Enter upper limit of integration: "))

# Ask the user if they want to input the number of pairs or the step value h
choice = input("Do you want to input the number of pairs or the step value h? (p/h): ")

if choice == "p":
  # Input the number of pairs
  user_input = int(input("Enter number of pairs: "))
  # Calculate the step value
  h = (upper_limit - lower_limit) / user_input
elif choice == "h":
  # Input the step value
  h = float(input("Enter the step value h: "))
  # Calculate the number of pairs
  user_input = int((upper_limit - lower_limit) / h)
else:
  print("Invalid choice. Please enter p or h.")
  exit()

# Generate the x and y values using np.linspace instead of np.arange
x_values = np.linspace(lower_limit, upper_limit, user_input + 1)
y_values = f(x_values)

# Display the table using tabulate
def Table_maker(x_values, y_values):
 data1 = {}
 data1["x"] = x_values
 data1["y"] = y_values
 print(tabulate(data1, headers="keys", tablefmt="grid"))

Table_maker(x_values, y_values)

# Use trapezoid function to approximate the integral of the given data
result = trapezoid(y_values, x=x_values)

print("\nThe value of the integral using trapezoidal method is: {}".format(result))
