#IMPORTANT (USAGE INFO)

# Use log fns as log(value, base)
# Use trignometric fns as cos(x) or sin(x) or tan(x)
# To use e as e**x use exp(x)
# To use power use x**y to signify x^y
# To use multiply use x*y to signify xy
# To use divide use x



# Importing the required modules
import math as mat
from sympy import *
import sympy as sp

# Defining a function to find the root of a given function using the fixed point iteration method
def root_calculator():
    
    # Defining a symbol x for the variable
    x = symbols('x')  
    
    # Taking the input of the function from the user
    fn_input = input("Enter the function: ")

    # Converting the input string to a SymPy expression
    global expr, j
    expr = sympify(fn_input)
    
    # Creating a lambda function to evaluate the expression numerically
    f = lambdify(x, expr)  
    
    # Evaluating the expression for x values from 0 to 19 and storing them in a list
    root = [f(i) for i in range(0, 20)]
    # Checking if the input function contains a logarithm
    if("log" in fn_input): # Handling the logarithm case
        for j in range(1, 19):
            if (root[j] < 0 and root[j + 1] > 0) or (root[j] > 0 and root[j + 1] < 0) or (root[j] < 0 and root[j + 1] == 0) or (root[j] > 0 and root[j + 1] == 0):
                
                print("First value of x =", j, "and it gives us:", root[j])
                print("Second value of x =", j + 1, "and it gives us:", root[j + 1])
                x_nought = ((j+j+1)/2)
                print("Value of X(Nought) is", x_nought)
                for k in range(0,j+1):
                    print("Iteration", k, ": x =", k, "gives us", root[k])
                print("Iteration", j+1, ": x =", j+1, "gives us", root[j+1])
                
                return x_nought
    else:   
    # Looping through the list to find an interval where the root lies
        for j in range(0, 19):
            # Checking if there is a sign change or a zero value in the interval
            if (root[j] < 0 and root[j + 1] > 0) or (root[j] > 0 and root[j + 1] < 0) or (root[j] < 0 and root[j + 1] == 0) or (root[j] > 0 and root[j + 1] == 0):
                
                # Printing the values of x and f(x) at the endpoints of the interval
                print("First value of x =", j, "and it gives us:", root[j])
                print("Second value of x =", j + 1, "and it gives us:", root[j + 1])
                
                # Taking the midpoint of the interval as the initial guess for the iteration
                x_nought = ((j+j+1)/2)
                print("Value of X(Nought) is", x_nought)
                
                # Printing the values of x and f(x) for each iteration until the midpoint
                for k in range(0,j+1):
                    print("Iteration", k, ": x =", k, "gives us", root[k])
                print("Iteration", j+1, ": x =", j+1, "gives us", root[j+1])
                
                # Returning the initial guess and the index of the interval
                return x_nought, j
            
# Defining a function to check if the fixed point iteration method is applicable for a given phi function
def eligibility_of_using_FPI():
    
    # Defining a symbol x1 for the variable
    x1 = symbols('x')
    
    # Taking the input of the phi function from the user
    global expr2
    fn_input1 = input("Enter the phi(x) function: ")
    
    # Converting the input string to a SymPy expression
    expr2 = sympify(fn_input1)
    
    # Creating a lambda function to evaluate the expression numerically
    f1 = lambdify(x1, expr2)
    
    # Computing the derivative of the expression symbolically
    d3 = Derivative(expr2, x1)
    
    # Evaluating the derivative at j and j+1 using subs() and Abs()
    d4 = Abs(d3.subs(x1, j))
    d5 = Abs(d3.subs(x1, j+1))
    
    # Checking if the derivative is less than 1 in absolute value at both points
    if ((d4 < 1) | (d5 < 1)):
        print("Iteration method is applicable")
        
        # Setting a global variable T to True to indicate applicability
        global T
        T = true
        
    else:
        print("Iteration method is not applicable")    

# Calling the root_calculator() function and storing its return values in x_nought and j   
x_nought = root_calculator()

# Calling the eligibility_of_using_FPI() function 
f3 = eligibility_of_using_FPI()

# Defining a symbol x for the variable
x = symbols('x')

# Initializing an iteration counter i to 1
i = 1

# Looping while T is True, i.e., while the iteration method is applicable 
while T == true:
    
    
    # Storing the previous value of x_nought in x_nought_previous 
    x_nought_previous = x_nought

     # Substituting x_nought in expr2 and storing it in expr3 
    expr3 = expr2.subs(x, x_nought) 
    
    # Rounding expr3 to 4 decimal places and storing it in x_nought
    x_nought = round(expr3, 4)
    
    # Printing the iteration number and the value of x_nought
    print("Iteration", i, ": x =", x_nought)
    
    # Checking if the previous and current values of x_nought are equal up to 4 decimal places
    if round(x_nought_previous, 4) == round(x_nought, 4):
        
        # Printing the root as x_nought and breaking the loop
        print("The root is:", x_nought)
        break
    
    # Incrementing the iteration counter by 1
    i += 1
