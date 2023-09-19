import numpy as np
import matplotlib.pyplot as plt


def solve_equations():
    # Define the initial conditions and step size
    x0 = 0.0  # Initial value of x
    y0 = 1.0  # Initial value of y
    u0 = 1.0  # Initial value of u
    h = 0.2  # Step size
    num_steps = 50  # Number of iterations

    # Initialize arrays to store the values
    x_vals = [x0]
    y_vals = [y0]
    u_vals = [u0]

    # Perform Euler's method
    for i in range(num_steps):
        # Calculate the derivatives at the current values
        dy_dx = u_vals[i]
        du_dx = (1 - y_vals[i] ** 2) * u_vals[i] - y_vals[i]

        # Update the values using Euler's method
        x_vals.append(x_vals[i] + h)
        y_vals.append(y_vals[i] + h * dy_dx)
        u_vals.append(u_vals[i] + h * du_dx)

    return x_vals, y_vals, u_vals


# Solve the equations and retrieve the values
x_vals, y_vals, u_vals = solve_equations()


res = [1, 7, 13, 19, 23, 26, 31, 42, 47, 50 ]

x, y, u = [], [], []
for i in res:
    x.append(x_vals[i])
    y.append(y_vals[i])
    u.append(u_vals[i])

for i in range(len(x)):
    print(f'x={x[i]:.1f}, y= {y[i]}, z={u[i]}')


# Plot the results
plt.plot(x_vals, y_vals)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Solution of y'' - (1 - y^2)y' + y = 0 using Euler's method")
plt.grid(True)
plt.show()
