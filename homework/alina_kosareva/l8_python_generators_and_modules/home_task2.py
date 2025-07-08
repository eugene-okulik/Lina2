import sys


sys.set_int_max_str_digits(100001)

def fibonacci_generator():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


gen = fibonacci_generator()

for i in range(100001):
    n = next(gen)
    if i in (5, 200, 1000, 100000):
        print(n)
