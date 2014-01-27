n,m = map(int,raw_input().split())

s = (n*(n+1))/2
t = m % s

for i in xrange(1,n+1):
	if(t < i):
		print t
		break
	t-=i