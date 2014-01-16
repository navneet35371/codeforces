import sys

n,k = [int(x) for x in raw_input().split()]

a = [int(x) for x in raw_input().split()]
ans = 0
for i in range(0,n):
	if(a[i]>=a[k-1] and a[i] != 0):
		ans+=1

print ans 