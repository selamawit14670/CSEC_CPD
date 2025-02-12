a = input()
b = input()
i = 0
pos = 1
for j in range(len(b)):
    if a[i] == b[j]:
        pos += 1
        i += 1
print(pos)
