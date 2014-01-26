r,c = map(int, raw_input().split())
row = [0]*r
col = [0]*c
for i in range(r):
    line = raw_input()
    if "S" in line:
        row[i] = 1
    else:
        row[i] = 0
    for j in range(c):
        if line[j]=='S':
            col[j] = 1
print(row.count(0)*c + col.count(0)*r - row.count(0)*col.count(0))