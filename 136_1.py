t = input()

a = [int(x) for x in raw_input().split()]

b = [0]*101

for i in range(0,t):
	b[a[i]] = i+1

for i in range(1,t+1):
	print b[i],

