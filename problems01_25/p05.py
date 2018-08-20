from peutil import *

bigdict = {}

for n in range(2,20):
	d = countdict(primefac(n))
	for k,v in d.items():
		if k in bigdict:
			bigdict[k] = max(bigdict[k],d[k])
		else:
			bigdict[k] = d[k]

print(prod([x**y for x,y in bigdict.items()]))