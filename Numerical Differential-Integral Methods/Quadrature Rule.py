#IMPORTANT (USAGE INFO)

# Use log fns as log(value, base)
# Use trignometric fns as cos(x) or sin(x) or tan(x)
# To use e as e**x use exp(x)
# To use power use x**y to signify x^y
# To use multiply use x*y to signify xy
# To use divide use x/y


# Import the necessary libraries
import numpy as np

# Input the expression for the function to be integrated
expr = input("Enter the expression for f(x): ")

# Define the function to be integrated using eval
def f(x):
    return eval(expr)

# Input the lower and upper limits of integration
lower_limit = float(input("Enter lower limit of integration: "))
upper_limit = float(input("Enter upper limit of integration: "))

# Define the 2-point Gauss formula weights and abscissas
weights_2_point = np.array([1, 1])
abscissas_2_point = np.array([-0.5773502691896257, 0.5773502691896257])

# Define the 3-point Gauss formula weights and abscissas
weights_3_point = np.array([0.5555555555555556, 0.8888888888888888, 0.5555555555555556])
abscissas_3_point = np.array([-0.7745966692414834, 0, 0.7745966692414834])

# Ask the user which Gaussian formula they want to use
formula = int(input("Which Gaussian formula do you want to use? (2-point: 2, 3-point: 3): "))

# Calculate the integration
if formula == 2:
    # Use the 2-point Gauss formula
    x_values = 0.5 * (lower_limit + upper_limit) + 0.5 * (upper_limit - lower_limit) * abscissas_2_point
    y_values = f(x_values)
    result = 0.5 * (upper_limit - lower_limit) * np.sum(weights_2_point * y_values)
    
    # Display the steps
    print("f(-1/√3) = ",y_values[0])
    print("f(1/√3) = ",y_values[1])
    print("Result: ", result)
    
elif formula == 3:
    # Use the 3-point Gauss formula
    x_values = 0.5 * (lower_limit + upper_limit) + 0.5 * (upper_limit - lower_limit) * abscissas_3_point
    y_values = f(x_values)
    result = 0.5 * (upper_limit - lower_limit) * np.sum(weights_3_point * y_values)
    
    # Display the steps
    print("f(0) = ",y_values[1])
    print("f(-√3/√5) = ",y_values[0])
    print("f(√3/√5) = ",y_values[2])
    print("Result: ", result)
    
else:
    print("Invalid formula choice. Please enter 2 or 3.")
    exit()

#Printing the result
print("\nThe value of the integral using the {}-point Gauss formula is: {}".format(formula, result))
