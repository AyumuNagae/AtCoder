n,m = map(int, input().split())
a = list(map(int, input().split()))
z = n - sum(a)
if z<0:
  print(-1)
else:
  print(z)