import numpy as np
from matplotlib import pyplot as plt


def weierstrass_function(a, b, x, n):
    result = 0

    for i in range(n):
        result += b ** i * np.cos(a ** i * np.pi * x)

    return result


a = 9
b = 0.5
n = 100

x = np.arange(0, 10, 0.01)
y = weierstrass_function(a, b, x, n)

plt.plot(x, y)
plt.show()
