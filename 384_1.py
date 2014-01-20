t = input()
if(t == 1):
	print '1'
elif(t % 2 == 1):
	print ((t*t)/2)+1
else:
	print ((t*t)/2)
s1 = ''
s2 = ''
for i in range (t):
	if(i %2 == 0):
		s1+='C'
		s2+='.'
	else:
		s1+='.'
		s2+='C'
for i in range (t):
	if(t == 1):
		print 'C'
		break
	if(i %2 == 0):
		print s1
	else:
		print s2
