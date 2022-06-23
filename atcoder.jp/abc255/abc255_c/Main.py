x,a,d,n=map(int,input().split())
x-=a
if d<0:x,d=-x,-d
ans = 0
if (n-1)*d>x>0:
  ans = min(x%d,-x%d)
else:
  ans = [-x,x-n*d+d][x>0]
print(ans)