n = int(input())
l = list(map(int, input().split()))
m = max(l)
l.remove(m)
if sum(l)>m:
  print('Yes')
else:
  print('No')