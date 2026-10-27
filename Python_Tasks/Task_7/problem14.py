# Problem14 - Anagram


## Hackerrank Link : https://www.hackerrank.com/challenges/anagram/problem

from collections import Counter

q = int(input())

for _ in range(q):
    s = input()

    if len(s) % 2 != 0:
        print(-1)
    else:
        mid = len(s) // 2

        s1 = s[:mid]
        s2 = s[mid:]

        count1 = Counter(s1)
        count2 = Counter(s2)

        changes = 0

        for ch in count1:
            if count1[ch] > count2[ch]:
                changes += count1[ch] - count2[ch]

        print(changes)