import streamlit as st
import pandas as pd
from functools import reduce

def lagrange_interpolation(x, x_values, y_values):
    """
    Performs Lagrange interpolation, showing step-by-step calculations.

    Args:
        x (float): The x-value to interpolate for.
        x_values (list): The list of known x-values.
        y_values (list): The list of known y-values.

    Returns:
        float: The interpolated y-value.
    """
    n = len(x_values)
    y = 0.0
    calculation_steps = []

    for i in range(n):
        term = y_values[i]
        term_str = f"{y_values[i]:.6f}"  # Start with y_i
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
                term_str += f" * (x - {x_values[j]:.6f}) / ({x_values[i]:.6f} - {x_values[j]:.6f})"
        y += term
        calculation_steps.append(term_str)

    # Display calculations
    st.write("**Calculation Steps:**")
    for i, step in enumerate(calculation_steps):
        st.latex(f"L_{i}(x) = {step}")

    st.latex(f"P(x) = {' + '.join(calculation_steps)}")
    st.latex(f"P({x:.6f}) = {y:.6f}")
    return y

def lagrange_interpolation_page():
    """
    Streamlit page for Lagrange Interpolation calculations.
    """
    st.subheader("Lagrange Interpolation")

    # Input for number of data points
    num_points = st.number_input("Enter the number of x and y pairs:", 
                                 min_value=2, value=3, step=1)

    # Create input table after button click
    if st.button("Create Table"):
        x_values = [st.number_input(f"x[{i}]", format="%.6f", value=0.0, key=f"x_{i}") for i in range(num_points)]
        y_values = [st.number_input(f"y[{i}]", format="%.6f", value=0.0, key=f"y_{i}") for i in range(num_points)]
        df = pd.DataFrame({"x": x_values, "y": y_values})
        st.dataframe(df)

        # Input for interpolation point
        x_interpolate = st.number_input("Enter the value of x to interpolate:", format="%.6f", value=0.0)

        # Calculate and display results
        if st.button("Calculate Interpolation"):
            y_interpolate = lagrange_interpolation(x_interpolate, x_values, y_values)
            st.success(f"The interpolated value of y for x = {x_interpolate:.6f} is: {y_interpolate:.6f}")