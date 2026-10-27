# problem13 - Sherlock and the Valid String


## Hackerrank Link : https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

from collections import Counter

s = input()
freq = Counter(s)
counts = list(freq.values())

unique_counts = set(counts)

if len(unique_counts) == 1:
    print("YES")
else:
    count_freq = Counter(counts)

    if len(count_freq) == 2:
        (f1, n1), (f2, n2) = count_freq.items()

        if (f1 == 1 and n1 == 1) or (f2 == 1 and n2 == 1):
            print("YES")
        elif (abs(f1 - f2) == 1) and (n1 == 1 or n2 == 1):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")