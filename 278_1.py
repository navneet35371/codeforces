n=input()
r=map(int, raw_input().split())
n=map(int, raw_input().split())
s=sum(r[min(n)-1:max(n)-1])
print min(s, sum(r) - s)