import sys

n = input()

d = 1;
ans = 1;

for i in range(n):
	ans = (d-ans+1000000007)%1000000007;
	d = d*3%1000000007
print ans