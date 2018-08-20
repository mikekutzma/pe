N=10
nums = {str(i) for i in range(N)}

perms = nums.copy()

for _ in range(len(nums)-1):
	perms = {p+j for p in perms for j in nums if j not in p}
M=1000000
print(sorted(list(perms))[M-1])