n, m = map(int,input().split())
ans = [0] * n
for i in range(m):
  a, b = map(int,input().split())
  # a<bということは、bが小さいaを持っているということ
  if a < b: ans[b - 1] += 1
  else:     ans[a - 1] += 1
print(ans.count(1))