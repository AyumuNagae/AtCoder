n,m,t  = map(int, input().split())
a = list(map(int, input().split()))
for i in range(m):
  x,y = map(int, input().split())
  a[x-1] -= y
for i in a:
  t-=i
  if t<=0:exit(print("No"))
print("Yes")