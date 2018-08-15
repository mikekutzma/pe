from peutil import * 
def dothis(N):
	i=1
	while True:
		if len(factors(int((i*(i+1))/2)))>N:
			return i
		i+=1
i=dothis(500)
print(int((i*(i+1))/2))
