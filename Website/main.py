import streamlit as st
import pandas as pd
import numpy as np
from newton_raphson import newton_raphson 
from lagrange_interpolation import lagrange_interpolation 
from n_f_d import newton_forward_difference
from romberg_method import romberg_integration
from simpsons_rule import simpsons_integration
from gauss_elimination import solve_gaussian_elimination
from math import pi, e, log, sin, cos, tan

def main():
    st.image("https://github.com/Kaos599/Applied-Numerical-Methods/blob/0e1fcdf3dc5ad86a9ec64e4bacd9ea123e92677f/Website/logo_1.png", use_column_width=True)
    st.title("Numerate: Applied Maths Solver")
    st.sidebar.header("Select Method")

    category = st.sidebar.selectbox("Choose a category:", 
                                   ["Iterative Methods", 
                                    "Interpolation Methods",
                                    "Numerical Differential-Integral Methods"])

    if category == "Iterative Methods":
        method = st.sidebar.selectbox("Choose a method:",
                                     ["Newton-Raphson Method",
                                      "Secant Method",
                                      "Fixed-Point Iteration Method",
                                      "Gauss-Elimination",
                                      "Gauss-Seidel",
                                      "Bisection Method"])
    elif category == "Interpolation Methods":
        method = st.sidebar.selectbox("Choose a method:",
                                     ["Newton Forward Interpolation",
                                      "Newton Backward Interpolation",
                                      "Lagrange Interpolation",
                                      "Lagrange Inverse Interpolation"])
    elif category == "Numerical Differential-Integral Methods":
        method = st.sidebar.selectbox("Choose a method:",
                                     ["Newton's Forward Difference",
                                      "Quadrature Rule",
                                      "Trapezoidal Rule",
                                      "Simpson's Rule",
                                      "Romberg Method"])

    if category == "Iterative Methods" and method == "Newton-Raphson Method":
        newton_raphson_page()  
    elif category == "Iterative Methods" and method == "Gauss-Elimination":
        gauss_elimination_page()
    elif category == "Interpolation Methods" and method == "Lagrange Interpolation":
        lagrange_interpolation_page()
    elif category == "Numerical Differential-Integral Methods" and method == "Newton's Forward Difference":
        newton_forward_difference_page()
    elif category == "Numerical Differential-Integral Methods" and method == "Quadrature Rule":
        quadrature_rule_page()
    elif category == "Numerical Differential-Integral Methods" and method == "Trapezoidal Rule":
        trapezoidal_rule_page()
    elif category == "Numerical Differential-Integral Methods" and method == "Simpson's Rule":
        simpsons_rule_page()
    elif category == "Numerical Differential-Integral Methods" and method == "Romberg Method":
            romberg_method_page()


        
def gauss_elimination_page():
    st.title("Gaussian Elimination Method")

    # User selects matrix size
    matrix_size = st.radio("Select the size of the matrix:", ('3x3', '4x4'))

    # Input fields for equations and RHS values
    equations = []
    rhs_values = []

    if matrix_size == '3x3':
        for i in range(1, 4):
            equation = st.text_input(f"Enter equation {i} (e.g., 2*x + 3*y - z):")
            rhs_value = st.number_input(f"Enter the RHS value for equation {i}:", value=0)
            equations.append(equation)
            rhs_values.append(rhs_value)

    elif matrix_size == '4x4':
        for i in range(1, 5):
            equation = st.text_input(f"Enter equation {i} (e.g., 2*x + 3*y - z + 4*w):")
            rhs_value = st.number_input(f"Enter the RHS value for equation {i}:", value=0)
            equations.append(equation)
            rhs_values.append(rhs_value)

    # Button to calculate the result
    if st.button("Calculate"):
        # Display and solve the system of equations
        steps, solution = solve_gaussian_elimination(equations, rhs_values, matrix_size)
        st.subheader("Gaussian Elimination Steps:")
        st.text(steps)
        st.subheader("Solution:")
        st.text(solution)

def romberg_method_page():
    st.subheader("Romberg's Method")

    # User inputs
    expr = st.text_input("Enter the expression for f(x):", "sin(x)")
    lower_limit = st.number_input("Enter lower limit of integration:", value=0.0, format="%.6f")
    upper_limit = st.number_input("Enter upper limit of integration:", value=np.pi, format="%.6f")

    if st.button("Calculate"):
        df1, df2, df3, result = romberg_integration(expr, lower_limit, upper_limit)

        # Display the tables
        st.write("Table for h1:")
        st.dataframe(df1)
        st.write("Table for h2:")
        st.dataframe(df2)
        st.write("Table for h3:")
        st.dataframe(df3)

        # Display the result
        st.success(f"The value of the integral using Romberg's method is: {result:.6f}")

def newton_forward_difference_page():
    st.subheader("Newton's Forward Difference Method")

    # Store the number of points in session state
    if 'num_points' not in st.session_state:
        st.session_state.num_points = 3

    # Store the x and y values in session state
    if 'x_values' not in st.session_state:
        st.session_state.x_values = [0.0] * st.session_state.num_points
    if 'y_values' not in st.session_state:
        st.session_state.y_values = [0.0] * st.session_state.num_points

    # Input for the number of x and y pairs
    st.session_state.num_points = st.number_input("Enter the number of x and y pairs:", 
                                                  min_value=2, value=st.session_state.num_points, step=1)

    # Create input table
    for i in range(st.session_state.num_points):
        st.session_state.x_values[i] = st.number_input(f"x[{i}]", value=st.session_state.x_values[i], key=f"x_{i}")
        st.session_state.y_values[i] = st.number_input(f"y[{i}]", value=st.session_state.y_values[i], key=f"y_{i}")
    
    # Display the table
    df = pd.DataFrame({"x": st.session_state.x_values, "y": st.session_state.y_values})
    st.dataframe(df)

    # Input for interpolation point and order of derivative
    x_interpolate = st.number_input("Enter the value of x to interpolate:", format="%.6f", value=0.0, key="x_interpolate")
    order = st.number_input("Enter the order of derivative (1, 2, or 3):", min_value=1, max_value=3, value=1, key="order")

    # Calculate and display the result
    if st.button("Calculate"):
        y_interpolate = newton_forward_difference(st.session_state.x_values, st.session_state.y_values, x_interpolate, order)
        st.success(f"The value of the {order}th derivative at x = {x_interpolate:.6f} is: {y_interpolate:.6f}")

def quadrature_rule_page():
    st.subheader("Quadrature Rule")
    st.write("This section will include Quadrature Rule methods. Content coming soon!")

def trapezoidal_rule_page():
    st.subheader("Trapezoidal Rule")
    st.write("This section will include Trapezoidal Rule methods. Content coming soon!")

def simpsons_rule_page():
    st.subheader("Simpson's Rule Method")

    # User inputs
    expr = st.text_input("Enter the expression for f(x):", "sin(x)")
    lower_limit = st.number_input("Enter lower limit of integration:", value=0.0, format="%.6f")
    upper_limit = st.number_input("Enter upper limit of integration:", value=np.pi, format="%.6f")
    
    rule = st.radio("Which Simpson's rule do you want to use?", ("1/3", "3/8"))
    choice = st.radio("Do you want to input the number of pairs or the step value h?", ("pairs", "h_value"))
    
    user_input = st.number_input(f"Enter the {'number of pairs' if choice == 'pairs' else 'step value h'}:", value=2.0)

    if st.button("Calculate"):
        df, result = simpsons_integration(expr, lower_limit, upper_limit, rule, choice, user_input)

        # Display the table
        st.text("Table:")
        st.text(df)

        # Display the result
        st.success(f"The value of the integral using Simpson's {rule} rule is: {result:.6f}")


def romberg_rule_page():
    st.subheader("Romberg Rule")
    st.write("This section will include Romberg Rule methods. Content coming soon!")
def newton_raphson_page():
    """
    Content and logic for the Newton-Raphson method page.
    """
    st.subheader("Newton-Raphson Method")
    
    fn_input = st.text_input("Enter the function (e.g., x**3 - 2*x - 5):", "x**3 - 2*x - 5")
    
    custom_x_nought = st.checkbox("Choose a custom x_nought value")
    
    x_nought_value = st.number_input("Enter x_nought:", value=0.0, format="%.6f") if custom_x_nought else 0.0
    
    root_sign = st.selectbox("Select root sign:", [("Positive (+)", "p"), ("Negative (-)", "n")])
    
    if st.button("Calculate"):
        df_output, root = newton_raphson(fn_input, custom_x_nought, x_nought_value, root_sign[1])
        st.dataframe(df_output)  
        st.success(f"The root is: {root}")

def lagrange_interpolation_page():
    """
    Streamlit page for Lagrange Interpolation calculations.
    """
    st.subheader("Lagrange Interpolation")

    num_points = st.number_input("Enter the number of x and y pairs:", 
                                 min_value=2, value=3, step=1, key="num_points")

    # Only initialize or reset session state when the "Create Table" button is clicked
    if st.button("Create Table") or 'x_values' not in st.session_state or len(st.session_state.x_values) != num_points:
        st.session_state.x_values = [0.0] * num_points
        st.session_state.y_values = [0.0] * num_points

    # Display input table
    st.write("### Input Table")
    for i in range(num_points):
        st.session_state.x_values[i] = st.number_input(f"x[{i}]", format="%.6f", value=st.session_state.x_values[i], key=f"x_{i}")
        st.session_state.y_values[i] = st.number_input(f"y[{i}]", format="%.6f", value=st.session_state.y_values[i], key=f"y_{i}")
    
    df = pd.DataFrame({"x": st.session_state.x_values, "y": st.session_state.y_values})
    st.dataframe(df)

    # Input for interpolation point
    x_interpolate = st.number_input("Enter the value of x to interpolate:", format="%.6f", value=0.0)

    # Calculate and display results
    if st.button("Calculate Interpolation"):
        y_interpolate = lagrange_interpolation(x_interpolate, st.session_state.x_values, st.session_state.y_values)
        st.success(f"The interpolated value of y for x = {x_interpolate:.6f} is: {y_interpolate:.6f}")         



if __name__ == "__main__":
    main()
