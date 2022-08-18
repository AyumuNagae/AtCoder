x,y = map(int, input().split())
z = [0,1,2]
if x == y:print(x)
else:
  z.remove(x)
  z.remove(y)
  print(*z)