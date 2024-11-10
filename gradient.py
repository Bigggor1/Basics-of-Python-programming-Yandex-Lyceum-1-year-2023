import matplotlib.pyplot as plt
import numpy as np
import matplotlib as ptl
from IPython.display import clear_output
import time


"""
Берем случайную точку  х  функции  f  и фиксируем  α  и  ϵ 
Вычисляем производную  f′(x) 
Двигаем  х :  xновое=x−α⋅f′(x) 
Повторяем снова начиная с пункта 2 до тех пор, пока  Δy=y(xновое)−y(x)  не станет меньше  ϵ  по модулю
"""
def f(x):
    return x**2 * np.sin(x)


def f_dash(x):
    return x * (2 * np.sin(x) + x * np.cos(x))


def gradient_descent_step(f_dash, x, alpha=0.001):
    f_dash_x = f_dash(x)
    delta_x = alpha*f_dash_x
    x_new = x - delta_x
    return x_new


def gradient_descent(f, f_dash, x, alpha=0.001, epsilon=0.01):
    y = f(x)
    xs = [x]
    ys = [y]

    while True:
        x = gradient_descent_step(f_dash, x, alpha)
        y = f(x)
        previous_y = ys[-1]

        delta_y = np.abs(y - previous_y)
        xs.append(x)
        ys.append(y)

        if delta_y < epsilon:
            print(x, y)
            break


gradient_descent(f, f_dash, 3)