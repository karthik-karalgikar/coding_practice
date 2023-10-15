def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    a = 12
    b = 9
    print("The GCD of the two numbers is", gcd(a, b))

'''
TRACING
a = 12 b = 9
gcd(12, 9)
b != 0
returns gcd(9, 12 % 9)
       -> gcd(9, 3)
goes back to function
gcd(9,3)
returns gcd(3, 9 % 3)
       ->gcd(3, 0)
goes back to function
b == 0
returns a, i.e., 3
GCD is 3
'''
