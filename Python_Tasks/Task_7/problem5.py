# Problem5 - Alternating Characters


## Hackerrank Link : https://www.hackerrank.com/challenges/alternating-characters/problem

q = int(input())

for _ in range(q):
    s = input()
    count = 0

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1

    print(count)