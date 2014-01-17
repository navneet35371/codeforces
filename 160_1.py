import sys

t = input()

a = [int(x) for x in raw_input().split()]
b = sum(a)/2
a.sort(reverse=True)
ans = 0
for i in range (0,t):
	ans += a[i]
	if(ans > b):
		print i+1
		break