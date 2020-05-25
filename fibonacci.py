

def fib(num):
    a = 0
    b =1

    sum = 0

    for i in range(num):
        yield a
        sum = a + b

        a = b
        b = sum

g = fib(8)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
