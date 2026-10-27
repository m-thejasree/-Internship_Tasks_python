# Problem - 1

# Hackerrank Link : https://www.hackerrank.com/challenges/py-if-else/problem

n = int(input().strip())
if n %2 == 1:
    print("Weird")
if n %2 == 0 and n in [2,3,4,5]:
    print("Not Weird")
if n % 2 == 0 and n in range(6,21):
    print("Weird")
if n%2 == 0 and n > 20:
    print("Not Weird")
    