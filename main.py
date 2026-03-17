import math

# #1. Compute sum of digits of an integer (no string conversion).
def sum_digits(n):
    # n=256
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
n = int(input("Enter a number: "))
print("Sum of Digits ", sum_digits(n))


# 2. Compute product of digits (no string).
def product_digits(n):
    p = 1
    while n > 0:
        p *= n % 10
        n //= 10
    return p

n = int(input("Enter number: "))
print("Product of Digits : ", product_digits(n))


# 3. Reverse a number (no string).
def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev

n = int(input("Enter number: "))
print("Reverse Number is :",reverse_number(n))

# 4. Check palindrome number (no string).
def is_palindrome(n):
    return n == reverse_number(n)
n = int(input("Enter number: "))
print("Palindrome: ",is_palindrome(n))


# 5. Check Armstrong number (general n-digit).
def is_armstrong(n):
    temp = n
    digits = 0
    while temp > 0:
        digits += 1
        temp //= 10

    temp = n
    s = 0
    while temp > 0:
        s += (temp % 10) ** digits
        temp //= 10

    return s == n

n = int(input("Enter number: "))
print("Armstrong: ",is_armstrong(n))

# 6. Check Perfect number.
def is_perfect(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n

n = int(input("Enter number: "))
print(is_perfect(n))


# 7. Check Strong number (sum of factorial of digits).
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def is_strong(n):
    temp = n
    s = 0
    while temp > 0:
        s += factorial(temp % 10)
        temp //= 10
    return s == n

n = int(input("Enter number: "))
print(is_strong(n))


# 8. Check Harshad/Niven number.
def is_harshad(n):
    return n % sum_digits(n) == 0

n = int(input("Enter number: "))
print(is_harshad(n))


# 9. Check Automorphic number (ends with its square).
def is_automorphic(n):
    sq = n * n
    temp = n
    while temp > 0:
        if temp % 10 != sq % 10:
            return False
        temp //= 10
        sq //= 10
    return True

n = int(input("Enter number: "))
print(is_automorphic(n))


# 10. Check Neon number (sum digits of square equals number).
def is_neon(n):
    return sum_digits(n * n) == n

n = int(input("Enter number: "))
print(is_neon(n))


# 11. Find GCD using Euclid algorithm.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(gcd(a, b))


# 12. Find LCM using GCD.
def lcm(a, b):
    return a * b // gcd(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(lcm(a, b))


# 13. Find HCF of three numbers.
def hcf_three(a, b, c):
    return gcd(gcd(a, b), c)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
print(hcf_three(a, b, c))


# 14. Compute power a^b using loop (no **).
def power(a, b):
    res = 1
    for _ in range(b):
        res *= a
    return res

a = int(input("Enter base: "))
b = int(input("Enter exponent: "))
print(power(a, b))


# 15. Compute power a^b mod m (fast exponentiation).
def power_mod(a, b, m):
    res = 1
    a %= m
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        a = (a * a) % m
        b //= 2
    return res

a = int(input("Enter base: "))
b = int(input("Enter exponent: "))
m = int(input("Enter modulus: "))
print(power_mod(a, b, m))


# 16. Find prime factors of a number.
def prime_factors(n):
    i = 2
    while i * i <= n:
        while n % i == 0:
            print(i, end=" ")
            n //= i
        i += 1
    if n > 1:
        print(n)

n = int(input("Enter number: "))
prime_factors(n)


# 17. Check prime number (optimized up to √n).
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter number: "))
print(is_prime(n))


# 18. Print primes in range using Sieve of Eratosthenes.
def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False

    return [i for i in range(2, n + 1) if prime[i]]

n = int(input("Enter limit: "))
print(sieve(n))


# 19. Find twin primes in a range.
def twin_primes(n):
    primes = sieve(n)
    return [(p, p + 2) for p in primes if p + 2 in primes]

n = int(input("Enter limit: "))
print(twin_primes(n))


# 20. Compute factorial using recursion.
def fact_rec(n):
    if n == 0:
        return 1
    return n * fact_rec(n - 1)

n = int(input("Enter number: "))
print(fact_rec(n))


# 21. Compute nCr (combinations) using factorial + simplification.
def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

n = int(input("Enter n: "))
r = int(input("Enter r: "))
print(nCr(n, r))


# 22. Compute nPr (permutations).
def nPr(n, r):
    return factorial(n) // factorial(n - r)

n = int(input("Enter n: "))
r = int(input("Enter r: "))
print(nPr(n, r))


# 23. Compute sum of series: 1 + 1/2 + 1/3 + … + 1/n.
def harmonic_sum(n):
    s = 0
    for i in range(1, n + 1):
        s += 1 / i
    return s

n = int(input("Enter n: "))
print(harmonic_sum(n))


# 24. Compute sin(x) using Taylor series (n terms).
import math

def sin_taylor(x, n):
    x = math.radians(x)
    s = 0
    for i in range(n):
        s += ((-1) ** i) * (x ** (2*i + 1)) / factorial(2*i + 1)
    return s

x = float(input("Enter angle: "))
n = int(input("Enter terms: "))
print(sin_taylor(x, n))


# 25. Compute e^x using Taylor series (n terms).
def exp_taylor(x, n):
    s = 1
    for i in range(1, n):
        s += (x ** i) / factorial(i)
    return s

x = float(input("Enter x: "))
n = int(input("Enter terms: "))
print(exp_taylor(x, n))
