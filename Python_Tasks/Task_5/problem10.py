# Problem10 - sWAP cASE


## Hackerrank Link : https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    string = ""
    for i in s:
        if i == i.lower():
            string = string + i.upper()
        elif i == i.upper():
            string = string+i.lower() 
        else:
            string = string+i
    return string
        