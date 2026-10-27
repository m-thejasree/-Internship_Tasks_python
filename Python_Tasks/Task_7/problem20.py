# Problem19 - Super Reduced String



## Hackerrank Link :https://www.hackerrank.com/challenges/reduced-string/problem

s = input()
result = []

for ch in s:
    if result and result[-1] == ch:
        result.pop()
    else:
        result.append(ch)

if result:
    print("".join(result))
else:
    print("Empty String")