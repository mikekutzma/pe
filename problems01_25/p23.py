from peutil import *

N = 28123
abdict = {i:sum(factors(i)[:-1]) for i in range(1,N)}
abnums = {i:k for i,k in abdict.items() if k>i}

absums = {i for i in range(1,N) if (len({i-j for j in abnums}&{j for j in abnums})==0)}
print(sum(absums))