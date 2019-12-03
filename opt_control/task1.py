from gekko import GEKKO
import numpy as np
import matplotlib.pyplot as plt

# Инициализируем модель
m = GEKKO()
nt = 101
m.time = np.linspace(0,2,nt)

# Задаём переменные
y = m.Var(value=1)
z = m.Var(value=5)
u = m.Var(value=0,lb=-1,ub=1)
p = np.zeros(nt)    # Отмечаем последнюю точку
p[-1] = 1.0
final = m.Param(value=p)

# Задаём уравнения
m.Equation(y.dt() == u)
m.Equation(z.dt() == 0.5 * y ** 2)
m.Obj(z * final)    # Целевая функция
m.options.IMODE = 6 # 6 -- задача оптимального управления/динамического программирования
m.solve(disp=False)


# Рисуем получившееся решение
plt.plot(m.time, y.value, 'k-', label=r'$y$')
plt.plot(m.time,u.value,'r--',label=r'$u$')
plt.legend(loc='best')
plt.xlabel('Time')
plt.ylabel('Value')
plt.show()

