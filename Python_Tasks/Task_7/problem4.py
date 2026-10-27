# Problem4 - Funny String


## Hackerrank Link : https://www.hackerrank.com/challenges/funny-string/problem

q = int(input())

for _ in range(q):
    s = input()
    r = s[::-1]

    funny = True

    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(r[i]) - ord(r[i - 1])):
            funny = False
            break

    if funny:
        print("Funny")
    else:
        print("Not Funny")