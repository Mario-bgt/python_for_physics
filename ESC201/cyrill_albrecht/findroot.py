"""Name:      Albreecht, Cyrill
   Email:     albrecht.cyrill@uzh.ch
   Date:      26 February, 2001
   Kurs:      ESC201
   Semester:  HS23
   Week:      1
   Thema:     Root finding
"""

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x ** x - 100


def main():
    # Plotting the function

    x = np.linspace(3, 4, 100)
    y = f(x)
    plt.plot(x, y)
    plt.grid()

    plt.show()

    def bisection_root_finding(f, a, b, tol=1e-6, max_iter=100):

        if f(a) * f(b) >= 0:
            return None
        elif f(a) == 0:
            return a
        elif f(b) == 0:
            return b
        else:
            for i in range(max_iter):
                c = (a + b) / 2  # midpoint

                if abs(f(c)) < tol:  # check if root is found
                    return c

                if f(c) * f(a) < 0:  # decide witch side to keep
                    b = c
                else:
                    a = c

            print(f"Did not converge after {max_iter} iterations.")

    print(bisection_root_finding(f, 0, 15))


# Main__________________________________________________________________________


if __name__ == "__main__":
    main()
