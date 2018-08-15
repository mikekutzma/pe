class Collatz:
	def __init__(self):
		self.colldict = {1:1}

	def getlen(self,x):
		if x in self.colldict:
			return self.colldict[x]
		l = 1+self.getlen(self.nextcol(x))
		self.colldict[x]=l
		return l

	def nextcol(self,x):
		if x%2==0:
			return int(x/2)
		return 3*x + 1

	def hasvals(self,n):
		return set(range(1,n))<set(self.colldict.keys())


def colinv(x):
	l = [int(x*2)]
	a = (x-1)/3
	if int(a)==a and a>1:
		l=l+[int(a)]
	return l

collist = [[1]]
for i in range(1,20):
	templist = [x for y in [colinv(z) for z in collist[i-1]] for x in y]
	collist.append(templist)

for i in collist:
	print(i)