from scipy.optimize import minimize
import matplotlib.pyplot as plt
import numpy as np


num_of_fractions = 41
t = np.linspace(0, 1, num_of_fractions)
dt = t[1] - t[0]


def f(y):
    return np.sum(y[1:] * (((y[1:] - y[:-1]) / dt) ** 2), axis=0)


y0 = [.5 for x in range(0, num_of_fractions)]
bounds = [(None, None) for x in range(0, num_of_fractions)]
bounds[0], bounds[-1] = (1.0, 1.0), (4.0, 4.0)

res = minimize(f, y0, method='l-bfgs-b', bounds=bounds)


def f_analytical(t):
    return [(7 * elem + 1) ** (2 / 3) for elem in t]


# Построим график и убедимся, что численное и аналитическое решения совпали
plt.plot(t, res.x, 'r', t, f_analytical(t), '--b')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(('y численный', 'y аналитический'))
plt.show()
