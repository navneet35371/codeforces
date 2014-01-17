a,b,w,x,c = [int(x) for x in raw_input().split()]
ans = 0
while(not(c <= a)):
	print a,b,c
	ans +=1
	c-=1
	if(b>=x):
		b=b-x
	else:
		a= a-1
		b=w-(x-b)
		

print ans