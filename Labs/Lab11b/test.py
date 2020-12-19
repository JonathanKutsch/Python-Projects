import matplotlib.pyplot as plt
import numpy as np


def get_params():
    parameters = open("parameters.txt", "r")
    x = np.arange(1, 7, 0.1)
    y = np.sin(2 * x) * np.exp(-0.2 * x) * 15
    # plt.plot(x, y, color="red")
    plt.plot(x, y, marker=10, color="green", label="y = 15exp(-0.2x)sin(2x)")
    plt.legend(loc='upper right', frameon=False)
    plt.title("Positive or negative?")
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.show()


get_params()