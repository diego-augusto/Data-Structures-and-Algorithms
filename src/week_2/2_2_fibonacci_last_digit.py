# Uses python3

def fibo_last_digit(n):
    
    if n <= 1:
        return n

    fib1 = 0 % 10
    fib2 = 1 % 10

    for i in range(2, n + 1):
        fib1, fib2 = fib2, (fib1 + fib2) % 10

    return fib2

n = int(input())

print(fibo_last_digit(n))