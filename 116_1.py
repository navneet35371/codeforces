import sys
import math
t = input()
ans = 0
ins = 0
out = 0
curr = 0
for i in range(0,t):
	a,b = [int(x) for x in raw_input().split()]
	curr = curr-a+b
	ans = max(ans,curr)
print ans