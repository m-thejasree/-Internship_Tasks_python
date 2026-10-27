# Problem19 - Weighted Uniform Strings


## Hackerrank Link : https://www.hackerrank.com/challenges/weighted-uniform-string/problem

s = input()
n = int(input())
queries = []

for i in range(n):
    queries.append(int(input()))

weights = set()
count = 0
previous = ''

for ch in s:
    if ch == previous:
        count += 1
    else:
        count = 1

    weight = (ord(ch) - ord('a') + 1) * count
    weights.add(weight)
    previous = ch

for q in queries:
    if q in weights:
        print("Yes")
    else:
        print("No")


