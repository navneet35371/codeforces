import sys

t = input()

for i in range(0,t):
	s = raw_input()
	l = len(s)
	if(l > 10):
		print s[0]+str(l-2)+s[l-1]
	else:
		print s