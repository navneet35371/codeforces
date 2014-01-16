import sys

s = raw_input()
s = s.lower()
s = s.translate(None,"aoeuiy")
for i in range(0,len(s)):
	sys.stdout.write('.'+s[i])