#IMPORTANT (USAGE INFO)

# Use log fns as log(value, base)
# Use trignometric fns as cos(x) or sin(x) or tan(x)
# To use e as e**x use exp(x)
# To use power use x**y to signify x^y
# To use multiply use x*y to signify xy
# To use divide use x/y


# import the tabulate module
from tabulate import tabulate

# getting the user input for the number of pairs
user_input = int(input("Enter number of x and y pairs: "))

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
for i in range(0,user_input):
    x_value="x{}".format(i)
    data[x_value]=int(input("Enter value of x({}): ".format(i)))
    x_values.append(data[x_value])
for i in range(0,user_input):
    y_value="y{}".format(i)
    data[y_value]=int(input("Enter value of y({}): ".format(i)))
    y_values.append(data[y_value])

Table_maker(x_values, y_values)

# calculating the polynomial using Lagrange interpolation formula
def lagrange_interpolation(x, x_values, y_values):
    polynomial = 0
    for i in range(len(x_values)):
        term = y_values[i]
        for j in range(len(x_values)):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        polynomial += term
    return polynomial

# getting the value of x to be interpolated from the user
x_interpolate = float(input("Enter the value of x to interpolate: "))

# interpolating the value of y for x_interpolate
y_interpolate = lagrange_interpolation(x_interpolate, x_values, y_values)

# printing the polynomial after applying the formula
print("The polynomial after applying the Lagrange interpolation formula is:")
terms = []
for i in range(len(x_values)):
    term = "({})".format(y_values[i])
    for j in range(len(x_values)):
        if i != j:
            term += " * (x - {}) / ({})".format(x_values[j], x_values[i] - x_values[j])
    terms.append(term)
polynomial = " + ".join(terms)
print(polynomial)

# printing the interpolated value of y for x_interpolate
print("The interpolated value of y for x = {} is: {}".format(x_interpolate, y_interpolate))



