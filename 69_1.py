t = input()
a = [0]*3
for i in range(t):
	a = map(sum,zip(a,[int(x) for x in raw_input().split()]))
if(set(a) == set([0])):
	print "YES"
else:
	print "NO"