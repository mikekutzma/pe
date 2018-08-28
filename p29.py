from peutil import *

def stringlist(l):
    return '.'.join([str(x) for x in l])

N=100
uniqueset = set()
for a in range(2,N+1):
    for b in range(2,N+1):
        uniqueset.add(stringlist(sorted(primefac(a)*b)))
print(len(uniqueset))