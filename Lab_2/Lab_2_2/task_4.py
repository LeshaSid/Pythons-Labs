def transpose(a):
    b = []
    n = len(a)
    m = len(a[0])
    for i in range(m):
        b.append([])
        for j in range(n):
            b[i].append(a[j][i])
    return b
n = int(input("Enter n: "))
m = int(input("Enter m: "))
a = []
for i in range(n):
    a.append([])
    for j in range(m):
        x = int(input(f"Enter x[{i}][{j}]: "))
        a[i].append(x)
print(a)
print(transpose(a))
