L, B = [int(x) for x in input(). split()]
n = 0
while B >= L:
    n += 1
    B = B * 2
    L = L * 3
print(n)
