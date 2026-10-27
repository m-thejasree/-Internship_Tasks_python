# Problem15 - Set .difference() Operation


## Hackerrank Link : https://www.hackerrank.com/challenges/py-set-difference-operation/problem

if __name__ == '__main__':
    n = int(input())
    english = set(map(int, input().split()))

    b = int(input())
    french = set(map(int, input().split()))

    result = english.difference(french)

    print(len(result))