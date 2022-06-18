n,a,b = map(int, input().split())
if abs(a)+abs(b) <= n and n%2 == (a+b)%2:
  print('Yes')
else:
  print('No')