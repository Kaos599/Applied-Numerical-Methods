
#IMPORTANT (USAGE INFO)

# Use log fns as log(value, base)
# Use trignometric fns as cos(x) or sin(x) or tan(x)
# To use e as e**x use exp(x)
# To use power use x**y to signify x^y
# To use multiply use x*y to signify xy
# To use divide use x

import math as mat
from sympy import *
import sympy as sp

# Define a function to create and solve a system of 3 linear equations in 3 variables
def Equation_maker():
    global x, y ,z, f1 ,f2, f3, b1, b2, b3

    # Define symbolic variables x, y, and z using sympy library
    x, y, z = sp.symbols('x y z')

    # Get inputs from the user for the 3 equations and their respective RHS values
    eq1_input = input("Enter the first equation: ")
    eq2_input = input("Enter the second equation: ")
    eq3_input = input("Enter the third equation: ")

    b1 = int(input("Enter the first RHS equation: "))
    b2 = int(input("Enter the second RHS equation: "))
    b3 = int(input("Enter the third RHS equation: "))

    # Convert the equation strings entered by the user into sympy expressions
    eq1 = (sp.sympify(eq1_input))
    eq2 = (sp.sympify(eq2_input))
    eq3 = (sp.sympify(eq3_input))

    # Extract the coefficients of x, y, and z for each equation
    a11 = eq1.coeff(x)
    a12 = eq1.coeff(y)
    a13 = eq1.coeff(z)

    a21 = eq2.coeff(x)
    a22 = eq2.coeff(y)
    a23 = eq2.coeff(z)

    a31 = eq3.coeff(x)
    a32 = eq3.coeff(y)
    a33 = eq3.coeff(z)

    # Print out the matrix of coefficients and RHS values
    print("Our matrix: ")
    print("[",a11,a12,a13,"]","[",b1,"]")
    print("[",a21,a22,a23,"]","[",b2,"]")
    print("[",a31,a32,a33,"]","[",b3,"]\n")

    # First step of Gaussian elimination: transform row 2
    a21_ = -(a21/a11)*a11 + a21
    a22_ = -(a21/a11)*a12 + a22
    a23_ = -(a21/a11)*a13 + a23
    b2_ = -(a21/a11)*b1 + b2

    # Second step of Gaussian elimination: transform row 3
    a32_ = -(a31/a11)*a12 + a32
    a33_ = -(a31/a11)*a13 + a33
    b3_ = -(a31/a11)*b1 + b3
    print("[",a11,a12,a13,"]","[",b1,"]")
    print("[",a21_,a22_,a23_,"]","[",b2_,"]", "R2 --> -(a21/a11)*R1+R2")
    print("[","0",a32_,a33_,"]","[",b3_,"]", "R3 --> -(a31/a11)*R1+R3\n")

   #Third Step: Row 3 transformation 

    a33_=-(a32_/a22_)*a23_+a33_ # calculate the new coefficient for z in the third row
    b3_=-(a32_/a22_)*b2_+b3_ # update the constant value in the third row

    print("[",a11,a12,a13,"]","[",b1,"]")
    print("[",a21_,a22_,a23_,"]","[",b2_,"]")
    print("[","0","0",a33_,"]","[",b3_,"]", "R3 --> -(a32/a22)*R2+R3\n") # print the updated matrix with informative message

    # Solving for the unknowns using back substitution
    # Since we have reduced the system to upper triangular form, we can solve for
    # the unknowns using back substitution starting from the last equation

    # Solving for z using the last equation
    z = b3_ / a33_

    # Solving for y using the second equation and the value of z we just found
    y = (b2_ - a23_ * z) / a22_

    # Solving for x using the first equation and the values of y and z we just found
    x = (b1 - a12 * y - a13 * z) / a11

    # Printing the solution
    print("The solution is: ")
    print("x =", x)
    print("y =", y)
    print("z =", z)

Equation_maker() #calling the function