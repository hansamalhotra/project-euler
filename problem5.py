#smallest multiple problem

# generates all multiples of common factors of numbers from 1 to 20 to narrow the search
def smultiple():
    for i in range(1,1000):
        yield i*2*3*5*7*11*13*17*19


for x in smultiple():
    flag = True
    for i in range(1,20):
        if (x/i)%1 == 0:
            continue
        else:
            flag = False    #breaks out of the loop if x is not divisible by any i
            break
    if flag:
        m = x
        break
print(m)

