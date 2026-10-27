# problem3 - Mutations

## Hackerrank Link - https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    s = ""
    for i in l:
        s = s+i
    return s