from peutil import *
n=100
print(sum([x*y for x in range(1,n+1) for y in range(1,n+1) if x!=y]))
