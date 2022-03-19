# plottask.py
# A program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# Author: Micheal McEnery

# This line imports numpy as np
import numpy as np

# This line imports matplotlib as plt
import matplotlib.pyplot as plt


# This line creates the x-axis
xpoints = np.array(range(0, 4))
# This line creates the y-axis
ypoints = xpoints


# This line plots the "f(x) = x" function
plt.plot(xpoints, ypoints, label = "f(x) = x", color = "r")

# This line plots the "g(x) = x2" function
plt.plot(xpoints, ypoints * ypoints, label = "g(x) = x2", color = "y")

# This line plots the "h(x) = x3" function
plt.plot(xpoints, ypoints * ypoints * ypoints, label = "h(x) = x3", color = "g")

# This line adds a title to the plot
plt.title("plottask.py")

# This line adds a label to the x-axis
plt.xlabel("x-axis")

# This line adds a label to the y-axis
plt.ylabel("y-axis")

# This line adds a legend to the plot
plt.legend()

# This line shows the plot
plt.show()