sum1 = 0
sum2 = 0

#last number in range() is not included in sum
for i in range(1, 101):
    sum1 += i**2
    sum2 += i

print(sum1)
print(sum2)
print(sum2**2)
ans = sum2**2 - sum1
print("The difference of sums is : ", ans)


