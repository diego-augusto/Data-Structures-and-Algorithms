# Uses python3


def gcd_naive(a, b):
    best = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            best = i

    return best


def gcd_euclidean(a, b):

    if b == 0:
        return a

    return gcd_euclidean(b, a % b)


numbers = [int(x) for x in input().split()]

print(gcd_euclidean(numbers[0], numbers[1]))
