import sys

s = raw_input()
l1 = len(s)
b  = s.translate(None,'47')
l1 -=len(b)
l1 = str(l1)
b = l1.translate(None,'47')
if(len(b) == 0):
	print 'YES'
else:
	print 'NO'