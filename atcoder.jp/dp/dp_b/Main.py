n,k  = map(int, input().split())
h = list(map(int, input().split()))
dp = [float('inf')]*n
dp[0]=0
dp[1] = abs(h[1]-h[0])
tmp = 0
for i in range(2,n):
  for j in range(1, k+1):
    if j>i:
      continue
    tmp = dp[i-j] + abs(h[i]-h[i-j])
    dp[i] = min(dp[i], tmp)
print(dp[n-1])