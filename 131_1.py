import sys
s = raw_input()

s = s.swapcase()
if(s.islower()):
	print s
elif(s.istitle()):
	print s
else:
	print s.swapcase()