n,r = map(int, input().split())
ans = 1
for i in range(r):
  ans *= (n-i)
  ans //= (i+1)
print(ans)