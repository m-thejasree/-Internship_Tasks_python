# Problem 11 - String Formatting

## Hackerrank Link :https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    width = len(bin(number)) - 2  # width of largest binary number

    for i in range(1, number + 1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]

        print(f"{deci:>{width}} {octa:>{width}} {hexa:>{width}} {bina:>{width}}")