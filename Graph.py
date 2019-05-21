import matplotlib.pyplot as plt #построение графика
import function as fun #
import numpy as np #считывание массива
import scipy as sp #научные и инженерные расчеты

cx, cy = fun.openFile('Coordinates.txt')
yarray = np.array(cy, dtype=float)          #np-библиотека для работы с мат ф-циями в массивах; dtype описывает эд-ты в массиве
xarray = np.array(cx, dtype=float)


xnew=np.linspace(np.min(xarray), np.max(xarray), 100)
ynew = [fun.funLagranz(xarray, yarray, i) for i in xnew]
plt.plot(xnew, ynew, 'red')
plt.plot(cx, cy, 'o', xnew, ynew)
plt.xlabel('X', fontsize=10)
plt.ylabel('Y', fontsize=10)
plt.legend(('Interpolation F(x)', 'F(x)'))
plt.grid(True)
plt.show()
#пока line принадлежит lines.split('\n'), это разделения файла на строки.
#x, y = re(регулярные выражения).split(разделить строку)('\s+'(до какого угодно числа пробелов), line (переменная которую надо разделить))
#разделяет на нескольк переменых, 1 из которых = x, 2 = у

#np.linspace(возвращает одномерный массив из указанного количества элементов) (np.min(xarray) начало послед, np.max(yarray) конец)
#на выходе одномерный массив из указанного количества элементов, значения которых равномерно распределенны внутри закрытого ([start, stop]) или полуоткрытого ([start, stop)) интервала




























#пока line принадлежит lines.split('\n'), это разделения файла на строки.
#x, y = re(регулярные выражения).split(разделить строку)('\s+'(до какого угодно числа пробелов), line (переменная которую надо разделить))
#разделяет на нескольк переменых, 1 из которых = x, 2 = у

#np.linspace(возвращает одномерный массив из указанного количества элементов) (np.min(xarray) начало послед, np.max(yarray) конец)
#на выходе одномерный массив из указанного количества элементов, значения которых равномерно распределенны внутри закрытого ([start, stop]) или полуоткрытого ([start, stop)) интервала