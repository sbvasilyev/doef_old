from scipy.optimize import minimize
import matplotlib.pyplot as plt
import numpy as np


num_of_fractions = 41
t = np.linspace(0, 1, num_of_fractions)
dt = t[1] - t[0]


def f(y):
    return np.sum(y[1:] ** 2 + (t[1:] ** 2) * (((y[1:] - y[:-1]) / dt) ** 2), axis=0)


y0 = [.5 for x in range(0, num_of_fractions)]
bounds = [(None, None) for x in range(0, num_of_fractions)]
bounds[0], bounds[-1] = (1.0, 1.0), (2.0, 2.0)

res = minimize(f, y0, method='l-bfgs-b', bounds=bounds)

plt.plot(t, res.x)
plt.xlabel('t')
plt.ylabel('y')
plt.show()

# Откинем правую границу

bounds2 = [(None, None) for x in range(0, num_of_fractions)]
bounds2[0] = (1.0, 1.0)

res2 = minimize(f, y0, method='l-bfgs-b', bounds=bounds2)

plt.plot(t, res2.x)
plt.xlabel('t')
plt.ylabel('y')
plt.show()
