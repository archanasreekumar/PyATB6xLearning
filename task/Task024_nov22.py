# Create a framework base counter that counts test execution instances:

class count_test:
    count = 0
    def __init__(self):
        count_test.count +=1

t1 = count_test()
t2 = count_test()

print(count_test.count)

