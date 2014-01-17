import sys

s = raw_input()
l1 = len(s)
s = s.translate(None,'HQ9')

if(len(s) == l1):
	print 'NO'
else:
	print 'YES'