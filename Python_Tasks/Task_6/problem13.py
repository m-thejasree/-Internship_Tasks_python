# Problem 13 - Set .union() Operation

## Hackerrank Link : https://www.hackerrank.com/challenges/py-set-union/problem

if __name__ == '__main__':
    n = int(input())
    english = set(map(int, input().split()))

    b = int(input())
    french = set(map(int, input().split()))

    result = english.union(french)

    print(len(result))
