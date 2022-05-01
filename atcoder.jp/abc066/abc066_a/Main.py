a,b,c = map(int, input().split())
m = 0
ans= 0
m = max(a,b,c)
if m == a:
  ans = b +c
elif m == b:
  ans = a+c
elif m == c:
  ans = a+b
print(ans)