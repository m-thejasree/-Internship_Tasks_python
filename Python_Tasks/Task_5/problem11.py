# Problem11 : Text Wrap

## Hackerrank Link : https://www.hackerrank.com/challenges/text-wrap/problem

def wrap(string, max_width):
    result = ""
    for i in range(0, len(string), max_width):
        result += string[i:i + max_width] + "\n"
    return result.rstrip("\n")