import sys

t = input()
s = ''
for i in range(0,t):
	a =  [x for x in raw_input().split()]
	if(len(s) > 100001):
		p = ''
	elif(int(a[0]) == 1):
		s += a[1]
	else:
		xt = s[:int(a[1])]*int(a[2])
		s+=xt 
val = input()
a =  [int(x) for x in raw_input().split()]
for i in range(0,val):
	print s[a[i]-1],