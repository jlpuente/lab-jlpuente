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
    for i in range(n):
        resultado = fibonacci(i)
        print(i, resultado)


