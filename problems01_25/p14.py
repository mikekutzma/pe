def nextcol(x):
	if x%2==0:
		return int(x/2)
	return int(3*x + 1)

maxl=0
maxi=0
N=1000000
for i in range(1,N):
	n=i
	l=1
	while n>1:
		n=nextcol(n)
		l=l+1
	if l>maxl:
		maxl,maxi=l,i
print(maxi)