import sys
import math
t = input()
c= 0
a =  [int(x) for x in raw_input().split()]
a.sort()
maxi = 0
vis = [0]*t
ans = [0]*t
for i in range(0,t):
	if(a[i] > maxi):
		maxi = a[i]
		vis[i] = 1
		ans[c] = a[i]
		c+=1
for i in range(t-1,-1,-1):
	if((a[i] < maxi) and (vis[i] == 0) ):
		maxi = a[i]
		ans[c] = a[i]
		c+=1
print c

for i in range(0,c):
	print ans[i],