n, k = map(int, input().split())
a = list(map(int, input().split()))
order = sorted(range(n), key=lambda x: a[x])
ans = [k // n] * n
for i in range(k % n):
  ans[order[i]] += 1
print(*ans, sep='\n')