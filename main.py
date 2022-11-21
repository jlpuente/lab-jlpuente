import argparse

cache = {}

def fibonacci(n):
    if n < 0:
        raise ValueError("n is lower than n")
    if n < 2:
        return n
    if n in cache:
        return cache[n]
    res = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = res
    return res

def print_fibonacci_n(n):
    parser = argparse.ArgumentParser(
        prog='Fibonacci calculator',
        description='Compute n-th Fibonacci')
    parser.add_argument('nth', type=int, help='The n-term of the fibonacci sucession')
    args = parser.parse_args()
    print(args.nth)

    for i in range(args.nth):
        resultado = fibonacci(i)
        print(i, resultado)

print_fibonacci_n(3)