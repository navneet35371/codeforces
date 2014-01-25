t = input()

a = [4,7,44,47,74,77,444,447,474,477,744,747,774,777]

for i in range(0,len(a)):
	if(t % a[i] == 0):
		print "YES"
		break
	if(i == 13):
		print "NO"