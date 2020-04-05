

def fibonacci_gen(num):
    num = int(input('Please enter a number: '))
    a = 1
    b = 1
    for i in range(num):
        yield a
        a,b = b, a+b

for num in fibonacci_gen(1):
    print(num)


