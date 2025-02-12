n, h = map(int, input().split())
a = list(map(int, input().split()))
sum = 0
for i in range(n):
    if a[i] > h:
        sum = sum + 2
    else:
        sum = sum + 1
print(sum)
