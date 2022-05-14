s = input(); t = input();
for _ in range(len(s)):
  s = s + s[0]
  s = s[1:]
  if s == t:
    print('Yes')
    exit()
print('No')