# Uses python3


def gcd_euclidean(a, b):

    if b == 0:
        return a

    return gcd_euclidean(b, a % b)


def lcm(a, b):
    return a * int(b / gcd_euclidean(a, b))


numbers = [int(x) for x in input().split()]

print(lcm(numbers[0], numbers[1]))
