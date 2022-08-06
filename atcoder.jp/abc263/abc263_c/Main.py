from itertools import combinations as c
n,m = map(int, input().split())
for v in c(range(1,m+1),n):
  print(*v)