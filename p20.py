N=100
l=[1]
for q in range(1,N+1):
	carry=0
	for i in range(len(l)):
		x=l[i]*q + carry
		l[i]=x%10
		carry=x//10
	if carry>0:
		l = l+[int(x) for x in str(carry)[::-1]]
print(sum(l))