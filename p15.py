N=20
tree = []
for i in range(N):
	tree.append([1])
	for j in range(1,i+1):
		tree[i].append(tree[i-1][j]+tree[i][j-1])
	tree[i].append(tree[i][-1]*2)
print(tree[-1][-1])
