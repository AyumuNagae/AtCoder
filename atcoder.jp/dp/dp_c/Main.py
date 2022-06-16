n = int(input())
dp = [[0,0,0] for _ in range(n)]
field = [list(map(int,input().split())) for _ in range(n)]
dp[0]=field[0]

for i in range(1,n):
  dp[i][0] = max(dp[i-1][1],dp[i-1][2])+field[i][0]
  dp[i][1] = max(dp[i-1][0],dp[i-1][2])+field[i][1]
  dp[i][2] = max(dp[i-1][0],dp[i-1][1])+field[i][2]
print(max(dp[n-1]))