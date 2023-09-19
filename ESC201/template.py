#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      Nachname, Vorname
   Email:     nachname.vorname@uzh.ch
   Date:      01 February, 2019
   Kurs:      ESC201
   Semester:  FS19
   Week:      2
   Thema:     Keplergleichung
"""

# Futures
from __future__ import print_function

# Each module import gets its own line
import matplotlib.pyplot as plt
import numpy as np

# Multiple functions from the same module can go on one line
# z.B. from subprocess import Popen, PIPE


# Functions_____________________________________________________________________

def hello_world():
    # Print "Hello, world!"
    print("Hello, world!")


def main():
    # Call a function
    hello_world()

    # Create a figure with matplotlib
    fig, ax = plt.subplots(1, 1, figsize=(10,10))

    # Random test data
    x1 = np.random.normal(0, 0.1, 1000)
    y1 = np.random.normal(0, 0.1, 1000)
    # Second set of random data
    x2 = np.random.normal(0.4, 0.1, 500)
    y2 = np.random.normal(0.1, 0.1, 500)

    # Plot the first data set as a scatter plot
    ax.scatter(x1, y1, color='blue', alpha=0.5, label='data1')
    # Plot the second data set
    ax.scatter(x2, y2, color='red', alpha=0.5, label='data2')

    # Change the axes labels
    ax.set_xlabel('x-axis', fontsize=18)
    ax.set_ylabel('y-axis', fontsize=18)

    # Give the figure a title
    ax.set_title('ESC201 Template', fontsize=18)

    # Set axes limits
    lim = 1.0
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)

    # Force equal aspect ratio
    ax.set_aspect('equal')

    # Grid overlay
    ax.grid(False)

    # Legend
    plt.legend(loc=2, prop={'size': 18})

    # Save the plot if desired
    plt.savefig('template.png', format='png')

    # Display the plot!
    plt.show()



# Main__________________________________________________________________________

if __name__== "__main__":
    main()
