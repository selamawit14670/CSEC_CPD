n = int(input())
s = input()
anton = 0
danik = 0
for i in range(n):
    if s[i] == "A":
        anton = anton + 1
    elif s[i] == "D":
        danik = danik + 1
if anton > danik:
    print("Anton")
elif danik > anton:
    print("Danik")
else:
    print("Friendship")
