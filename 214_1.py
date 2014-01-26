n,m=map(int,raw_input().split())
r=range(32)
print(sum(a*a+b-n==a+b*b-m==0 for a in r for b in r))