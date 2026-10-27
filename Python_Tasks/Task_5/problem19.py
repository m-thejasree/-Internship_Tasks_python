# Problem19 - Merge the Tools!


## Hackerrank  Link : https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        sub = string[i:i+k]
        result = ""

        for ch in sub:
            if ch not in result:
                result += ch

        print(result)


