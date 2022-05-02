n = int(input())
lr = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i,j in lr:
  ans = ans + j - i + 1
print(ans)