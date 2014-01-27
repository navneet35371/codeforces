t = input()
a = [int(x) for x in raw_input().split()]
d = 0.0
for i in range(0,t):
	d += (a[i]/100.0)*(1.0/t)

print d*100