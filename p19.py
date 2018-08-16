#this spits out 172, still trying to figure out why
months = {i:None for i in range(1,13)}
years = {i:months.copy() for i in range(1,101)}
for y in range(1,101):
	for m in range(1,13):
		if m in [4,6,9,11]:
			years[y][m]=list(range(1,31))
			continue
		if m in [1,3,5,7,8,10,12]:
			years[y][m]=list(range(1,32))
			continue
		if y%4==0 and (y%100!=0 or y%400==0):
			years[y][m]=list(range(1,30))
			continue
		years[y][m]=list(range(1,29))

dayslists = []
for y in range(1,101):
	for m in range(1,13):
		dayslists.append(years[y][m])
t = 0
for i in range(1,len(dayslists)):
	dayslists[i] = [x+dayslists[i-1][-1] for x in dayslists[i]]

for i,m in enumerate(dayslists):
	if m[0]%7==0:
		print(i+1)
		t=t+1

print(t)