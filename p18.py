with open('data/p18.txt') as f:
	data = [[int(y) for y in x.strip().split(' ')] for x in f.readlines()]

for i in range(len(data)-1)[::-1]:
	for j in range(len(data[i])):
		data[i][j] = data[i][j]+max(data[i+1][j],data[i+1][j+1])
print(data[0][0])