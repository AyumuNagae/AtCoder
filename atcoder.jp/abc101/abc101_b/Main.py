s = input(); n = int(s);
ss = 0
for i in s:
  ss += int(i)
print('Yes' if n%ss == 0 else'No')