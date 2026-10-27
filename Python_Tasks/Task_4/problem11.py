# problem11 - String Validators

# Hacerrank Link : https://www.hackerrank.com/challenges/string-validators/problem

s = input()
print(any(c.isalnum() for c in s))

    # Check for alphabetical characters
print(any(c.isalpha() for c in s))

    # Check for digits
print(any(c.isdigit() for c in s))

    # Check for lowercase characters
print(any(c.islower() for c in s))

    # Check for uppercase characters
print(any(c.isupper() for c in s))