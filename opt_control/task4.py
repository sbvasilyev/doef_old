import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as plt

m = GEKKO()
nt = 301
tm = np.linspace(0, 1, nt)
m.time = tm

y1 = m.Var(value=np.pi / 2.0)
y2 = m.Var(value=4.0)
y3 = m.Var(value=0.0)

p = np.zeros(nt)
p[-1] = 1.0
final = m.Param(value=p)

T = m.FV(value=1.0, lb=0.1, ub=100.0)
T.STATUS = 1

u = m.MV(value=0, lb=-2, ub=2)
u.STATUS = 1

m.Equation(y1.dt() == u * T)
m.Equation(y2.dt() == m.cos(y1) * T)
m.Equation(y3.dt() == m.sin(y1) * T)

m.Equation(y2 * final <= 0)
m.Equation(y3 * final <= 0)

m.Obj(T)

m.options.IMODE = 6
m.solve()

print('Найденное T: ' + str(T.value[0]))

tm = tm * T.value[0]

plt.figure(1)
plt.plot(tm, y1.value, 'k-', LineWidth=2, label=r'$y_1$')
plt.plot(tm, y2.value, 'b-', LineWidth=2, label=r'$y_2$')
plt.plot(tm, y3.value, 'g--', LineWidth=2, label=r'$y_3$')
plt.plot(tm, u.value, 'r--', LineWidth=2, label=r'$u$')
plt.legend(loc='best')
plt.xlabel('Time')
plt.ylabel('Value')
plt.show()
