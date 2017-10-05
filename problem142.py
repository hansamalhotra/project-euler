#why didnt I think of this before omg
import math
sum=3000000
def f(p):
    for i in range(int(math.sqrt(p)),1000):
        yield i**2
for c in f(1):
    for b in f(c):
        for a in f(b):
            if a>b and b>c:
                if math.sqrt(a-b)%1==0 and math.sqrt(b-c)%1==0 and math.sqrt(a-c)%1==0:
                    s=(a+b+c)/2
                    if s<sum:
                        sum=s
                        x=a+b-c
                        y=a+c-b
                        z=b+c-a



print(sum)
print(x)
print(y)
print(z)





