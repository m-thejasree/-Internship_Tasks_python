# Problem18 - String Construction


## Hackerrank Link : https://www.hackerrank.com/challenges/string-construction/problem

q = int(input())

for _ in range(q):
    s = input()
    seen = set()
    cost = 0

    for ch in s:
        if ch not in seen:
            cost += 1
            seen.add(ch)

    print(cost)

