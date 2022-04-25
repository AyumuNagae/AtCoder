n = int(input())
p = [0,0,0]
for _ in range(n):
  t,x,y = map(int,input().split())
  c = t - p[0]
  d = abs(x-p[1])+abs(y-p[2])
  if d <= c and d%2 == c%2:
    p = [t,x,y]
  else:
    print("No")
    exit()
print("Yes")