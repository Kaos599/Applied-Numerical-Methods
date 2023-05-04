#IMPORTANT (USAGE INFO)

# Use log fns as log(value, base)
# Use trignometric fns as cos(x) or sin(x) or tan(x)
# To use e as e**x use exp(x)
# To use power use x**y to signify x^y
# To use multiply use x*y to signify xy
# To use divide use x



# Import necessary libraries
import math as mat
from sympy import *
import sympy as sp

# Define a function to calculate the root of a user-input function using the bisection method
def root_calculator():
    # Define a symbolic variable x
    x = symbols('x')
    # Prompt the user to enter the function
    fn_input = input("Enter the function: ")
    # Convert the input string to a symbolic expression
    global expr
    expr = sympify(fn_input)
    # Create a lambda function to evaluate the expression
    f = lambdify(x, expr)
    # Calculating the derivative of user-inputed function
    p1 = sp.diff(expr, x)
    #Prompt the user to enter whether they want positive or negative root
    sign = input("Do you want positve root (p) or negative root (n) ?: ")
    print("-"*70)
    # Printing the user-inputed function and its derivative
    print("f(x)=",fn_input)
    print("f'(x)=",p1)
    if sign == "p":
        # Calculate the function value for a range of x values
        root = [f(i) for i in range(0, 20)]
        # Loop through the function values and find two adjacent values that straddle the x-axis
        for j in range(0, 19):
            if (root[j] < 0 and root[j + 1] > 0) or (root[j] > 0 and root[j + 1] < 0) or (root[j] < 0 and root[j + 1] == 0) or (root[j] > 0 and root[j + 1] == 0):
                # Print the function values for each iteration
                for k in range(0,j+1):
                    print("Iteration", k, ": f(",k,") gives us", root[k])
                print("Iteration", j+1, ": f(",j+1,") gives us", root[j+1])
                print("-"*70)
                # Print the two values and their indices
                print("First value of x =", j, "and it gives us:", root[j])
                print("Second value of x =", j + 1, "and it gives us:", root[j + 1])
                # Calculate the x_nought
                if (abs(root[j]) > abs(root[j+1])):
                    x_nought = j+1
                elif(abs(root[j]) < abs(root[j+1])):
                    x_nought = j
                else:
                    x_nought = ((j+j+1)/2)
                # You can change this value by copying 'x_nought = (Value Here)' and deleting the if statement that is calculating the current value of x nought
                print("Value of X(Nought) is", x_nought)
                # Return the midpoint value
                return x_nought
    if sign == "n":
        # Calculate the function value for a range of x values
        root = [f(i) for i in range(-1, -19, -1)]
        # Loop through the function values and find two adjacent values that straddle the x-axis
        for j in range(-1, -19, -1):
            if (root[j] < 0 and root[j - 1] > 0) or (root[j] > 0 and root[j - 1] < 0) or (root[j] < 0 and root[j - 1] == 0) or (root[j] > 0 and root[j - 1] == 0):
                # Print the function values for each iteration
                for k in range(-1,j-1,-1):
                    print("Iteration", -k, ": f(",k,") gives us", root[k])
                print("Iteration", -j+1, ": f(",j-1,") gives us", root[j-1])
                print("-"*70)
                # Print the two values and their indices
                print("First value of x =", j, "and it gives us:", root[j])
                print("Second value of x =", j - 1, "and it gives us:", root[j - 1])
                # Calculate the x_nought
                if (abs(root[j]) > abs(root[j-1])):
                    x_nought = j-1
                elif(abs(root[j]) < abs(root[j-1])):
                    x_nought = j
                else:
                    x_nought = ((j+j-1)/2)
                # You can change this value by copying 'x_nought = (Value Here)' and deleting the if statement that is calculating the current value of x nought
                print("Therefore value of X(Nought) is", x_nought)
                # Return the midpoint value
                return x_nought
    else:
        print("Invalid Input")



# Call the root_calculator function to get the initial value of x_nought
x_nought = root_calculator()

# Define a symbolic variable x
x = symbols('x')
# Create a lambda function to evaluate the derivative of the expression
d = lambdify(x, diff(expr,x))
# Initialize the iteration counter
i = 1
# Implement the Newton-Raphson method to find the root of the expression
while True:
    # Calculate the value of the derivative at x_nought
    d1 = sp.diff(expr, x)
    # Save the current value of x_nought
    x_nought_previous = x_nought
    # Calculate the next value of x_nought using the Newton-Raphson formula
    expr2 = x_nought - expr.subs(x, x_nought)/d1.subs(x, x_nought)
    # Round the value to four decimal places
    x_nought = round(expr2, 6)
    # Print the current value of x_nought and the iteration number
    print("Iteration", i, ": x =", x_nought)
    # Check if the current value of x_nought is the same as the previous value (convergence)
    if round(x_nought_previous, 6) == round(x_nought, 6):
        # If so, print the root and exit the loop
        print("The root is:", x_nought)
        break
    # If not, increment the iteration counter and continue the loop
    i += 1
