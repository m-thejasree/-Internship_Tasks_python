# Problem7 - Alphabet Rangoli


## Hackerrank LInk : https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    letters = "abcdefghijklmnopqrstuvwxyz"
    width = 4 * size - 3
    lines = []
    for i in range(size):
        row_letters = []
        for j in range(size-1, size-i-2, -1):
            row_letters.append(letters[j])
        for j in range(size-i, size):
            row_letters.append(letters[j])
        row = '-'.join(row_letters)
        lines.append(row.center(width, '-'))
    for i in range(size-2, -1, -1):
        lines.append(lines[i])
    for line in lines:
        print(line)