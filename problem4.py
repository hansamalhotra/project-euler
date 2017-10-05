
for i in range(999,900,-1):
    for j in range(999,900,-1):
        a = i*j
        s = str(a)
        l = len(s)
        flag = True

        #this checks if the number is a palidrome using strings
        for k in range(l):
            if s[k]==s[l-k-1]:
                continue
            else:
                flag = False
                break
        #trying to break out of multiple loops here
        if flag:
            pal=a
            m = i
            n = j
            break
    if flag:
        break

print(pal)
print(m)
print(n)


