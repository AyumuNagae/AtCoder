a,b = map(int, input().split())
ans = 0;tmp = 1;
while tmp < b:
  tmp = tmp + (a-1)
  ans += 1
print(ans)