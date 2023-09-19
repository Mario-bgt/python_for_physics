# -*- coding: utf-8 -*-

"""Name:      Baumgartner, Mario Lukas
   Email:     mariolukas.baumgartner@uzh.ch
   Date:      19 September, 2023
   Kurs:      ESC201
   Semester:  HS23
   Week:      1
   Thema:     Bisection root finding
"""


# Functions_____________________________________________________________________

def bisection_method(func, a, b, max_iter=1000, eps=0.001):
    """
    Bisection method for root finding
    :param func: function to find root of
    :param a: left bound
    :param b: right bound
    :param max_iter: maximum number of iterations
    :param eps: tolerance
    :return: root of function
    """
    # Check if root is in interval
    if func(a) * func(b) > 0:
        print("Root is not in interval or multiple roots exist")
        return None
    # Check if root is at bounds
    if func(a) == 0:
        return a
    if func(b) == 0:
        return b
    # Check if root is at midpoint
    midpoint = (a + b) / 2
    if func(midpoint) == 0:
        return midpoint
    # Iterate until tolerance is reached
    for i in range(max_iter):
        midpoint = (a + b) / 2
        if abs(func(midpoint)) < eps:
            return midpoint
        if func(a) * func(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    print("Maximum number of iterations reached")
    return None


def main():
    def funny_function(x):
        return 2 ** x - 100*x + 1

    root = bisection_method(funny_function, 5, 15)
    print('The root of 2^x - 100*x + 1 in the interval [5:15] is:', root)


# Main__________________________________________________________________________

if __name__ == "__main__":
    main()
