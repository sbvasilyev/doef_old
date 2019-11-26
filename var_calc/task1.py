from scipy.optimize import minimize
import matplotlib.pyplot as plt
import numpy as np
import math

# Задаём дискретное время
num_of_fractions = 41   # Количество делений на дискретной шкале времени
t = np.linspace(0, 2, num_of_fractions)     # Дискретная шкала времени
dt = t[1] - t[0]    # Рассчитываем шаг шкалы


# Задаём оптимизируемый функционал в дискретном времени
def f(y):
    return np.sum(y[1:] ** 2 + ((y[1:] - y[:-1]) / dt) ** 2)


y0 = [0.5 for x in range(0, num_of_fractions)]     # Начальное значение y

# Задаем ограничения на y. У нас y(0)=0 и y(2)=1
bounds = [(None, None) for x in range(0, num_of_fractions)]
bounds[0], bounds[-1] = (0.0, 0.0), (1.0, 1.0)

# Минимизируем функционал
res = minimize(f, y0, method='l-bfgs-b', bounds=bounds)


# Определим функцию, возвращающую аналитическое решение. Напомню, что y = (e^t - e^(-t))/(e^2 - e^(-2))
def f_analytical(t):
    return [(math.exp(elem) - math.exp(-elem))/(math.exp(2) - math.exp(-2)) for elem in t]


# Построим график и убедимся, что численное и аналитическое решения совпали
plt.plot(t, res.x, 'r', t, f_analytical(t), '--b')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(('y численный', 'y аналитический'))
plt.show()
