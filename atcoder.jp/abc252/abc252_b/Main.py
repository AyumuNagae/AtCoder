n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
al = []

for i in b:
  al.append(a[i-1])
if max(a) not in al:
  print('No')
else:
  print('Yes')