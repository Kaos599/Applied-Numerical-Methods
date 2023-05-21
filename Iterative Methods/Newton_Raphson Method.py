#IMPORTANT (USAGE INFO)

# Use log fns as log(value, base)
# Use trignometric fns as cos(x) or sin(x) or tan(x)
# To use e as e**x use exp(x)
# To use power use x**y to signify x^y
# To use multiply use x*y to signify xy
# To use divide use x/y


#import neccesary modules
import math as mat
from sympy import *
import sympy as sp
from tabulate import tabulate

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
 
    # Ask the user to choose the value of X(Nought) or not
    custom=input("Do you want to choose the value of X(Nought)? (y or n): ")
    
    # If yes, ask the user to enter the value of X(Nought)
    if custom == 'y':
        x_nought = float(input("X(Nought)= "))
        return x_nought
    
    # If no, ask the user to choose the sign of the root
    elif custom == 'n':
 
        sign = input("Do you want positve root (p) or negative root (n) ?: ")
        print("-"*70)
 
        # Print the function and its derivative
        print("f(x)=",fn_input)
        print("f'(x)=",sp.diff(expr, x))
        
        # If positive root, loop through positive values of x and find where f(x) changes sign
        if sign == "p":
 
            root = [f(i) for i in range(0, 20)]
 
            for j in range(0, 19):
                if (root[j] < 0 and root[j + 1] > 0) or (root[j] > 0 and root[j + 1] < 0) or (root[j] < 0 and root[j + 1] == 0) or (root[j] > 0 and root[j + 1] == 0):
 
                    for k in range(0,j+1):
                        print("Iteration", k, ": f(",k,") gives us", root[k])
                    print("Iteration", j+1, ": f(",j+1,") gives us", root[j+1])
                    print("-"*70)
 
                    print("First value of x =", j, "and it gives us:", root[j])
                    print("Second value of x =", j + 1, "and it gives us:", root[j + 1])
 
                    # Choose the value of X(Nought) based on the absolute values of f(x)
                    if (abs(root[j]) > abs(root[j+1])):
                        x_nought = j+1
                    elif(abs(root[j]) < abs(root[j+1])):
                        x_nought = j
                    else:
                        x_nought = ((j+j+1)/2)
 
                    print("Value of X(Nought) is", x_nought)
 
                    return x_nought
        
        # If negative root, loop through negative values of x and find where f(x) changes sign
        elif sign == "n":
 
            root = [f(i) for i in range(-1, -19, -1)]
 
            for j in range(-1, -19, -1):
                if (root[j] < 0 and root[j - 1] > 0) or (root[j] > 0 and root[j - 1] < 0) or (root[j] < 0 and root[j - 1] == 0) or (root[j] > 0 and root[j - 1] == 0):
 
                    for k in range(-1,j-1,-1):
                        print("Iteration", -k, ": f(",k,") gives us", root[k])
                    print("Iteration", -j+1, ": f(",j-1,") gives us", root[j-1])
                    print("-"*70)
 
                    print("First value of x =", j, "and it gives us:", root[j])
                    print("Second value of x =", j - 1, "and it gives us:", root[j - 1])
 
                    # Choose the value of X(Nought) based on the absolute values of f(x)
                    if (abs(root[j]) > abs(root[j-1])):
                        x_nought = j-1
                    elif(abs(root[j]) < abs(root[j-1])):
                        x_nought = j
                    else:
                        x_nought = ((j+j-1)/2)
 
                    print("Therefore value of X(Nought) is", x_nought)
 
                    return x_nought
        
        # If invalid input, print an error message
        else:
            print("Invalid Input")
    
    # If invalid input, print an error message
    else:
        print("Invalid Input")


# Call the root_calculator function and assign the returned value to x_nought
x_nought = root_calculator()


# Create a symbol for x
x = symbols('x')

# Create a lambda function to evaluate the derivative of the expression for any x
d = lambdify(x, diff(expr,x))

# Initialize a list of lists to store output data
output_data = []

# Initialize a counter variable for counting the iterations
i = 0

# Repeat until convergence is reached
while True:
 
    # Calculate the derivative of the expression at x_nought
    d1 = sp.diff(expr, x)
 
    # Store the previous value of x_nought
    x_nought_previous = x_nought
 
    # Apply the Newton-Raphson formula to get the next value of x_nought
    expr2 = x_nought - expr.subs(x, x_nought)/d1.subs(x, x_nought)
 
    # Round the result to six decimal places
    x_nought = round(expr2, 6)

    # Append a sublist with [x_nought_previous, x_nought, f(x_nought)] to output_data
    output_data.append([x_nought_previous, x_nought, f(x_nought)])
     # Check if convergence is reached by comparing previous and current values of x_nought
    if round(x_nought_previous, 6) == round(x_nought, 6):
 
        # Call tabulate function with output_data and headers as arguments and assign it to table variable
        table = tabulate(output_data, headers=["x_nought_previous", "x_nought", "f(x_nought)"], tablefmt="fancy_grid")

        # Print table variable
        print(table)

        # Print final result
        print("The root is:", x_nought)
        
        # Break out of while loop
        break
 
    # Increment the counter by 1
    i += 1


