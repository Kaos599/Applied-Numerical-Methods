import numpy as np
from tabulate import tabulate

def coef(x, y):
    n = len(x)
    a = np.copy(y)
    for i in range(1, n):
        for j in range(0, n-i):
            a[j] = a[j+1] - a[j]
        if i < 4: # add this condition to include the higher order forward differences
            a = np.append(a, 0) # append a zero at the end of the array
    return a

def Eval(a, x, r, h, order):
    if order == 1:
        p = r
        p1 = p - 0.5
        p2 = p - 1
        if x in x_values: # check if x is a tabular value
            return (a[1] - 0.5 * a[2] + (1/3) * a[3] - (1/4) * a[4]) / h # use the formula for tabular values
        else:
            return (a[1] + p1 * a[2] + (6 * p2**2 - 6 * p2 + 2) / 12 * a[3]) / h # use the formula for non-tabular values
    elif order == 2:
        p = r
        p1 = p - 1
        if x in x_values: # check if x is a tabular value
            return (a[2] - a[3] + (11/12) * a[4]) / (h**2) # use the formula for tabular values
        else:
            return (a[2] + p1 * a[3] + (6 * p**2 - 18 * p + 11) / 12 * a[4]) / (h**2) # use the formula for non-tabular values
    elif order == 3:
        p = r
        if x in x_values: # check if x is a tabular value
            return (a[3] - (3/2) * a[4]) / (h**3) # use the formula for tabular values
        else:
            return (a[3] + (12 * p - 18) / 12 * a[4]) / (h**3) # use the formula for non-tabular values
    else:
        return 0

def binom(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return binom(n-1, k-1) + binom(n-1, k)

def Table_maker(x_values, y_values):
    data1 = {}
    data1["x"] = x_values
    data1["y"] = y_values
    print(tabulate(data1, headers="keys", tablefmt="grid"))

data={}
x_values=[]
y_values=[]
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

a = coef(x_values, y_values)
x_interpolate = float(input("Enter the value of x to interpolate: "))

order = int(input("Enter the order of derivative: "))
r = (x_interpolate - x_values[0]) / (x_values[1] - x_values[0])
h = x_values[1] - x_values[0]
y_interpolate = Eval(a, x_interpolate, r, h, order)
print("\nThe value of the {}th derivative using Newton's forward difference formula is: {}".format(order, y_interpolate))
