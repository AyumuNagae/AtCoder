s = input(); n = int(s); ss = 0

for i in s:
  ss = ss + int(i)
if n%ss == 0:
  print('Yes')
else:
  print('No')