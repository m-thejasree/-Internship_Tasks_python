# Problem16 - collections.Counter()


## Hackerrank Link : https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

x = int(input())
shoe_sizes = list(map(int, input().split()))

inventory = Counter(shoe_sizes)

n = int(input())
money = 0

for i in range(n):
    size, price = map(int, input().split())

    if inventory[size] > 0:
        money += price
        inventory[size] -= 1

print(money)