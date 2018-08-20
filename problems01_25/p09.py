import math
print([int(i*j*math.sqrt(i**2 + j**2)) for i in range(1,499) for j in range(1,i) if math.floor(math.sqrt(i**2 + j**2))==math.sqrt(i**2 + j**2) and i+j+math.sqrt(i**2 + j**2)==1000][0])