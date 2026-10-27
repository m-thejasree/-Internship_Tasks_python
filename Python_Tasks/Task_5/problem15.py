# Problem15 - Lists


## Hackerrank Link : https://www.hackerrank.com/challenges/python-lists/problem

N = int(input())
my_list = []

for i in range(N):
    cmd = input()  # Read one command

        # If the command is insert
    if "insert" in cmd:
        parts = cmd.split()
        index = int(parts[1])
        value = int(parts[2])
        my_list.insert(index, value)

        # If the command is print
    elif cmd == "print":
        print(my_list)

        # If the command is remove
    elif "remove" in cmd:
        parts = cmd.split()
        value = int(parts[1])
        my_list.remove(value)

        # If the command is append
    elif "append" in cmd:
        parts = cmd.split()
        value = int(parts[1])
        my_list.append(value)

    elif cmd == "sort":
        my_list.sort()

        # If the command is pop
    elif cmd == "pop":
        my_list.pop()

        # If the command is reverse
    elif cmd == "reverse":
        my_list.reverse()
