# Problem 8 - Tuples

## Hackerrank Link : https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))

    x = 0x345678
    multiplier = 1000003
    length = len(t)

    for i, value in enumerate(t):
        x = ((x ^ value) * multiplier) & 0xFFFFFFFFFFFFFFFF
        multiplier += 82520 + 2 * (length - i - 1)

    x = (x + 97531) & 0xFFFFFFFFFFFFFFFF

    if x >= 2**63:
        x -= 2**64

    if x == -1:
        x = -2

    print(x)