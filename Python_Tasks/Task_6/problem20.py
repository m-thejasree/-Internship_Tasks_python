# Problem20 - Validating phone numbers


## Hackerrank LInk : https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com

import re

N = int(input())

for i in range(N):
    number = input().strip()

    if re.fullmatch(r'[789]\d{9}', number):
        print("YES")
    else:
        print("NO")