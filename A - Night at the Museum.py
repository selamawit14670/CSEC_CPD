b = input()
shortest = 0
start = 'a'
 
for i in range(len(b)):
    forward = abs(ord(b[i])-ord(start))
    reverse = 26 - forward
    if forward > reverse:
        shortest += reverse
    else:
        shortest += forward
    start = b[i]
print(shortest)
