def fib(n,a=1,b=2):
	if a<n:
		yield a
	while b<n:
		yield b
		a,b=b,a+b

print(sum([x for x in fib(4000000) if x%2==0]))
