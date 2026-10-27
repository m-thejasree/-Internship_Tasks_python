# Problem1 - Set .symmetric_difference() Operation


## Hackerrank Link : https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

M = int(input())
set_M = set(map(int, input().split()))

N = int(input())
set_N = set(map(int, input().split()))

result = set_M.symmetric_difference(set_N)

print(len(result))