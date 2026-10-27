# Problem2 - The Captain's Room


## Hackerrank Link : https://www.hackerrank.com/challenges/py-the-captains-room/problem

K = int(input())
rooms = list(map(int, input().split()))

room_set = set(rooms)

captain_room = (sum(room_set) * K - sum(rooms)) // (K - 1)

print(captain_room)