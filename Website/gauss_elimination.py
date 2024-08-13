import sympy as sp

def solve_gaussian_elimination(equations, rhs_values, matrix_size):
    steps = ""
    solution = ""

    if matrix_size == '3x3':
        steps, solution = gauss_elimination_3x3(equations, rhs_values)
    elif matrix_size == '4x4':
        steps, solution = gauss_elimination_4x4(equations, rhs_values)

    return steps, solution

def gauss_elimination_3x3(equations, rhs_values):
    # Define symbolic variables
    x, y, z = sp.symbols('x y z')

    # Convert the equations to sympy expressions
    eq1 = sp.sympify(equations[0])
    eq2 = sp.sympify(equations[1])
    eq3 = sp.sympify(equations[2])

    # Extract coefficients
    a11 = eq1.coeff(x)
    a12 = eq1.coeff(y)
    a13 = eq1.coeff(z)

    a21 = eq2.coeff(x)
    a22 = eq2.coeff(y)
    a23 = eq2.coeff(z)

    a31 = eq3.coeff(x)
    a32 = eq3.coeff(y)
    a33 = eq3.coeff(z)

    b1 = rhs_values[0]
    b2 = rhs_values[1]
    b3 = rhs_values[2]

    # Step-by-step Gaussian Elimination
    steps = "Initial Matrix:\n"
    steps += f"[{a11}, {a12}, {a13}] [{b1}]\n"
    steps += f"[{a21}, {a22}, {a23}] [{b2}]\n"
    steps += f"[{a31}, {a32}, {a33}] [{b3}]\n\n"

    # Row transformations
    a21_ = -(a21/a11)*a11 + a21
    a22_ = -(a21/a11)*a12 + a22
    a23_ = -(a21/a11)*a13 + a23
    b2_ = -(a21/a11)*b1 + b2

    a32_ = -(a31/a11)*a12 + a32
    a33_ = -(a31/a11)*a13 + a33
    b3_ = -(a31/a11)*b1 + b3

    steps += "After row transformations:\n"
    steps += f"[{a11}, {a12}, {a13}] [{b1}]\n"
    steps += f"[{a21_}, {a22_}, {a23_}] [{b2_}]\n"
    steps += f"[0, {a32_}, {a33_}] [{b3_}]\n\n"

    # Further transformations
    a33_ = -(a32_/a22_)*a23_ + a33_
    b3_ = -(a32_/a22_)*b2_ + b3_

    steps += "After further row transformations:\n"
    steps += f"[{a11}, {a12}, {a13}] [{b1}]\n"
    steps += f"[{a21_}, {a22_}, {a23_}] [{b2_}]\n"
    steps += f"[0, 0, {a33_}] [{b3_}]\n\n"

    # Back substitution
    z = b3_ / a33_
    y = (b2_ - a23_ * z) / a22_
    x = (b1 - a12 * y - a13 * z) / a11

    solution = f"x = {x}\n"
    solution += f"y = {y}\n"
    solution += f"z = {z}"

    return steps, solution

def gauss_elimination_4x4(equations, rhs_values):
    # Define symbolic variables
    x, y, z, w = sp.symbols('x y z w')

    # Convert the equations to sympy expressions
    eq = [sp.sympify(e) for e in equations]

    # Extract coefficients
    a = []
    for i in range(4):
        row = [eq[i].coeff(x), eq[i].coeff(y), eq[i].coeff(z), eq[i].coeff(w)]
        a.append(row)

    b = rhs_values

    steps = "Initial Matrix:\n"
    for i in range(4):
        steps += f"[{a[i][0]}, {a[i][1]}, {a[i][2]}, {a[i][3]}] [{b[i]}]\n"
    steps += "\n"

    # Perform Gaussian Elimination
    for i in range(3):
        for j in range(i + 1, 4):
            factor = -(a[j][i] / a[i][i])
            for k in range(i, 4):
                a[j][k] = factor * a[i][k] + a[j][k]
            b[j] = factor * b[i] + b[j]

            steps += f"After eliminating a[{j}][{i}]:\n"
            for m in range(4):
                steps += f"[{a[m][0]}, {a[m][1]}, {a[m][2]}, {a[m][3]}] [{b[m]}]\n"
            steps += "\n"

    # Back substitution
    solution = []
    for i in range(3, -1, -1):
        value = b[i]
        for j in range(i + 1, 4):
            value -= a[i][j] * solution[3 - j]
        value /= a[i][i]
        solution.append(value)

    solution.reverse()
    
    solution_text = f"x = {solution[0]}\n"
    solution_text += f"y = {solution[1]}\n"
    solution_text += f"z = {solution[2]}\n"
    solution_text += f"w = {solution[3]}"

    return steps, solution_text
