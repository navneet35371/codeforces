import sys
import fractions

a,b,n = [int(x) for x in raw_input().split()]

cnt = 0

while 1:
	cnt+=1
	if(cnt % 2 == 1):
		gc = fractions.gcd(n,a)
		n-=gc
	else:
		gc = fractions.gcd(n,b)
		n-=gc
	if(n < 0):
		break
if(cnt % 2 == 0):
	print '0'
else:
	print '1'