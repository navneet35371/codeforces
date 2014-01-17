s = raw_input()
t = raw_input()
idx = s.find('|')
right = len(s)-idx-1

req = abs(idx-right)

if((req > len(t)) or((idx == right)and (len(t)%2 ==1))):
	print 'Impossible'
elif((req == 0) and (len(t) % 2 == 0)):
	print t[:len(t)/2]+s+t[len(t)/2:]
elif((right > idx)and (req == len(t))):
	print t+s
elif((right < idx)and (req == len(t))):
	print s+t
else:
	print 'Impossible'
