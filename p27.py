from peutil import *
maxcoeff = 1000

def quad(n,a,b):
    return n**2 + a*n + b

blist = [x for x in range(2,maxcoeff) if isprime(x)]
alist = [x  for x in range(-maxcoeff+1,maxcoeff) if x%2==1]

maxlen = 0
maxcoeffs = 1,1
for a in alist:
    for b in blist:
        n=0
        while isprime(quad(n,a,b)):
            n=n+1
        if n>maxlen:
            maxlen=n
            maxcoeffs = a,b
            print('New max =',n,a,b)

print(maxlen,maxcoeffs,prod(maxcoeffs))
