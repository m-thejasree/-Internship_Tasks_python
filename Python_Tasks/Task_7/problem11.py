# Problem11 - Two Strings


## Hackerrank Problem : https://www.hackerrank.com/challenges/two-strings/problem

q = int(input())

for _ in range(q):
    s1 = input()
    s2 = input()

    if set(s1) & set(s2):
        print("YES")
    else:
        print("NO")