
n = list(map(int, input().split()))
a = input()
cal = 0
for i in range(len(a)):
    int_a = int(a[i])
    cal += n[int_a - 1]
 
print(cal)
