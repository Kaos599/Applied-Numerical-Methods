
#IMPORTANT (USAGE INFO)

# Use log fns as log(value, base)
# Use trignometric fns as cos(x) or sin(x) or tan(x)
# To use e as e**x use exp(x)
# To use power use x**y to signify x^y
# To use multiply use x*y to signify xy
# To use divide use x


# import the tabulate module
import numpy as np
from tabulate import tabulate

#defining function coef(x,y)
def coef(x, y):
    # Compute the finite divided differences and store them in a
    # one-dimensional array
    n = len(x)
    a = np.copy(y) # Initialize the array with y values
    for i in range(1, n):
        for j in range(n-1, i-1, -1):
            a[j] = (a[j] - a[j-1]) / (x[j] - x[j-i]) # Compute the divided differences
    return a # Return the array of coefficients

#defining function Eval(a,x,r)
def Eval(a, x, r):
    # Evaluate the polynomial using Horner's method
    n = len(a) - 1
    p = a[n]
    for i in range(n-1, -1, -1):
        p = a[i] + (r - x[i]) * p # Update the polynomial value
    return p # Return the interpolated value


def Table_maker(x_values, y_values):
    # creating an empty dictionary to store the data
    data1 = {}

    # adding the x_values and y_values lists to the data dictionary with keys "x" and "y"
    data1["x"] = x_values
    data1["y"] = y_values

    # printing the data dictionary as a table using tabulate
    print(tabulate(data1, headers="keys", tablefmt="grid"))


# creating an empty dictionary to store the data
data={}
# creating empty list for storing x and y values
x_values=[]
y_values=[]

# taking user input for the values of x and y
user_input = int(input("Enter number of x and y pairs: "))

for i in range(0,user_input):
    x_value="x{}".format(i)
    data[x_value]=float(input("Enter value of x({}): ".format(i)))
    x_values.append(data[x_value])
for i in range(0,user_input):
    y_value="y{}".format(i)
    data[y_value]=float(input("Enter value of y({}): ".format(i)))
    y_values.append(data[y_value])

Table_maker(x_values, y_values)

# Compute the coefficients using Newton's divided difference formula
a = coef(x_values, y_values) 

# taking user input for the value of x to be interpolated
x_interpolate = float(input("Enter the value of x to interpolate: "))

# Evaluate the polynomial at the given point
y_interpolate = Eval(a, x_values, x_interpolate) 

# printing the value of f(x)
print("The interpolated value of y for x = {} is: {}".format(x_interpolate, y_interpolate))



