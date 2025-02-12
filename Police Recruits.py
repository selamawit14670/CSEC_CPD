n = int(input())
action = list(map(int, input().split()))
 
a = 0
b = 0
 
for i in range(n):
    if action[i] < 0:
        if a > 0:
            a += action[i]
            if a < 0:
                b += abs(a)
                a = 0
        else:
            b += abs(action[i])
    else:
        a += action[i]
 
print(b)
