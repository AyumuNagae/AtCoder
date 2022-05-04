n,x = map(int,input().split())
m = [int(input()) for _ in range(n)]
ans = len(m)
x = x - sum(m)
while x >= min(m):
  x = x - min(m)
  ans += 1
print(ans)