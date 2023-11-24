import math as mat
from sympy import *
import sympy as sp
 
def Equation_maker():
    global x, y ,z, f1 ,f2, f3, b1, b2, b3
 
    # Ask the user for the size of the matrix
    size = int(input("Enter the size of the matrix (3 or 4): "))
 
    # Check if the size is valid
    if size not in [3, 4]:
        print("Invalid size. Please enter 3 or 4.")
        return
 
    # Create symbols for the variables
    x, y, z = sp.symbols('x y z')
    if size == 4:
        w = sp.symbols('w') # Add an extra symbol for the fourth variable
 
    # Ask the user for the equations and the RHS values
    eq_input = [] # A list to store the equations
    b = [] # A list to store the RHS values
    for i in range(1, size + 1):
        eq_input.append(input(f"Enter the equation {i}: ")) # Append each equation to the list
        b.append(int(input(f"Enter the RHS value {i}: "))) # Append each RHS value to the list
 
    # Convert the equations to sympy expressions
    eq = [sp.sympify(e) for e in eq_input]
 
    # Extract the coefficients of the variables from each equation
    a = [] # A list to store the coefficients
    for i in range(size):
        row = [] # A list to store the coefficients of each row
        row.append(eq[i].coeff(x)) # Append the coefficient of x
        row.append(eq[i].coeff(y)) # Append the coefficient of y
        row.append(eq[i].coeff(z)) # Append the coefficient of z
        if size == 4:
            row.append(eq[i].coeff(w)) # Append the coefficient of w if size is 4
        a.append(row) # Append the row to the list of coefficients
 
    # Print the matrix and the RHS values
    print("Our matrix: ")
    for i in range(size):
        print("[", end="") # Print an opening bracket
        for j in range(size):
            print(a[i][j], end=" ") # Print each coefficient with a space
        print("]", end="") # Print a closing bracket
        print("[", b[i], "]") # Print the RHS value with brackets
 
    print() # Print a newline
 
    # Perform Gaussian elimination to reduce the matrix to upper triangular form
    for i in range(size - 1): # Loop over each pivot row except the last one
        for j in range(i + 1, size): # Loop over each row below the pivot row
            factor = -(a[j][i] / a[i][i]) # Compute the factor to eliminate the coefficient below the pivot
            for k in range(i, size): # Loop over each column from the pivot column onwards
                a[j][k] = factor * a[i][k] + a[j][k] # Update the coefficient by adding the product of the factor and the pivot row coefficient
            b[j] = factor * b[i] + b[j] # Update the RHS value by adding the product of the factor and the pivot row RHS value
 
            # Print the matrix and the RHS values after each elimination step
            print(f"After eliminating a[{j}][{i}]:")
            for m in range(size):
                print("[", end="")
                for n in range(size):
                    print(a[m][n], end=" ")
                print("]", end="")
                print("[", b[m], "]")
 
            print() # Print a newline
 
    # Perform back substitution to solve for each variable
    solution = [] # A list to store the solution values
    for i in range(size - 1, -1, -1): # Loop over each row from bottom to top
        value = b[i] # Start with the RHS value of that row
        for j in range(i + 1, size): # Loop over each column from right to left except the diagonal element
            value -= a[i][j] * solution[size - j - 1] # Subtract the product of the coefficient and the already solved variable from the value
        value /= a[i][i] # Divide the value by the diagonal element of that row
        solution.append(value) # Append the value to the solution list
 
    # Reverse the solution list to match the order of the variables
    solution.reverse()
 
    # Print the solution
    print("The solution is: ")
    print("x =", solution[0])
    print("y =", solution[1])
    print("z =", solution[2])
    if size == 4:
        print("w =", solution[3]) # Print the fourth variable if size is 4
 
Equation_maker()
