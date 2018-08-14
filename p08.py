from peutil import * 
with open('data/p8.txt') as f:
	data = [int(y) for y in list(''.join([x.strip() for x in f.readlines()]))]

N=13
print(max([prod(data[i:i+N]) for i in range(len(data)-N)]))
