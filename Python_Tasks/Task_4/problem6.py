# Problem6 - 

## Hackerrank Link:https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = int(input())
arr = list(map(int, input().split()))
a = sorted(list(set(arr)))
print(a[-2])
    