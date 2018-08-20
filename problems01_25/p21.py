from peutil import *

def getam(x):
	l = factors(x)
	return sum(l[:-1])

d = {}
for i in range(1,10000):
	d[i]=getam(i)
print(sum([k for k in d if d[k] in d and d[k]!=k and d[d[k]]==k]))