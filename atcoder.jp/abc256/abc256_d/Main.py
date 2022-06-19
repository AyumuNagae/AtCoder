n = int(input())
lr = [list(map(int, input().split())) for _ in range(n)]
lr.sort()
tmp = lr[0]
for i in range(1,n):
  if lr[i][0] <= tmp[1] and lr[i][1] > tmp[1]:
    tmp[1] = lr[i][1]
  elif lr[i][0] > tmp[1]:
    print(*tmp)
    tmp.clear()
    tmp = lr[i]

print(*tmp)