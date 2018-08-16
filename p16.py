M=2
N=1000
l=[1]
for q in range(N):
	carry=0
	for i in range(len(l)):
		x=l[i]*M
		l[i]=x%10 + carry
		carry=x//10
	if carry>0:
		l = l+[int(x) for x in str(carry)[::-1]]
print(sum(l))