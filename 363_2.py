n, k = [int(_) for _ in raw_input().split()]

h = [int(_) for _ in raw_input().split()]

sums = [sum(h[:k])]
for i in range(1, n - k + 1):
    sums.append(sums[-1] + h[i + k - 1] - h[i-1])
    
print(sums.index(min(sums)) + 1)
