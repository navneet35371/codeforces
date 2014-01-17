t = input()

a = [int(x) for x in raw_input().split()]

a = set(a)
print max(a) - len(a)
for i in range(1,max(a)):
	if i not in a:
		print i,