import math

def fib(n,a=1,b=2):
	if a<n:
		yield a
	while b<n:
		yield b
		a,b=b,a+b

def isprime(n):
	if n<2:
		return False
	i=2
	while i<=math.sqrt(n):
		if n%i==0:
			return False
		i+=1
	return True

def ispalindrome(x):
	return str(x)==str(x)[::-1]

def primefac(x):
	if type(x)!=int:
		raise TypeError('Value must be integer for prime factorization.')
	plist = []
	if x<2:
		return plist
	while not isprime(x):
		for i in range(2,x):
			if isprime(i) and x%i==0:
				plist.append(i)
				x=int(x/i)
				break
	plist.append(x)
	return plist

def countdict(l):
	if type(l) not in (list,str):
		raise TypeError('Type must be list or str for countdict.')
	return {x:len([y for y in l if y==x]) for x in list(set(l))}

def prod(l):
	p = 1
	for x in l:
		p=p*x
	return p