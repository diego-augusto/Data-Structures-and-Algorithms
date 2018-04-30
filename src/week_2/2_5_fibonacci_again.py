# Uses python3


def pisano_perid_naive(n):

    fib1 = 0
    fib2 = 1

    pisano_perid = [0, 1]

    while True:
        fib1, fib2 = fib2, (fib1 + fib2) % n
        if fib1 == 0 and fib2 == 1:
            return len(pisano_perid) - 1
        pisano_perid.append(fib2)

def fibo_list(n):
    
    if n <= 1:
        return n

    fib1 = 0
    fib2 = 1

    for i in range(2, n + 1):
        fib1, fib2 = fib2, fib1 + fib2

    return fib2


numbers = [int(x) for x in input().split()]
pisano = pisano_perid_naive(numbers[1])
new_modulo = numbers[0] % pisano

print(fibo_list(new_modulo) % numbers[1])
