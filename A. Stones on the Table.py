n = int(input())
st = input()
stones = 0
for i in range(1, len(st)):
    if st[i] == st[i - 1]:
        stones +=1

print(stones)
