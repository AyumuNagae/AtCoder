a,b,c,x,y=map(int,input().split())
ans= a*x + b*y

for i in range(x+y):
  ans=min(ans,  c*i*2  +  a*max(0,x-i)  +  b*max(0,y-i)  )

print(ans)