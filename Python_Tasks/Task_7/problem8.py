# Problem8 - Gemstones


## Hackerrank Link : https://www.hackerrank.com/challenges/gem-stones/problem

n = int(input())

common = set(input())

for i in range(n - 1):
    rock = set(input())
    common = common.intersection(rock)

print(len(common))