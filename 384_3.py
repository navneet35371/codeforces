t = input()

a = [int(x) for x in raw_input().split()]

no1 = a.count(1)
no0 = a.count(0)
n1 = no1
n2 = no0
b = [0]*t
for i in range (0,t):
	print no0,no1
	if(a[i] == 0):
		b[i] = n1-no1 + no0 -1
		no0-=1
	else:
		b[i] = n1-no1 + no0 -1
		no1-=1
print b
a1 = 0
a2 = 0
a3 = 0
a4 = 0
for i in range(0,t):
	if(a[i] == 0):
		a1 += b[i]
	else:
		a2 += b[i]
for i in range(t-1,-1,-1):
	if(a[i] == 0):
		a3 += b[i]
	else:
		a4 += b[i]
print min(a1,a2,a3,a4)