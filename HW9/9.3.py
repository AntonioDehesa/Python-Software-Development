import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    x = np.linspace(0,2*np.pi, 100)
    plt.plot(x,np.sin(x), "bo-")
    plt.plot(x,np.cos(x), "mD:")
    plt.legend(labels = ("Sine", "Cosine"), loc= "lower right")
    plt.title("Sine and Cosine vs angle in radians")
    plt.xlabel("Angle in radians")
    plt.ylabel("Sine and Cosine")
    plt.grid()
    plt.show()