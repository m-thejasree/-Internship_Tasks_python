# Problem 14 - Set .intersection() Operation

## Hackerrank LInk : https://www.hackerrank.com/challenges/py-set-intersection-operation/problem


if __name__ == '__main__':
    n = int(input())
    english = set(map(int, input().split()))

    b = int(input())
    french = set(map(int, input().split()))

    result = english.intersection(french)

    print(len(result))
