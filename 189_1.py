l=map(int,raw_input().split())
n=l[0]
l=l[1:]
d=(n+1)*[-1]
d[0]=0
for i in range(1,n+1):
    for j in l:
        if i-j>=0 and d[i-j]!=-1:
            d[i]=max(d[i],d[i-j]+1)
            print i,j
print d
print d[n]