# Problem9 - Beautiful Binary String


## Hackerrank Link : https://www.hackerrank.com/challenges/beautiful-binary-string/problem

n = int(input())
s = input()

count = 0
i = 0

while i < len(s) - 2:
    if s[i:i + 3] == "010":
        count += 1
        i += 3
    else:
        i += 1

print(count)