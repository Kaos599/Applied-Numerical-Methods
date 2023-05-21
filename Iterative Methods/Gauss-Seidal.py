
#IMPORTANT (USAGE INFO)

# Use log fns as log(value, base)
# Use trignometric fns as cos(x) or sin(x) or tan(x)
# To use e as e**x use exp(x)
# To use power use x**y to signify x^y
# To use multiply use x*y to signify xy
# To use divide use x


# Import the necessary modules
import math as mat
from sympy import *
import sympy as sp
from tabulate import tabulate

# Define a function to get the input from the user and return the initial values
def Equation_maker(): 
    # Declare the global variables for the symbols and the functions
    global x, y, z, f1, f2, f3
    # Define the symbols for the variables
    x, y, z = sp.symbols('x y z')

    # Get the input equations from the user
    eq1_input = input("Enter the first equation: ")
    eq2_input = input("Enter the second equation: ")
    eq3_input = input("Enter the third equation: ")

    # Get the right-hand sides of the equations from the user
    b1 = float(input("Enter the first RHS equation: "))
    b2 = float(input("Enter the second RHS equation: "))
    b3 = float(input("Enter the third RHS equation: "))

    # Parse the equations using sympy
    eq1 = (sp.sympify(eq1_input))
    eq2 = (sp.sympify(eq2_input))
    eq3 = (sp.sympify(eq3_input))

    # Extract the coefficients of each variable from each equation
    a11 = eq1.coeff(x)
    a12 = eq1.coeff(y)
    a13 = eq1.coeff(z)

    a21 = eq2.coeff(x)
    a22 = eq2.coeff(y)
    a23 = eq2.coeff(z)

    a31 = eq3.coeff(x)
    a32 = eq3.coeff(y)
    a33 = eq3.coeff(z)

    # Rewrite each equation in terms of one variable using algebra
    f1 = ((b1 - a12 * y - a13 * z) / a11)
    f2 = ((b2 - a21 * x - a23 * z) / a22)
    f3 = ((b3 - a31 * x - a32 * y) / a33)

    # Print the rewritten equations
    print("The equations are:")
    print(f1)
    print(f2)
    print(f3)

    # Return the functions as output
    return f1, f2, f3

# Call the function to create the equations
f1, f2, f3 = Equation_maker()

# Initialize an iteration counter
i = 1

# Initialize an initial guess for each variable
x1 = 0 
y1 = 0 
z1 = 0

# Initialize an empty list to store the output data
output_data = []

# Loop for 20 iterations or until convergence is reached
for i in range(20):
    # Store the previous values of each variable
    x_previous = x1
    y_previous = y1
    z_previous = z1

    # Update each variable using the most recent values of the other variables and round to four decimal places
    x1 = round(float(f1.subs({y: y1, z: z1}).evalf()), 4)
    y1 = round(float(f2.subs({x: x1, z: z_previous}).evalf()), 4)
    z1 = round(float(f3.subs({x: x_previous, y: y_previous}).evalf()), 4)


    # Check if the absolute relative approximate error for each variable is less than 0.0001 (or 0.01%)
    if (
        round(x_previous, 4) == round(x1, 4)
        and round(y_previous, 4) == round(y1, 4)
        and round(z_previous, 4) == round(z1, 4)
    ):
        break

    # Append the current iteration and values of each variable to the output_data list
    output_data.append([i, x1, y1, z1])

# Call tabulate function with output_data and headers as arguments and assign it to table variable
table = tabulate(output_data, headers=["Iteration", "x", "y", "z"], tablefmt="fancy_grid")

# Print table variable
print(table)

