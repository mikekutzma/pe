N=1000
fibla=[1]
fiblb=[1]
n=2
while len(fiblb)<N:
	carry=0
	temp = [fibla[i]+fiblb[i] if i<len(fibla) else fiblb[i] for i in range(len(fiblb))]
	for i in range(len(temp)):
		x=temp[i]+carry
		temp[i]=x%10
		carry=x//10
	if carry>0:
		temp = temp+[int(x) for x in str(carry)[::-1]]
	fibla = fiblb
	fiblb = temp
	n=n+1

print(n,"".join(str(x) for x in fiblb[::-1]))
