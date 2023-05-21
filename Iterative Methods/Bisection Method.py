
"""
a and b are the endpoints of the interval that contains the root of the function. They are initialized with the given values and updated in each iteration depending on which subinterval contains the root.
t is the midpoint of the interval [a, b]. It is calculated as (a + b) / 2 in each iteration. It is an approximation of the root of the function.
f(t) is the value of the function at t. It is calculated by calling the function f(x) with x = t. It is used to check if t is close to the root or not. If f(t) is close to zero, then t is a good approximation of the root. If f(t) is not close to zero, then t is not a good approximation of the root.
"""


# Import the neccessary modules
import math as mat
from sympy import *
import sympy as sp
from tabulate import tabulate

# Define a function to get the input from the user and return the initial values
def root_calculator():
 
    # Create a symbol for x
    x = symbols('x')
 
    # Ask the user to enter the function
    fn_input = input("Enter the function: ")
 
    # Convert the input string to a sympy expression
    global expr
    expr = sympify(fn_input)
 
    # Create a lambda function to evaluate the expression for any x
    global f 
    f = lambdify(x, expr) 
 
    # Ask the user to enter the lower bound of the interval that contains the root
    a = float(input("Enter the lower bound of the interval: "))
 
    # Ask the user to enter the upper bound of the interval that contains the root
    b = float(input("Enter the upper bound of the interval: "))
 
    # Print a separator line
    print("-"*70)
 
    # Print the function entered by the user
    print("f(x)=",fn_input)
 
    # Define the tolerance value for stopping the loop
    tolerance = 1e-6 
 
    # Return the initial values of a, b, and tolerance
    return a, b, tolerance

# Call the root_calculator function and assign the returned values to a, b, and tolerance
a, b, tolerance = root_calculator()

# Create a symbol for x
x = symbols('x')

# Define another tolerance value (this seems redundant since we already have one from root_calculator)
tolerance = 1e-4

# Initialize a list of lists to store the output data
output_data = []

# Initialize the counter variable for counting the iterations
i = 0

# Repeat until f(t) is close to zero
while True:
 
    # Find the midpoint of [a, b]
    t = (a + b) / 2
 
    # Increment the counter by 1
    i += 1
 
    # Append a sublist with [a, b, t, f(t)] to output_data
    output_data.append([i, a, b, t, f(t)])
 
    # Check if f(t) is close to zero
    if abs(f(t)) < tolerance:
 
        # Break the loop and print a separator line
        print("-"*70)
        
        # Print a message with final result
        print("The root is:", t)
        
        # Break out of while loop
        break
 
    # Check which subinterval contains the root
    if f(t) * f(a) < 0:
        # Root is in left subinterval, update b with t
        b = t
    else:
        # Root is in right subinterval, update a with t
        a = t

# Call tabulate function with output_data and headers as arguments and assign it to table variable
table = tabulate(output_data, headers=["Interation Number","a", "b", "t", "f(t)"], tablefmt="fancy_grid")

# Print table variable
print(table)
