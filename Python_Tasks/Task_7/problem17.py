# Problem17 - Separate the Numbers


## Hackerrank Link : https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separateNumbers(s):
    for i in range(1, len(s) // 2 + 1):
        first = int(s[:i])
        number = first
        result = ""

        while len(result) < len(s):
            result += str(number)
            number += 1

        if result == s:
            print("YES", first)
            return

    print("NO")


q = int(input())

for _ in range(q):
    s = input().strip()
    separateNumbers(s)