import math as mat
from sympy import *
import sympy as sp
from tabulate import tabulate
import pandas as pd 

# --- Function for Newton-Raphson Method ---

def newton_raphson(fn_input, custom_x_nought, x_nought_value, root_sign):
        """
        Calculates the root of a function using the Newton-Raphson method.

        Args:
            fn_input (str): The function to find the root of.
            custom_x_nought (bool): Whether the user wants to input a custom x_nought value.
            x_nought_value (float): The custom x_nought value (if provided).
            root_sign (str): Whether to search for a positive ('p') or negative ('n') root.

        Returns:
            tuple: A tuple containing the output dataframe (pd.DataFrame) and the root (float).
        """

        # Create a symbol for x
        x = symbols('x')

        # Convert the input string to a sympy expression
        expr = sympify(fn_input)

        # Create a lambda function to evaluate the expression for any x
        f = lambdify(x, expr) 

        # Determine x_nought based on user input
        if custom_x_nought:
            x_nought = x_nought_value
        else:
            x_nought = find_initial_guess(f, root_sign)

        # Create a lambda function to evaluate the derivative of the expression for any x
        d = lambdify(x, diff(expr,x))

        # Initialize a list of dictionaries to store output data
        output_data = []

        # Initialize a counter variable for counting the iterations
        i = 0

        # Repeat until convergence is reached
        while True:
            # Calculate the derivative of the expression at x_nought
            d1 = sp.diff(expr, x)

            # Store the previous value of x_nought
            x_nought_previous = x_nought

            # Apply the Newton-Raphson formula to get the next value of x_nought
            expr2 = x_nought - expr.subs(x, x_nought)/d1.subs(x, x_nought)

            # Round the result to six decimal places
            x_nought = round(expr2, 6)

            # Append data as a dictionary to output_data
            output_data.append({"Iteration": i, "x_(i-1)": x_nought_previous, "x_i": x_nought, "f(x_i)": f(x_nought)})

            # Check if convergence is reached by comparing previous and current values of x_nought
            if round(x_nought_previous, 6) == round(x_nought, 6):
                # Create a DataFrame from the output data
                df_output = pd.DataFrame(output_data)
                return df_output, x_nought
            i += 1

# --- Helper Function to Find Initial Guess (unchanged) ---
def find_initial_guess(f, sign):
    """
    Finds an initial guess for the root based on the sign.
    """
    if sign == "p":
        for i in range(0, 20):
            if f(i) * f(i + 1) <= 0:  # Check for sign change or root at i
                return i 
    elif sign == "n":
        for i in range(-1, -20, -1):
            if f(i) * f(i - 1) <= 0:
                return i
    return 0  # Default to 0 if no suitable guess is found