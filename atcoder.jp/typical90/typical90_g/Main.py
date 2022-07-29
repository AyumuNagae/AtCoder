from bisect import bisect_left
n = int(input())
a = list(map(int,input().split()))
q = int(input())
B = [int(input()) for _ in range(q)]
a.sort()

for b in B:
  x = bisect_left(a, b)
  if   x == 0:print(a[0] - b)
  elif x == n:print(b - a[-1])
  else:print(min(b - a[x - 1], a[x] - b))