t = input()
a = [int(x) for x in raw_input().split()]
ma = a[0]
mi = a[0]
ans = 0
for i in range (1,t):
	if(ma < a[i]):
		ans+=1
		ma = a[i]
	if(mi > a[i]):
		ans+=1
		mi = a[i]
print ans
