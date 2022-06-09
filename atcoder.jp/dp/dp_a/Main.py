n=int(input())
h=list(map(int,input().split()))
dp=[0]*n
dp[1]=abs(h[1]-h[0])
for x in range(2,n):
  dp[x]=min(dp[x-1]+abs(h[x]-h[x-1]),dp[x-2]+abs(h[x]-h[x-2]))
print(dp[-1])