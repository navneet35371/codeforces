import sys
n = input()
a = map(int, raw_input().split())

i = a.index(max(a))

j = a[::-1].index(min(a))

print i + j - (i > n - 1 - j)