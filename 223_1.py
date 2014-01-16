import sys
import math
t = input()

a =  [int(x) for x in raw_input().split()]
x = 0
y = t-1
s = 0
t1 = 0
for i in range(0,t):
	if(i % 2 == 0):
		if(a[x] > a[y]):
			s+= max(a[x],a[y])
			x+=1
		else:
			s+= max(a[x],a[y])
			y-=1
	else:
		if(a[x] > a[y]):
			t1+= max(a[x],a[y])
			x+=1
		else:
			t1+= max(a[x],a[y])
			y-=1
print s,t1