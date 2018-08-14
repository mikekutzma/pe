import math
m=600851475143
def isprime(n):
	if n<2:
		return False
	i=2
	while i<=math.sqrt(n):
		if n%i==0:
			return False
		i+=1
	return True
maxprime=1
while not isprime(m):
	for i in range(2,m):
		if (isprime(i) and m%i==0):
			maxprime = max(maxprime,i)
			m=int(m/i)
			break
maxprime = max(maxprime,m)
print(maxprime)
