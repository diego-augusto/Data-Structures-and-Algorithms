# Uses python3

def fibo_rec(n):
    if n <= 1:
        return n
    return fibo_rec(n - 1) + fibo_rec(n - 2)


def fibo_list(n):

    if n <= 1:
        return n

    fib1 = 0
    fib2 = 1

    for i in range(2, n + 1):
        fib1, fib2 = fib2, fib1 + fib2

    return fib2


n = int(input())

print(fibo_list(n))
