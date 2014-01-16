import sys

t = input()
st = 5
while 1:
	if(t < st):
		break
	t -= st;
	st *= 2

tmp = 1
a = ["Sheldon", "Leonard", "Penny", "Rajesh" ,"Howard"]
for i in range(0,5):
	if(t == 0):
		print "Howard"
		break
	tmp+=st/5
	if(tmp > t):
		print a[i]
		break