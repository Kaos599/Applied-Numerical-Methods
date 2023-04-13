import math as mat
from sympy import *

def root_calculator():
    x = symbols('x')  # define the symbolic variable x
    fn_input = input("Enter the function: ") 
    global expr
    expr = sympify(fn_input)  # convert the input string into a SymPy expression
    f = lambdify(x, expr)  # convert the expression into a callable function
    root = [f(i) for i in range(0, 20)]  # evaluate the function for values from 0 to 19
    for j in range(0, 19):  # iterate over the range from 0 to 18
        if (root[j] < 0 and root[j + 1] > 0) or (root[j] > 0 and root[j + 1] < 0):  # check if the sign changes between j and j + 1
            print("First value of x =", j, "and it gives us:", root[j])  # print the first value of x and the function
            print("Second value of x =", j + 1, "and it gives us:", root[j + 1])  # print the second value of x and the function
            global x_nought
            x_nought = ((j+j+1)/2) # find the mid-point between j and j+1 and set it to x_nought
            print("Value of X(Nought) is", x_nought)
           
             # print a space after the word are 
            for k in range(0,j+1): # use a for loop to display previous values with x getting incremented 
                print("Previous values of x =", k, "are", root[k]) #print each previous value with a space after it 
            
            break  # exit the loop


root_calculator() # call the function to find the root and set the value of x_nought

x = symbols('x') # define the symbolic variable x
d = lambdify(x, diff(expr,x)) # define the derivative of the expression using x_nought
while True: # use a while loop to apply the Newton-Raphson method
    x_nought_previous = x_nought # store the value of x_nought before it gets updated
    expr2 = x_nought - (expr.subs(x, x_nought)/d(x_nought)) # apply the Newton-Raphson method to find the new value of x_nought
    x_nought = round(expr2, 4) # round the new value of x_nought to 4 decimal places
    if round(x_nought_previous, 4) == round(x_nought, 4): # check if the new value of x_nought is the same as the previous value to stop the loop
        print("The root is:", x_nought) # print the root
        break
