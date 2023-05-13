from tabulate import tabulate


user_input = int(input("Enter number of x and y pairs: "))

def Table_maker(x_values, y_values):
 
 data1 = {}

 
 data1["x"] = x_values
 data1["y"] = y_values

 
 print(tabulate(data1, headers="keys", tablefmt="grid"))



data={}

x_values=[]
y_values=[]

for i in range(0,user_input):
 x_value="x{}".format(i)
 data[x_value]=float(input("Enter value of x({}): ".format(i)))
 x_values.append(data[x_value])
for i in range(0,user_input):
 y_value="y{}".format(i)
 data[y_value]=float(input("Enter value of y({}): ".format(i)))
 y_values.append(data[y_value])

Table_maker(x_values, y_values)

def newton_backward(x_values, y_values, x):
 
 n = len(x_values)

 
 backward_difference = [[0 for i in range(n)]
 for j in range(n)]

 
 for i in range(n):
    backward_difference[i][0] = y_values[i]

 
 for i in range(1, n):
    for j in range(n - 1, i - 1, -1):
        backward_difference[j][i] = backward_difference[j][i-1] - backward_difference[j-1][i-1]

 
 result = backward_difference[n-1][0]

 print("The table is: ")
 for i in range(n - 1, -1, -1):
    row = []
    for j in range(n - i):
        row.append(backward_difference[i][j])
        print(row)

 
 u = (x - x_values[n-1]) / (x_values[1] - x_values[0])
 for i in range(1, n):
    term = backward_difference[n-1][i]
    for j in range(i):
        term = term * (x - x_values[n-i+j])
        term = term / (x_values[i] - x_values[j])
    result = result + term

 return result


x = float(input("\nEnter the value of x to be interpolated: "))


result = newton_backward(x_values, y_values, x)


print("\nThe value of f({}) using Newton backward interpolation method is: {}".format(x, result))
