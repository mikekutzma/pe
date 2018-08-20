with open('data/p13.txt') as f:
	data = [[int(x) for x in list(line.strip())] for line in f.readlines()]

t = []
for i in list(range(len(data[0])))[::-1]:
	s = sum([x[i] for x in data])
	t.append(s)
t.append(0)
for i in range(len(t)-1):
	x = t[i]
	t[i]=x%10
	t[i+1]+=x//10
print("".join([str(x) for x in t[::-1]])[:10])