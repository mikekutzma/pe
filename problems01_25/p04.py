from peutil import *

l = range(900,1000)
print(max([z for z in [x*y for x in l for y in l] if ispalindrome(z)]))