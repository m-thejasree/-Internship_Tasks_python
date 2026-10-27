# Problem1 - Find the Runner-Up Score!


## Hackerrank LInk : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = int(input())
arr = map(int, input().split())
l = sorted(list(set(arr)))
print(l[-2])