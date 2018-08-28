import math


def fib(n, a=1, b=2):
    if a < n:
        yield a
    while b < n:
        yield b
        a, b = b, a + b


def isprime(n):
    if n < 2:
        return False
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


def ispalindrome(x):
    return str(x) == str(x)[::-1]


def primefac(x):
    if type(x) != int:
        raise TypeError('Value must be integer for prime factorization.')
    plist = []
    if x < 2:
        return plist
    while not isprime(x):
        for i in range(2, x):
            if isprime(i) and x % i == 0:
                plist.append(i)
                x = int(x / i)
                break
    plist.append(x)
    return plist


def factors(m):
    p = [1] + primefac(m)
    pold = []
    while (p != pold):
        pold = p
        p = sorted(list(set([x * y for x in p for y in p if x * y <= m and m % (x * y) == 0])))
    return p


def countdict(l):
    if type(l) not in (list, str):
        raise TypeError('Type must be list or str for countdict.')
    return {x: len([y for y in l if y == x]) for x in list(set(l))}


def prod(l):
    p = 1
    for x in l:
        p = p * x
    return p


def primegenerator(n, maxp=None):
    plist = []
    m = 2
    if (n < 0 and maxp == None):
        return
    while (len(plist) < n or n < 0) and (maxp == None or m < maxp):
        p = True
        for j in plist:
            if m % j == 0:
                p = False
                break
            if j > math.sqrt(m):
                break
        if p:
            plist.append(m)
            yield m
        m = m + 1
