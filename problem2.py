f1=1
f2=1
sum=0
while f2<=4000000:
    s=f1+f2
    f1=f2
    f2=s
    if s%2==0:
        print(s)
        sum+=s
print("The sum is: ",sum)