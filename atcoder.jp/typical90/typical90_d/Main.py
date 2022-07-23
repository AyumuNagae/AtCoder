h,w = map(int, input().split())
s = [list(map(int, input().split())) for i in range(h)]
ans = [[0] * w for _ in range(h)]

#縦合計
y = [0] * w
for i in range(w):
  cnt = 0
  for j in range(h): 
    cnt += s[j][i]
  y[i] = cnt

#横合計
x = [0] * h
for i in range(h):
  cnt = 0
  for j in range(w):
    cnt += s[i][j]
  x[i] = cnt

for i in range(h):
  for j in range(w):
    ans[i][j] = x[i] + y[j] - s[i][j]

for i in range(h):
  print(*ans[i])