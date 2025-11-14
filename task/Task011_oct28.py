# Print even numbers between 1 and 20

n = 20

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)

[print(i) for i in range(1, n+1) if i % 2 != 0]
