def spiralsum(N):
    s=0
    for i in range(N):
        s=s+ ((2*i + 1)**2 - 3*i)
    return 4*s - 3


print(spiralsum(501))