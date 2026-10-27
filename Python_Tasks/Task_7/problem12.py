# Problem12 - Making Anagrams


## Hackerrank Link : https://www.hackerrank.com/challenges/making-anagrams/problem

from collections import Counter

s1 = input()
s2 = input()

count1 = Counter(s1)
count2 = Counter(s2)

deletions = 0

for ch in set(s1 + s2):
    deletions += abs(count1[ch] - count2[ch])

print(deletions)