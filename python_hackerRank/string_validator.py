# Sample Input

# qA2
# Sample Output

# True
# True
# True
# True
# True


if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s)) # any alphabet and neumeric
    print(any(c.isalpha() for c in s)) # any alphabet
    print(any(c.isdigit() for c in s)) # any digit
    print(any(c.islower() for c in s)) # any lower case
    print(any(c.isupper() for c in s)) # any upper case