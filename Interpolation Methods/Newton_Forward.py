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
    data[x_value]=float(input("Enter value of x({}): ".format(i)))
    x_values.append(data[x_value])
for i in range(0,user_input):
    y_value="y{}".format(i)
    data[y_value]=float(input("Enter value of y({}): ".format(i)))
    y_values.append(data[y_value])

Table_maker(x_values, y_values)
def newton_forward(x_values, y_values, x):
    # number of data points
    n = len(x_values)

    # calculating forward difference table
    forward_difference = [[0 for i in range(n)]
                          for j in range(n)]

    # inserting y values in the first column
    for i in range(n):
        forward_difference[i][0] = y_values[i]

    # calculating forward difference table
    for i in range(1, n):
        for j in range(n - i):
            forward_difference[j][i] = (forward_difference[j + 1][i - 1] - forward_difference[j][i - 1])

    # initializing result
    result = forward_difference[0][0]

    print("The table is: ")
    print(tabulate(forward_difference, tablefmt="grid"))

    # calculating the value of f(x) using the formula
    for i in range(1, n):
        term = forward_difference[0][i]
        for j in range(i):
            term = term * (x - x_values[j])
            term = term / (x_values[i] - x_values[j])
        result = result + term

    return result

# taking user input for the value of x to be interpolated
x = float(input("\nEnter the value of x to be interpolated: "))

# calculating the value of f(x) using the newton forward interpolation method
result = newton_forward(x_values, y_values, x)

# printing the value of f(x)
print("\nThe value of f({}) using Newton forward interpolation method is: {}".format(x, result))
