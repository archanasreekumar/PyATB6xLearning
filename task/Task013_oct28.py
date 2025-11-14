# Skip numbers divisible by 3, from (0,100)

n = 100

for i in range(n+1):
    if i % 3 !=0:
        print(i)