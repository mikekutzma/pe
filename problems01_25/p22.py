with open('data/p22.txt') as f:
	names = [x.strip('"') for x in f.read().split(',')]
names.sort()
s=0
for i,name in enumerate(names):
	s = s+(sum([ord(x)-64 for x in name])*(i+1))
print(s)