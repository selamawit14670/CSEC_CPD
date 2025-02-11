st1 = input()
st2 = input()
st1 = st1.lower()
st2 = st2.lower()
ans = 0
for i in range(len(st1)):
    asci_1 = ord(st1[i])
    asci_2 = ord(st2[i])
    if asci_1 > asci_2:
        ans = 1
        break
    elif asci_1 < asci_2:
        ans = -1
        break
    else:
        continue
print(ans)
