def digitsum(x):
    return sum([int(a)**5 for a in str(x)])

dslist = []
for n in range(10,9999999):
    if digitsum(n)==n:
        print(n)
        dslist.append(n)

print(dslist,sum(dslist))