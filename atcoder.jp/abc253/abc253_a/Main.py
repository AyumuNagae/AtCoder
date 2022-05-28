a = list(map(int, input().split()))
m = a[1]
a = sorted(a)
n = a[1]

if m == n:
  print('Yes')
else:
  print('No')