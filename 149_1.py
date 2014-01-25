t = input()
a = [int(x) for x in raw_input().split()]
a = sorted(a)[::-1]
ans = 0
temp = 0
for i in range(12):
	if(temp < t):
		ans+=1
		temp += a[i]
	else:
		break;
if(temp < t):
	print '-1'
else:
	print ans