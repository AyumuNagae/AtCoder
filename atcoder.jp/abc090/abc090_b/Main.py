a,b = map(int, input().split()); ans = 0;
for i in range(a, b+1):
  si = str(i)
  if si == si[::-1]: ans += 1
print(ans)