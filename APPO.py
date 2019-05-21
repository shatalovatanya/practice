import matplotlib.pyplot as plt
import function as fun
import numpy as np
import scipy as sp

x, y = fun.openFile('data.txt')
plt.plot(x, y, 'orange')
plt.xlim(0, 2)
plt.ylim(0,2)

def approximation(x, y):
    d = 1
    fp, residuals, rank, sv, rcond = sp.polyfit(x, y, d, full=True)
    f = sp.poly1d(fp)
    # print('Коэффициент -- a %s  '%round(fp[0],4))
    # print('Коэффициент-- b %s  '%round(fp[1],4))
    # print('Коэффициент -- c %s  '%round(fp[2],4))
    # y1=[fp[0]*x[i]**2+fp[1]*x[i]+fp[2] for i in range(0,len(x))] # значения функции a*x**2+b*x+c
    # so=round(sum([abs(y[i]-y1[i]) for i in range(0,len(x))])/(len(x)*sum(y))*100,4) # средняя ошибка
    # print('Average quadratic deviation '+str(so))
    fx = sp.linspace(x[0], x[-1] + 1, len(x))
    plt.plot(x, y, 'o', markersize=10)
    plt.plot(fx, f(fx),  linewidth=2)
    plt.grid(True)
    plt.show()


approximation(x, y)