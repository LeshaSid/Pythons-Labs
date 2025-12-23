import numpy as np

lenthes = np.array([int(i) for i in input("Длины: ").split()])
speeds = np.array([int(i) for i in input("Скорость: ").split()])
k = int(input("k = "))
p = int(input("p = "))

path_lengths = lenthes[k-1:p]
path_speeds = speeds[k-1:p]

S = sum(path_lengths)
T = sum(path_lengths / path_speeds)
V = S / T 

print(f"S = {S} км", end=", ")
print(f"T = {T:.2f} час", end=", ")
print(f"V = {V:.2f} км/ч")