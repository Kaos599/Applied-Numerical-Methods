#IMPORTANT (USAGE INFO)

# Use log fns as log(value, base)
# Use trignometric fns as cos(x) or sin(x) or tan(x)
# To use e as e**x use exp(x)
# To use power use x**y to signify x^y
# To use multiply use x*y to signify xy
# To use divide use x



# Importing the required modules
from tabulate import tabulate
import numpy as np
from scipy.integrate import simpson
from math import *

# Input the expression for the function to be integrated
expr = input("Enter the expression for f(x): ")

# Define the function to be integrated using eval
def f(x):
  return eval(expr)

# Input the lower and upper limits of integration
lower_limit = eval(input("Enter lower limit of integration: "))
upper_limit = eval(input("Enter upper limit of integration: "))

# Ask the user which Simpson's rule they want to use
rule = input("Which Simpson's rule do you want to use? (1/3 or 3/8): ")

# Ask the user if they want to input the number of pairs or the step value h
choice = input("Do you want to input the number of pairs or the step value h? (p/h): ")

if choice == "p":
  # Input the number of pairs
  user_input = int(input("Enter number of pairs: "))
  # Check if the number of pairs is even, otherwise Simpson's method cannot be used
  if user_input % 2 != 0:
    print("Invalid number of pairs. Please enter an even number.")
    exit()
  # Calculate the step value
  h = (upper_limit - lower_limit) / user_input
elif choice == "h":
  # Input the step value
  h = float(input("Enter the step value h: "))
  # Calculate the number of pairs
  user_input = int((upper_limit - lower_limit) / h)
  # Check if the number of pairs is even, otherwise Simpson's method cannot be used
  if user_input % 2 != 0:
    print("Invalid step value. Please enter a value that results in an even number of pairs.")
    exit()
else:
  print("Invalid choice. Please enter p or h.")
  exit()

# Generate the x and y values using np.linspace instead of np.arange
x_values = np.linspace(lower_limit, upper_limit, user_input + 1)
y_values = np.vectorize(f)(x_values)

# Display the table using tabulate
def Table_maker(x_values, y_values):
  data1 = {}
  data1["x"] = x_values
  data1["y"] = y_values
  print(tabulate(data1, headers="keys", tablefmt="grid"))

Table_maker(x_values, y_values)

# Calculate the integral using the chosen Simpson's rule
if rule == "1/3":
  if user_input % 2 != 0:
    print("Invalid number of pairs for Simpson's 1/3 rule. Please enter an even number.")
    exit()
  result = simpson(y_values, x=x_values, even='first')
elif rule == "3/8":
  if user_input % 3 != 0:
    print("Invalid number of pairs for Simpson's 3/8 rule. Please enter a number divisible by 3.")
    exit()
  result = simpson(y_values, x=x_values, even='last')
else:
  print("Invalid rule choice. Please enter 1/3 or 3/8.")
  exit()

print("\nThe value of the integral using Simpson's {} rule is: {}".format(rule, result))
