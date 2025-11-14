import matplotlib.pyplot as plt
from numpy import *
from math import pi

def f(x):
    denominator = x**2 - 9
    if denominator == 0:
        return None
    else:
        return 5/denominator

ls_x = [i for i in range(-10, 10)]
ls_f_x = [f(x) for x in ls_x]

plt.plot(ls_x, ls_f_x)
plt.xlabel('х')
plt.ylabel('y')
plt.title('y = 5/(x^2 - 9)')
plt.show()



