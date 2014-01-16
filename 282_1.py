import sys

t = input()
ans = 0
for i in range(0,t):
	s = raw_input()
	if(s[1] == "+"):
		ans+=1
	else:
		ans-=1

print ans