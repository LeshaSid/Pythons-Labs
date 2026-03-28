import matplotlib.pyplot as plt
from numpy import *
from math import pi

def to_radians(num):
    return num*(pi/180)

def f(x):
    return e**(cos(x)) + log((cos(0.6*x))**2 + 1) * sin(x)

def h(x):
    return -log((cos(x) + sin(x))**2 + 2.5) + 10

ls_x = [to_radians(i) for i in range(-360, 360)]
ls_f_x = [f(x) for x in ls_x]
ls_h_x = [h(x) for x in ls_x]

plt.plot(ls_x, ls_f_x)
plt.xlabel('х')
plt.ylabel('y')
plt.title('y = e^(cos(x)) + ln((cos(0.6*x))^2 + 1) * sin(x)')
plt.show()

plt.plot(ls_x, ls_h_x)
plt.xlabel('х')
plt.ylabel('y')
plt.title('y = -ln((cos(x) + sin(x))^2 + 2.5) + 10')
plt.show()


