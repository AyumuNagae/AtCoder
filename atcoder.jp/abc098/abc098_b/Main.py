n = int(input()); s = input(); tmp = 0; ans = 0;

for i in range(n):
  a = set(s[:i])
  b = set(s[i:])
  tmp = len(a&b)
  ans = max(ans,tmp)
print(ans)