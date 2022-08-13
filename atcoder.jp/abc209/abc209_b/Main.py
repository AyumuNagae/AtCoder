n,x = map(int, input().split())
a = list(map(int, input().split()))
b = len(a) // 2
if x + b - sum(a) >= 0:
  print("Yes")
else:
  print("No")