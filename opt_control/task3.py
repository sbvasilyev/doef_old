from gekko import GEKKO
import numpy as np
import math
import matplotlib.pyplot as plt

m = GEKKO()
nt = 301
m.time = np.linspace(0,2,nt)

y = m.Var(value=2)
z = m.Var(value=0)
u = m.Var(value=np.e-2, lb=np.e-2)
p = np.zeros(nt)
p[-1] = 1.0
final = m.Param(value=p)

m.Equation(y.dt()==y + u)
m.Equation(z.dt()==-y + (u ** 2) * 0.5 + u)
m.Obj(z*final)
m.options.IMODE = 6
m.solve(disp=False)



def u_a(t):
    return [math.exp(-elem + 2) - 2 if elem <= 1
            else math.e - 2
            for elem in t]


def y_a(t):
    return [2 + 0.5 * math.exp(2) * (math.exp(elem) - math.exp(-elem)) if elem <= 1
            else (1 + 0.5 * (math.e ** 2 - 1)) * math.exp(elem) - math.e + 2
            for elem in t]


plt.figure(figsize=(4,3))
plt.subplot(2,1,1)
plt.plot(m.time,y.value,'k-',label=r'$y$')
plt.plot(m.time,y_a(m.time),'r--',label=r'$y^*$')
plt.legend(loc='best')
plt.ylabel('Value')
plt.subplot(2,1,2)
plt.plot(m.time,u.value,'k-',label=r'$u$')
plt.plot(m.time,u_a(m.time),'r--',label=r'$u^*$')
plt.legend(loc='best')
plt.ylabel('Value')
plt.xlabel('Time')
plt.show()
