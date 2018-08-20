from peutil import * 
with open('data/p11.txt') as f:
	data = [[int(y) for y in x.strip().split()] for x in f.readlines()]

N=4
h = max([max([prod(row[i:i+N]) for i in range(len(row)-N)]) for row in data])
vdata = [[row[i] for row in data] for i in range(len(data[0]))]
v = max([max([prod(row[i:i+N]) for i in range(len(row)-N)]) for row in vdata])
boxes = [[row[j:j+N] for row in data[i:i+N]] for i in range(len(data)-N+1) for j in range(len(data[0])-N+1)]
d1 = max([ prod([box[i][i] for i in range(len(box))]) for box in boxes ])
d2 = max([ prod([box[i][len(box[i])-i-1] for i in range(len(box))]) for box in boxes ])
print(max(h,v,d1,d2))