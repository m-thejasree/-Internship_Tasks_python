# Problem 10 - Designer Door Mat

## Hackerrank Link : https://www.hackerrank.com/challenges/designer-door-mat/problem

if __name__ == '__main__':
    n, m = map(int, input().split())

    # Top cone
    for i in range(1, n, 2):
        print(('.|.' * i).center(m, '-'))

    # Welcome message
    print('WELCOME'.center(m, '-'))

    # Bottom cone
    for i in range(n - 2, 0, -2):
        print(('.|.' * i).center(m, '-'))