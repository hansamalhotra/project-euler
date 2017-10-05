
import random

a = 1
for i in range(2 , 1000000):
    m = random.randrange(1 , i)  # 3 tries for increased accuracy
    n = random.randrange(1 , i)
    k = random.randrange(1 , i)
    if (m**(i-1))% i == 1 and n**(i-1) % i == 1 and (k**(i-1))%i ==1:
        a += 1
        if a == 10001 or a == 10000 or a == 10002:
            print("The prime number is: ", i)

            break
