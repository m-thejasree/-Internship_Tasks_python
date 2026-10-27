# Problem16 - Caesar Cipher


## Hackerrank Link : https://www.hackerrank.com/challenges/caesar-cipher-1/problem
n = int(input())
s = input()
k = int(input())

result = ""

for ch in s:
    if ch.isalpha():
        start = ord('A') if ch.isupper() else ord('a')
        new_char = chr((ord(ch) - start + k) % 26 + start)
        result += new_char
    else:
        result += ch

print(result)
