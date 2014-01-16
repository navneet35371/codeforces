import sys

t = input()
ans = 0
for i in range(0,t):
	a,b,c = [int(x) for x in raw_input().split()]
	if(a+b+c > 1):
		ans+=1
print ans