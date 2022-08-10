n,x = map(int, input().split())
cnt = 0
x *= 100
for i in range(n):
  cnt += 1
  v,p = map(int, input().split())
  x -= v*p
  if x < 0:
    exit(print(cnt))
print(-1)